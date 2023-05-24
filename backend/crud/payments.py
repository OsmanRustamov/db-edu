from typing import Type
from sqlalchemy.orm import Session, Query
from sqlalchemy.exc import IntegrityError
from backend import orm
from backend.common.exceptions import CrudException, CrudNotFoundException
from backend.orm import Payments


class Crud:
    @staticmethod
    def all(session: Session) -> list[Type[Payments]]:
        return session.query(orm.Payments).all()

    @staticmethod
    def one(session: Session, code: str, only_query: bool = False) -> orm.Payments | Query | None:
        query = session.query(orm.Payments).filter(orm.Payments.payments_code.like(f'{code}'))
        return query if only_query else query.first()

    @staticmethod
    def create(session: Session, data: dict) -> orm.Payments | CrudException:
        item = orm.Payments(**data)
        try:
            session.add(item)
            session.commit()
        except IntegrityError as e:
            session.rollback()
            raise CrudException(str(e.__cause__))
        session.refresh(item)
        return item

    @staticmethod
    def update(session: Session, code: str, data: dict) -> orm.Payments | CrudException | CrudNotFoundException:
        item = Crud.one(session, code)
        if not item:
            raise CrudNotFoundException(f'Payments with code = {code} not found')
        try:
            item.fill(data)
            session.add(item)
            session.commit()
        except IntegrityError as e:
            session.rollback()
            raise CrudException(str(e.__cause__))
        session.refresh(item)
        return item

    @staticmethod
    def delete(session: Session, code: str) -> CrudException | CrudNotFoundException | None:
        item = Crud.one(session, code)
        if not item:
            raise CrudNotFoundException(f'Payments with code = {code} not found')
        try:
            Crud.one(session, code, True).delete()
            session.commit()
        except IntegrityError as e:
            session.rollback()
            raise CrudException(str(e.__cause__))
        return None