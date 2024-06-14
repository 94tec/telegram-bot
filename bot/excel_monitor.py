import os
import pandas as pd

class ExcelMonitor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.last_modified = None
        self.last_data = None
        self.load_file()

    def load_file(self):
        if os.path.exists(self.file_path):
            self.last_modified = os.path.getmtime(self.file_path)
            self.last_data = pd.read_excel(self.file_path, engine='openpyxl')
        else:
            raise FileNotFoundError(f"No such file: {self.file_path}")

    def check_for_changes(self):
        if os.path.getmtime(self.file_path) > self.last_modified:
            new_data = pd.read_excel(self.file_path, engine='openpyxl')
            added_data = new_data[~new_data.isin(self.last_data)].dropna(how='all')
            modified_data = new_data[new_data.isin(self.last_data) & (new_data != self.last_data).any(axis=1)]
            self.last_data = new_data
            self.last_modified = os.path.getmtime(self.file_path)
            return added_data, modified_data
        return None, None
