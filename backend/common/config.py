from multipledispatch import dispatch
from typing import Any
from environs import Env
from os import path


class Config:
    __storage: dict | Env = {}

    @dispatch(dict)
    def __init__(self, data: dict):
        for key, value in data.items():
            self.__storage[str(key).upper()] = value
        self.check()

    @dispatch(str)
    def __init__(self, filename: str):
        if not path.exists(filename) or not (path.isfile(filename) or path.islink(filename)):
            raise Exception('Problem with config file')
        env = Env()
        env.read_env(filename)
        self.__storage = env
        self.check()

    def check(self) -> bool | Exception:
        return True

    def get(self, key: str, default: Any = None) -> Any | None:

        if type(self.__storage) == Env:
            return self.__storage(key.upper(), default=default)
        return self.__storage.get(key.upper(), default)

    @property
    def dsn(self) -> str | None:
        return


