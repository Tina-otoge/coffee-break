import json

from . import Storage

class JSONStorage(Storage):
    STORAGE_PATH = 'storage.json'

    def __init__(self):
        try:
            with open(self.STORAGE_PATH) as f:
                self.data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            print('Could not open storage file ({})'.format(self.STORAGE_PATH))
            self.data = {}
        try:
            self.index = list(sorted(self.data.keys()))[-1]
        except IndexError:
            self.index = 0

    def get(self, id):
        return json.loads(self.data[str(id)])

    def find(self, value):
        results = [k for k, v in self.data.items() if value == v]
        if len(results) > 0:
            return results[0]
        return None

    def insert(self, value):
        index = self.find(value)
        if index:
            return index
        self.data[++self.index] = value
        return self.index

    def commit(self):
        with open(self.STORAGE_PATH, 'w') as f:
            json.dump(self.data, f)

