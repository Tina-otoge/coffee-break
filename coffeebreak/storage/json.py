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
            self.data = []

    def get(self, id):
        return self.data[id]

    def find(self, value):
        try:
            self.data.index(value)
        except ValueError:
            return None

    def insert(self, value):
        index = self.find(value)
        if index:
            return index
        self.data.append(value)
        return len(self.data) - 1

    def commit(self):
        with open(self.STORAGE_PATH, 'w') as f:
            json.dump(self.data, f)

