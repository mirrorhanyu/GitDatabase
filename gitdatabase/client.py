import os
import shutil

from git import Repo

from gitdatabase.collection import Collection
from random import random


class Client:
    def __init__(self, repo, access_token, **kwargs):
        branch = kwargs.pop('branch', 'main')
        local_path = f'{os.path.dirname(os.path.dirname(__file__))}/database-{random()}'
        shutil.rmtree(local_path, ignore_errors=True)
        remote = f'https://{access_token}:x-oauth-basic@{repo}'
        Repo.clone_from(remote, local_path, branch=kwargs.pop('branch', 'main'))
        self.database = Repo(local_path)

    def __getattr__(self, collection_name):
        return Collection(self.database, collection_name)

