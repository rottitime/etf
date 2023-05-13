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


class UpdateEvaluationVisibilitySchema(marshmallow.Schema):
    user_id = marshmallow.fields.UUID()
    evaluation_id = marshmallow.fields.UUID()
    page_name = marshmallow.fields.Str()
    status = marshmallow.fields.Str()


class UpdateEvaluationUsersSchema(marshmallow.Schema):
    evaluation_id = marshmallow.fields.UUID()
    user_data = marshmallow.fields.Nested(schemas.UserSchema)


class UpdatedEvaluationUsersSchema(marshmallow.Schema):
    evaluation_id = marshmallow.fields.UUID()
    user_id = marshmallow.fields.UUID()
    user_created = marshmallow.fields.Boolean()


class RemoveEvaluationUserSchema(marshmallow.Schema):
    evaluation_id = marshmallow.fields.UUID()
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

    @with_schema(load=GetEvaluationSchema, dump=schemas.EvaluationSchema)
    def get(self, user_id, evaluation_id):
        evaluation = models.Evaluation.objects.get(id=evaluation_id, users__id=user_id)
        return evaluation

    @with_schema(load=UpdateEvaluationSchema(partial=True), dump=schemas.EvaluationSchema)
    @register_event("Evaluation updated")
    def update(self, user_id, evaluation_id, data):
        evaluation = models.Evaluation.objects.get(id=evaluation_id, users__id=user_id)
        for key, value in data.items():
            setattr(evaluation, key, value)
        evaluation.save()
        return evaluation

    @with_schema(load=UpdateEvaluationVisibilitySchema, dump=schemas.EvaluationSchema)
    def update_page_status(self, user_id, evaluation_id, page_name, status):
        evaluation = models.Evaluation.objects.get(id=evaluation_id, users__id=user_id)
        evaluation.update_evaluation_page_status(page_name, status)
        evaluation.save()
        return evaluation

    @with_schema(load=UpdateEvaluationUsersSchema, dump=UpdatedEvaluationUsersSchema)
    @register_event("User added to evaluation")
    def add_user_to_evaluation(self, evaluation_id, user_data):
        evaluation = models.Evaluation.objects.get(id=evaluation_id)
        user, user_created = models.User.objects.update_or_create(email=user_data["email"], defaults=user_data)
        evaluation.users.add(user)
        output = {"evaluation_id": evaluation_id, "user_id": user.id, "user_created": user_created}
        return output

    @with_schema(load=RemoveEvaluationUserSchema, dump=schemas.UserSchema)
    @register_event("User removed from evaluation")
    def remove_user_from_evaluation(self, evaluation_id, user_id):
        evaluation = models.Evaluation.objects.get(id=evaluation_id)
        user = models.User.objects.get(id=user_id)
        evaluation.users.remove(user)
        return evaluation.users.all()


facade = Facade(evaluation=Evaluation())
