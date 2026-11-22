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
                "last_ids" : {},
                "resident" : {}
            }

    def save(self):
        with open(self.file_path + ".tmp", 'w') as f:
            json.dump(self.data, f)
        os.replace(self.file_path + ".tmp", self.file_path)


    def insert(self, table, record):
        """Give the record a new ID, store it, save it, and return the ID."""
        # 1. new_id = ...            get an ID from next_id
        # 2. record[...] = new_id    key is the table name + "_id" (use an f-string)
        # 3. self.data[table][...] = record    key must be str(new_id)
        # 4. self.save()
        # 5. return new_id
        new_id = self.next_id(table)
        record[f"{table}_id"] = new_id
        self.data[table][str(new_id)] = record
        self.save()
        return new_id

    def next_id(self,table):
        """Return the next id for a table and increment the counter."""
        if table not in self.data["last_ids"]:
            self.data["last_ids"][table] = 1
        else:
            self.data["last_ids"][table] += 1
        return self.data["last_ids"][table] 

