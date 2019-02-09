from typing import List
from .field import Field

class Table:
    def __init__(self, name: str, fields: List[Field]):
        self.__check_primary_key_is_present(fields)

        self.name = name
        self.fields = fields

    def __check_primary_key_is_present(self, fields: List[Field]):
        primary_keys = [field for field in fields if field.primary_key]
        if (len(primary_keys) != 1):
            raise Exception('Table must have one primary key, and only one')
