import json
import os
import uuid

from gitdatabase.cursor import Cursor


class Collection:
    def __init__(self, database, collection_name):
        self.database = database
        self.collection_name = collection_name

    def find(self, *args, **kwargs):
        return Cursor(self.database, self.collection_name, *args, **kwargs)

    def insert_one(self, item):
        _id = str(uuid.uuid4())
        local_collection = f'{self.database.working_dir}/{self.collection_name}.json'
        if os.path.exists(local_collection):
            with open(local_collection, 'r') as file:
                records = json.load(file)
                item.update({'_id': _id})
                records.append(item)
            with open(local_collection, 'w') as file:
                json.dump(records, file, indent=2, ensure_ascii=False)
            self.database.git.add(f'{self.collection_name}.json')
            self.database.index.commit(f'update {self.collection_name}')
            self.database.remote(name="origin").push()
            return _id
        else:
            raise FileNotFoundError('collection not exists')

