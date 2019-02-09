from src.field import Field
from src.db import Db

fields = [
    Field('id', 'int', primary_key=True),
    Field('name', 'string'),
    Field('city', 'string', nullable=True),
    Field('activated', 'bool')
]

db = Db(fields)

print(Db)
