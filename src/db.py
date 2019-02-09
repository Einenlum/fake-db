from typing import List
from .table import Table

class Db:
    def __init__(self, tables: List[Table]):
        self.tables = tables

    def insert(self, table_name: str, **row_values):
        table = self.__get_table(table_name)

        table.insert(**row_values)

    def __get_table(self, table_name: str) -> Table:
        try:
            return [table for table in self.tables if table.name == table_name][0]
        except:
            raise Exception(f"No table was found with name {table_name}")
