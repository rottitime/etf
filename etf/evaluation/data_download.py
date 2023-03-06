from schemas import EvaluationSchema
from models import Evaluation


def download_json(evaluations_qs):
    eval_schema = EvaluationSchema()
    data = eval_schema.dump(evaluations_qs)
    return data
