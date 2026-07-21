import os
import csv
import json
# pyrefly: ignore [missing-import]
import pytest
from data_processor.readers import CSVReader, JSONReader, ExcelReader
from data_processor.writers import CSVWriter, JSONWriter

try:
    import openpyxl
except ImportError:
    openpyxl = None

def test_csv_read_write(tmp_path):
    filepath = tmp_path / "test.csv"
    data = [
        {"id": "1", "name": "Alice", "age": "30"},
        {"id": "2", "name": "Bob", "age": "25"}
    ]
    
    # Write using standard csv
    with open(filepath, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=["id", "name", "age"])
        writer.writeheader()
        writer.writerows(data)
        
    reader = CSVReader(str(filepath))
    read_data = reader.read()
    assert read_data == data

    # Test writer
    out_filepath = tmp_path / "out.csv"
    writer_obj = CSVWriter(str(out_filepath))
    writer_obj.write(read_data)
    
    # Read back to verify
    reader2 = CSVReader(str(out_filepath))
    assert reader2.read() == data


def test_json_read_write(tmp_path):
    filepath = tmp_path / "test.json"
    data = [
        {"id": 1, "name": "Alice", "active": True},
        {"id": 2, "name": "Bob", "active": False}
    ]
    
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f)
        
    reader = JSONReader(str(filepath))
    read_data = reader.read()
    assert read_data == data

    # Test writer
    out_filepath = tmp_path / "out.json"
    writer_obj = JSONWriter(str(out_filepath))
    writer_obj.write(read_data)
    
    reader2 = JSONReader(str(out_filepath))
    assert reader2.read() == data

def test_json_read_invalid(tmp_path):
    filepath = tmp_path / "invalid.json"
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump({"not": "a list"}, f)
        
    reader = JSONReader(str(filepath))
    with pytest.raises(ValueError):
        reader.read()

@pytest.mark.skipif(openpyxl is None, reason="openpyxl is not installed")
def test_excel_read(tmp_path):
    filepath = tmp_path / "test.xlsx"
    
    # Create a test Excel file
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.append(["id", "name", "score"])
    ws.append([1, "Alice", 95])
    ws.append([2, "Bob", 88])
    wb.save(filepath)
    
    reader = ExcelReader(str(filepath))
    read_data = reader.read()
    
    # Note that Excel numeric cells will be read as integers/floats, not strings.
    # The header is converted to strings in the reader.
    expected_data = [
        {"id": 1, "name": "Alice", "score": 95},
        {"id": 2, "name": "Bob", "score": 88}
    ]
    
    assert read_data == expected_data
