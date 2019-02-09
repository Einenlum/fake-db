class Field:
    allowed_types = ['string', 'int', 'bool']
    def __init__(self, name: str, type: str, **options):
        if type not in Field.allowed_types:
            raise Exception(f'{type} is not a valid type. Valid types: {" ".join(Field.allowed_types)}.')
        self.name = name
        self.type = type

        default_options = {
            'primary_key': False,
            'nullable': False
        }
        options = {**default_options, **options}
        for key, value in options.items():
            setattr(self, key, value)
