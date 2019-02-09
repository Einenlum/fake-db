from typing import List
from .field import Field

class Db:
    @classmethod
    def init(cls, fields: List[Field]):
        cls.fields = fields

    def is_initiated(cls):
        return len(cls.fields) > 0

