import marshmallow

from . import models, schemas
from .utils import Entity, Facade, register_event, with_schema


class CreateEvaluationSchema(marshmallow.Schema):
    user_id = marshmallow.fields.UUID()


class Evaluation(Entity):
    @with_schema(load=CreateEvaluationSchema, dump=schemas.EvaluationSchema)
    @register_event("Evaluation created")
    def create(self, user_id):
        user = models.User.objects.get(id=user_id)
        evaluation = models.Evaluation()
        evaluation.save()
        evaluation.users.add(user)
        evaluation.save()
        return evaluation


facade = Facade(evaluation=Evaluation())
