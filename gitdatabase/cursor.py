import json
import os
from collections import deque


class Cursor(object):
    def __init__(self, database, collection, filter_condition=None):
        self.database = database
        self.collection = collection
        self.filter_condition = filter_condition
        self.items = deque(self._query_item())

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.items):
            return self.items.popleft()
        raise StopIteration

    def _query_item(self):
        local_collection = f'{self.database.working_dir}/{self.collection}.json'
        if os.path.exists(local_collection):
            with open(local_collection, 'r') as data:
                records = json.load(data)
                if bool(self.filter_condition):
                    return [record for record in records for filter_name, filter_value in self.filter_condition.items() if record.get(filter_name) == filter_value]
                else:
                    return records
        else:
            raise FileNotFoundError('collection not exists')




