import os
import shutil

from git import Repo

from gitdatabase.collection import Collection


class Client:
    def __init__(self, repo, username, password, **kwargs):
        branch = kwargs.pop('branch', 'main')
        local_path = f'{os.path.dirname(os.path.dirname(__file__))}/{username}-database'
        shutil.rmtree(local_path, ignore_errors=True)
        remote = f'https://{username}:{password}@{repo}'
        Repo.clone_from(remote, local_path, branch=kwargs.pop('branch', 'main'))
        self.database = Repo(local_path)

    def __getattr__(self, collection_name):
        return Collection(self.database, collection_name)

