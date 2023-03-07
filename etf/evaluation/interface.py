import marshmallow

from . import models, schemas
from .utils import Entity, Facade, register_event, with_schema


class CreateEvaluationSchema(marshmallow.Schema):
    user_id = marshmallow.fields.UUID()


class GetEvaluationSchema(marshmallow.Schema):
    user_id = marshmallow.fields.UUID()
    evaluation_id = marshmallow.fields.UUID()


class UpdateEvaluationSchema(marshmallow.Schema):
    user_id = marshmallow.fields.UUID()
    evaluation_id = marshmallow.fields.UUID()
    data = marshmallow.fields.Nested(schemas.EvaluationSchema)


class UpdateEvaluationStatusSchema(marshmallow.Schema):
    user_id = marshmallow.fields.UUID()
    evaluation_id = marshmallow.fields.UUID()
    page_name = marshmallow.fields.Str()
    status = marshmallow.fields.Str()


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

    @with_schema(load=GetEvaluationSchema, dump=schemas.EvaluationSchema)
    def get(self, user_id, evaluation_id):
        evaluation = models.Evaluation.objects.get(id=evaluation_id, users__id=user_id)
        return evaluation

    @with_schema(load=UpdateEvaluationSchema, dump=schemas.EvaluationSchema)
    @register_event("Evaluation updated")
    def update(self, user_id, evaluation_id, data):
        evaluation = models.Evaluation.objects.get(id=evaluation_id, users__id=user_id)
        for key, value in data.items():
            setattr(evaluation, key, value)
        evaluation.save()
        return evaluation

    @with_schema(load=UpdateEvaluationStatusSchema, dump=schemas.EvaluationSchema)
    def update_page_status(self, user_id, evaluation_id, page_name, status):
        evaluation = models.Evaluation.objects.get(id=evaluation_id, users__id=user_id)
        evaluation.update_evaluation_page_status(page_name, status)
        evaluation.save()
        return evaluation


facade = Facade(evaluation=Evaluation())
