import os
import json
from data_processor.readers import JSONReader
from data_processor.writers import JSONWriter
from data_processor.transformers import ColumnFilter, MissingValueImputer
from data_processor.workflows import DataPipeline

def test_data_pipeline(tmp_path):
    input_file = tmp_path / "in.json"
    output_file = tmp_path / "out.json"
    
    raw_data = [
        {"id": 1, "name": "Alice", "secret": "x", "age": 30},
        {"id": 2, "name": "Bob", "secret": "y", "age": None}
    ]
    
    with open(input_file, 'w', encoding='utf-8') as f:
        json.dump(raw_data, f)
        
    reader = JSONReader(str(input_file))
    writer = JSONWriter(str(output_file))
    
    pipeline = DataPipeline(reader, writer)
    pipeline.add_transformer(ColumnFilter(["id", "name", "age"]))
    pipeline.add_transformer(MissingValueImputer("age", 0))
    
    result = pipeline.run()
    
    expected = [
        {"id": 1, "name": "Alice", "age": 30},
        {"id": 2, "name": "Bob", "age": 0}
    ]
    
    assert result == expected
    
    # Verify writer output
    with open(output_file, 'r', encoding='utf-8') as f:
        written_data = json.load(f)
        
    assert written_data == expected
