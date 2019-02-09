from unittest import TestCase
from src.table import Table
from src.field import Field

class TestTable(TestCase):
    def test_normal_instanciation(self):
        fields = [
            Field('id', 'int', primary_key=True),
            Field('name', 'string')
        ]

        table = Table('table_name', fields)

    def test_instanciation_with_bad_primary_key_config(self):
        fields = [
            Field('name', 'string')
        ]

        # No primary key
        with self.assertRaises(Exception):
            table = Table('table_name', [Field('name', 'string')])

        # Several primary keys
        with self.assertRaises(Exception):
            table = Table('table_name', [
                Field('id_1', 'int', primary_key=True),
                Field('id_2', 'int', primary_key=True)
            ])
