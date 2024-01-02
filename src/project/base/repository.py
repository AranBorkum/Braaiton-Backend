from django.db.models import Model, QuerySet


class BaseRepository:
    object_model: Model

    def get_object(self, **kwargs) -> Model:
        return self.object_model.objects.get(**kwargs)

    def get_objects(self, **kwargs) -> QuerySet:
        return self.object_model.objects.filter(**kwargs)

    def create_object(self, **kwargs) -> Model:
        return self.object_model.objects.create(**kwargs)

    @staticmethod
    def update_object(obj, **kwargs):
        for key, value in kwargs.items():
            setattr(obj, key, value)

        obj.save()
