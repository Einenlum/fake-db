from unittest import TestCase, mock
from src.table import Table
from src.field import Field

class TestTable(TestCase):
    def test_normal_instanciation(self):
        fields = [
            Field('id', 'int', primary_key=True),
            Field('name', 'str')
        ]

        table = Table('table_name', fields)

    def test_instanciation_with_bad_primary_key_config(self):
        fields = [
            Field('name', 'str')
        ]

        # No primary key
        with self.assertRaises(Exception):
            table = Table('table_name', [Field('name', 'str')])

        # Several primary keys
        with self.assertRaises(Exception):
            table = Table('table_name', [
                Field('id_1', 'int', primary_key=True),
                Field('id_2', 'int', primary_key=True)
            ])

    def test_check_insert(self):
        fields = [
            Field('id', 'int', primary_key=True),
            Field('name', 'str')
        ]

        table = Table('users', fields)
        table.insert(id=1, name='Pierre')

        self.assertTrue(len(table.values) == 1)

    def test_check_exception_if_not_nullable_field_missing(self):
        fields = [
            Field('id', 'int', primary_key=True),
            Field('name', 'str')
        ]

        table = Table('users', fields)
        with self.assertRaises(Exception):
            table.insert(name='Pierre')

    def test_check_no_exception_if_nullable_field_missing(self):
        fields = [
            Field('id', 'int', primary_key=True),
            Field('name', 'str'),
            Field('age', 'int', nullable=True)
        ]

        table = Table('users', fields)
        table.insert(id=5, name='Pierre')

    def test_check_exception_if_wrong_type(self):
        fields = [
            Field('id', 'int', primary_key=True),
            Field('name', 'str')
        ]

        table = Table('users', fields)
        with self.assertRaises(Exception):
            table.insert(id='test', name='Pierre')

    def test_export(self):
        fields = [
            Field('id', 'int', primary_key=True),
            Field('name', 'str'),
            Field('age', 'int', nullable=True)
        ]

        table = Table('users', fields)
        table.insert(id=5, name='Pierre')
        table.insert(id=6, name='Roger')

        self.assertEqual(table.export(), [
            {'id': 5, 'name': 'Pierre'},
            {'id': 6, 'name': 'Roger'}
        ])

    def test_get_with_non_matching_search(self):
        field = mock.Mock(spec=Field)
        field.primary_key = True
        table = Table('users', [field])
        table.values = [
            {'id': 1, 'name': 'Pascal'},
            {'id': 2, 'name': 'Martine'}
        ]

        self.assertEqual(table.get_with_value('name', 'José'), [])

    def test_get_with_matching_search(self):
        field = mock.Mock(spec=Field)
        field.primary_key = True
        table = Table('users', [field])
        table.values = [
            {'id': 1, 'name': 'Pascal'},
            {'id': 2, 'name': 'Martine'}
        ]

        self.assertEqual(table.get_with_value('name', 'Martine'), [
            {'id': 2, 'name': 'Martine'}
        ])
