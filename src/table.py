from typing import List
from .field import Field

class Table:
    def __init__(self, name: str, fields: List[Field]):
        self.__check_primary_key_is_present(fields)

        self.name = name
        self.fields = fields
        self.values = []

    def insert(self, **values):
        missing_fields_names = self.__get_missing_fields_names(list(values.keys()))
        for missing_field_name in missing_fields_names:
            missing_field = self.__get_field(missing_field_name)
            if not missing_field.nullable:
                raise Exception(f"The field {missing_field_name} is not nullable")

        for field_name, value in values.items():
            field = self.__get_field(field_name)
            field.check_value_integrity(value)

        self.values.append({
            **values
        })

    def __get_missing_fields_names(self, fields_names):
        return [field.name for field in self.fields if
                                field.name not in fields_names]

    def __get_field(self, field_name):
        for field in self.fields:
            if field.name == field_name:
                return field
        raise Exception(f"No field {field_name} was found")

    def __check_primary_key_is_present(self, fields: List[Field]):
        primary_keys = [field for field in fields if field.primary_key]
        if (len(primary_keys) != 1):
            raise Exception('Table must have one primary key, and only one')
