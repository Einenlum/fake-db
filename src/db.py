from typing import List
from .field import Field

class Db:
    def __init__(self, fields: List[Field]):
        self.fields = fields

    def __is_initiated(self):
        return len(self.fields) > 0

