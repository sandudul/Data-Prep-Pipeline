from data_processor.readers import ExcelReader
import pprint

if __name__ == "__main__":
    print("Reading dataset/Datasets.xlsx...")
    reader = ExcelReader('dataset/Datasets.xlsx')
    data = reader.read()
    
    print(f"\nTotal rows read: {len(data)}")
    print("\nFirst 5 rows:")
    pprint.pprint(data[:5], sort_dicts=False)
