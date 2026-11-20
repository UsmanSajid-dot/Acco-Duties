import json
import os

class JsonStore:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = self.load()

    def load(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as f:
                return json.load(f)
        else:
            return {
                "schema_version" : 1,
                "next_ids" : {},
                "resident" : {}
            }

    def save(self):
        with open(self.file_path + ".tmp", 'w') as f:
            json.dump(self.data, f)
        os.replace(self.file_path + ".tmp", self.file_path)
        