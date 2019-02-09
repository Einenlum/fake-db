class Field:

    ALLOWED_TYPES = ['str', 'int', 'bool']

    def __init__(self, name: str, type: str, **options):
        self.__check_type_integrity(type)

        self.name = name
        self.type = type

        default_options = {
            'primary_key': False,
            'nullable': False
        }
        options = {**default_options, **options}
        for key, value in options.items():
            setattr(self, key, value)

    def check_value_integrity(self, value):
        types = {
            'str': str,
            'int': int,
            'bool': bool
        }

        for type_name, obj in types.items():
            if self.type == type_name and not isinstance(value, obj):
                raise Exception(f"The value should be of type {value} but it is { type(value) }")

    def __check_type_integrity(self, type):
        if type not in Field.ALLOWED_TYPES:
            raise Exception(f'{type} is not a valid type. Valid types: {" ".join(Field.ALLOWED_TYPES)}.')

