from unittest import TestCase
from src.db import Db
from src.table import Table
from src.field import Field

class TestDb(TestCase):
    def test_instanciation(self):
        table = Table('users', [
            Field('id', 'int', primary_key=True),
            Field('name', 'str'),
            Field('age', 'int', nullable=True)
        ])

        db = Db([table])

    def test_insert(self):
        table = Table('users', [
            Field('id', 'int', primary_key=True),
            Field('name', 'str'),
            Field('age', 'int', nullable=True)
        ])

        db = Db([table])
        db.insert('users', id=2, name='Roger')

    def test_exception_if_table_does_not_exist(self):
        table = Table('users', [
            Field('id', 'int', primary_key=True)
        ])

        db = Db([table])
        with self.assertRaises(Exception):
            db.insert('despacito', id=2)
