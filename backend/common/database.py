from sqlalchemy.orm import Session
from sqlalchemy.engine import create_engine
from backend.common import Config
from backend.orm import Base as OrmBase


class Database:
    __session: Session = None

    @staticmethod
    def config(config: Config):
        if Database.__session:
            Database.__session.close()
        engine = create_engine(config.dsn, echo=bool(config.get('debug', False)))
        Database.__session = Session(autoflush=False, bind=engine)
        OrmBase.metadata.create_all(bind=engine)

    @staticmethod
    def get_session() -> Session | Exception:
        if Database.__session is None:
            raise Exception('Please config db connection')
        return Database.__session
