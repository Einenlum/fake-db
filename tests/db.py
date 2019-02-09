from unittest import TestCase
from src.db import Db
from src.table import Table
from src.field import Field

class TestDb(TestCase):
    def test_instanciation(self):
        table = Table('users', [
            Field('id', 'int', primary_key=True),
            Field('name', 'string'),
            Field('age', 'int', nullable=True)
        ])

        db = Db([table])
