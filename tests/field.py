from unittest import TestCase
from src.field import Field

class TestField(TestCase):
    def test_exception_if_bad_type(self):
        with self.assertRaises(Exception):
            field = Field('some_name', 'some_invalid_type')

    def test_normal_instanciation(self):
        field = Field('some_name', 'string')
