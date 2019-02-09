from typing import List
from .table import Table

class Db:
    def __init__(self, tables: List[Table]):
        self.tables = tables
