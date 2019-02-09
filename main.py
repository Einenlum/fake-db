from src.field import Field
from src.table import Table
from src.db import Db

fields = [
    Field('id', 'int', primary_key=True),
    Field('name', 'string'),
    Field('city', 'string', nullable=True),
    Field('activated', 'bool')
]
table = Table('users', fields)

db = Db([table])

print(Db)
