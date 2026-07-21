from typing import Any, List
from .core import DataTransformer, DataType

class ColumnFilter(DataTransformer):
    """Keeps only the specified columns (keys) in the data."""
    
    def __init__(self, columns_to_keep: List[str]):
        self.columns_to_keep = columns_to_keep
        
    def transform(self, data: DataType) -> DataType:
        transformed_data = []
        for row in data:
            new_row = {k: v for k, v in row.items() if k in self.columns_to_keep}
            transformed_data.append(new_row)
        return transformed_data


class MissingValueImputer(DataTransformer):
    """Replaces missing or empty string values for a specific column with a default value."""
    
    def __init__(self, column: str, default_value: Any):
        self.column = column
        self.default_value = default_value
        
    def transform(self, data: DataType) -> DataType:
        transformed_data = []
        for row in data:
            new_row = row.copy()
            val = new_row.get(self.column)
            if val is None or val == "":
                new_row[self.column] = self.default_value
            transformed_data.append(new_row)
        return transformed_data


class TypeCaster(DataTransformer):
    """Casts a specific column to a new type."""
    
    def __init__(self, column: str, new_type: type):
        self.column = column
        self.new_type = new_type
        
    def transform(self, data: DataType) -> DataType:
        transformed_data = []
        for row in data:
            new_row = row.copy()
            if self.column in new_row and new_row[self.column] is not None:
                try:
                    new_row[self.column] = self.new_type(new_row[self.column])
                except (ValueError, TypeError):
                    pass # Keep original if cast fails, or we could raise it depending on requirements.
            transformed_data.append(new_row)
        return transformed_data
