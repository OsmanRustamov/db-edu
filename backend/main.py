import sys
sys.path.insert(1, '../')
import asyncio
import uvicorn
from os import path
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.common import Config, Database
from backend.routes import routes


class SqlLiteConfig(Config):
    __dsn: str = None

    def check(self) -> bool | Exception:
        super().check()
        database_file = self.get('DB_FILE')
        if not database_file:
            raise Exception('DB_FILE is undefined')
        database_path = path.abspath(database_file)
        self.__dsn = f'sqlite:///{database_path}'
        return True

    @property
    def dsn(self) -> str | None:
        return self.__dsn


config = SqlLiteConfig(path.abspath('default.config.env'))
Database.config(config)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)
for route in routes:
    app.include_router(route)


async def main():
    web_config = uvicorn.Config(
        'main:app',
        host=config.get('WEB_HOST', '127.0.0.1'),
        port=int(config.get('WEB_PORT', 5000)),
        log_level=config.get('WEB_LOG_LEVEL', 'info' if not bool(config.get('DEBUG')) else 'debug')
    )
    server = uvicorn.Server(web_config)
    await server.serve()


if __name__ == '__main__':
    asyncio.run(main())
