from typing import Any

from services.mock_source import MockLogSource
from services.file_source import FileLogSource
from services.csv_source import CsvLogSource


class SourceFactory:
    @staticmethod
    def create_source(kind: str, **kwargs) -> Any:
        """Create a log source by kind. Supported: 'mock', 'file', 'csv'.

        For 'file', pass `filepath` in kwargs.
        For 'csv', pass `filepath` in kwargs.
        """
        if kind == "mock":
            return MockLogSource()
        if kind == "file":
            path = kwargs.get("filepath", "logs/sample.log")
            return FileLogSource(path)
        if kind == "csv":
            path = kwargs.get("filepath", "logs/voters.csv")
            return CsvLogSource(path)

        raise ValueError(f"Unknown source kind: {kind}")
