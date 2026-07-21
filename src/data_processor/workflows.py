from typing import List, Optional
from .core import DataReader, DataTransformer, DataWriter, DataType

class DataPipeline:
    """Automates a data processing workflow."""
    
    def __init__(self, reader: DataReader, writer: Optional[DataWriter] = None):
        """
        Initializes the pipeline with a source and an optional destination.
        """
        self.reader = reader
        self.writer = writer
        self.transformers: List[DataTransformer] = []
        
    def add_transformer(self, transformer: DataTransformer) -> "DataPipeline":
        """Adds a transformer to the workflow pipeline. Returns self for chaining."""
        self.transformers.append(transformer)
        return self
        
    def run(self) -> DataType:
        """
        Executes the workflow:
        1. Read data
        2. Apply all transformers sequentially
        3. (Optional) Write data
        4. Return the processed data
        """
        print("Reading data...")
        data = self.reader.read()
        
        for idx, transformer in enumerate(self.transformers):
            print(f"Applying transformation {idx + 1}: {transformer.__class__.__name__}...")
            data = transformer.transform(data)
            
        if self.writer:
            print(f"Writing data to destination using {self.writer.__class__.__name__}...")
            self.writer.write(data)
            
        print("Workflow completed.")
        return data
