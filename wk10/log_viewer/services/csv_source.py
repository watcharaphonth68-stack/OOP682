import csv
from interfaces.data_source import ILogSource


class CsvLogSource(ILogSource):
    """CSV Log Source - reads CSV files and formats them as logs."""
    
    def __init__(self, file_path: str):
        self.file_path = file_path
    
    def get_logs(self) -> list[str]:
        """Read CSV file and return formatted rows including headers."""
        logs = []
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                csv_reader = csv.reader(file)
                for row in csv_reader:
                    logs.append(' | '.join(row))
        except FileNotFoundError:
            logs.append(f"Error: File not found: {self.file_path}")
        except Exception as e:
            logs.append(f"Error reading CSV: {str(e)}")
        
        return logs
