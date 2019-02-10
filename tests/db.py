from unittest import TestCase, mock
from src.db import Db
from src.table import Table
from src.field import Field

class TestDb(TestCase):
    def test_instanciation(self):
        table = mock.Mock(spec=Table)

        db = Db([table])

    def test_insert(self):
        table = mock.Mock(spec=Table)
        table.name = 'users'

        db = Db([table])
        db.insert('users', id=2, name='Roger')
        table.insert.assert_called_once_with(id=2, name='Roger')

    def test_exception_if_table_does_not_exist(self):
        table = mock.Mock(spec=Table)
        table.name = 'users'

        db = Db([table])
        with self.assertRaises(Exception):
            db.insert('despacito', id=2)

    def test_export(self):
        table = mock.Mock(spec=Table)
        table.name = 'users'
        table.export.return_value = [
            {'id': 1, 'name': 'Roger'},
            {'id': 2, 'name': 'Patrick'}
        ]

        db = Db([table])
        self.assertEqual(db.export(), [
            {'users': [
                {'id': 1, 'name': 'Roger'},
                {'id': 2, 'name': 'Patrick'}
            ]}
        ])
