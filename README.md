# Data Processor

A modular, reusable, and document data processing package in Python. 
Built using Object-Oriented principles, this package provides abstract base classes for building robust data pipelines.

## Features

- **Readers**: Load data from various sources (CSV, JSON, Excel).
- **Transformers**: Clean and modify data in standard forms.
- **Writers**: Output processed data to desired formats.
- **Workflows**: Run sequence of readers, transformers, and writers with a simple pipeline interface.

## Installation

```bash
pip install -e .[dev]
```

## Running Tests

```bash
pytest tests/
```
