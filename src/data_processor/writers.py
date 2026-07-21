import csv
import json
from .core import DataWriter, DataType

class CSVWriter(DataWriter):
    """Writes data to a CSV file."""
    
    def __init__(self, filepath: str, delimiter: str = ','):
        self.filepath = filepath
        self.delimiter = delimiter
        
    def write(self, data: DataType) -> None:
        if not data:
            # If there's no data, create an empty file
            with open(self.filepath, mode='w', encoding='utf-8') as f:
                pass
            return
            
        fieldnames = []
        for row in data:
            for key in row.keys():
                if key not in fieldnames:
                    fieldnames.append(key)
        with open(self.filepath, mode='w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=self.delimiter)
            writer.writeheader()
            for row in data:
                writer.writerow(row)


class JSONWriter(DataWriter):
    """Writes data to a JSON file."""
    
    def __init__(self, filepath: str, indent: int = 4):
        self.filepath = filepath
        self.indent = indent
        
    def write(self, data: DataType) -> None:
        with open(self.filepath, mode='w', encoding='utf-8') as f:
            json.dump(data, f, indent=self.indent)
