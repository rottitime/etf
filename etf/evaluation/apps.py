from django.apps import AppConfig


class EvaluationConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "etf.evaluation"

    def ready(self):
        # noinspection PyUnresolvedReferences
        import etf.evaluation.authentication_views
