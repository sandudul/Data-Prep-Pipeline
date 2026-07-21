from abc import ABC, abstractmethod
from typing import Any, Dict, List

# Define our basic data structure: A list of dictionaries
DataType = List[Dict[str, Any]]

class DataReader(ABC):
    """Abstract base class for reading data."""
    
    @abstractmethod
    def read(self) -> DataType:
        """Reads data from a source and returns a list of dictionaries."""
        pass


class DataTransformer(ABC):
    """Abstract base class for transforming data."""
    
    @abstractmethod
    def transform(self, data: DataType) -> DataType:
        """Applies a transformation to the data and returns the modified data."""
        pass


class DataWriter(ABC):
    """Abstract base class for writing data."""
    
    @abstractmethod
    def write(self, data: DataType) -> None:
        """Writes the data to a destination."""
        pass
