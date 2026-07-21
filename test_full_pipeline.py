from data_processor.readers import ExcelReader
from data_processor.transformers import ColumnFilter, TypeCaster, MissingValueImputer
from data_processor.writers import CSVWriter
from data_processor.workflows import DataPipeline

if __name__ == "__main__":
    print("Testing the full DataProcessor package on Datasets.xlsx...")
    
    # 1. Setup Reader and Writer
    reader = ExcelReader('dataset/Datasets.xlsx')
    writer = CSVWriter('dataset/processed_dataset.csv')
    
    # 2. Setup Pipeline
    pipeline = DataPipeline(reader, writer)
    
    # 3. Add Transformers
    # Removed ColumnFilter to retain all columns in the processed dataset
    pipeline.add_transformer(MissingValueImputer("Department", "Unknown"))
    pipeline.add_transformer(TypeCaster("Salary", float))
    
    # 4. Run Workflow
    processed_data = pipeline.run()
    
    print(f"\nPipeline finished! Processed {len(processed_data)} rows.")
    print("First 2 rows of the processed data:")
    for row in processed_data[:2]:
        print(row)
