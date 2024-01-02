from project.base.repository import BaseRepository


class BaseService:
    repository: BaseRepository

    def get(self, *args, **kwargs):
        raise NotImplementedError()

    def update(self, *args, **kwargs):
        raise NotImplementedError()
