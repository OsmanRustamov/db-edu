import unittest
from os import path, unlink
from backend.common import Config


class TestConfig(unittest.TestCase):
    data: dict = {
        'key': 'Value',
        'key2': 2
    }
    filename: str = path.abspath('./test.env')

    def __unlink(self):
        if path.exists(self.filename) and path.isfile(self.filename):
            unlink(self.filename)

    def __check(self, config: Config):
        self.assertEquals(config.get('key'), self.data['key'])
        self.assertEquals(config.get('other'), None)
        self.assertEquals(config.get('key', 'lower'), self.data['key'])
        self.assertEquals(config.get('other', 'lower'), 'lower')
        self.assertEquals(config.dsn, None)

    def setUp(self) -> None:
        self.__unlink()
        with open(self.filename, mode='w') as file:
            for key, value in self.data.items():
                file.write(f'{str(key).upper()}={str(value)}\n')

    def tearDown(self) -> None:
        self.__unlink()

    def test_config_with_dict(self):
        self.__check(Config(self.data))

    def test_config_with_file(self):
        self.__check(Config(self.filename))


if __name__ == '__main__':
    unittest.main()
