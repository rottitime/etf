from etf.evaluation.schemas import EvaluationSchema
from etf.evaluation.models import Evaluation, EvaluationStatus
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse


def download_json(evaluations_qs):
    eval_schema = EvaluationSchema()
    # TODO - remove this once have figured out how to serialize evals
    x = evaluations_qs.first()
    data = eval_schema.dumps(x)
    return data


@login_required
def download_data_view(request):
    visible_qs = Evaluation.objects.exclude(status=EvaluationStatus.DRAFT)
    data = download_json(visible_qs)
    content_type = "application/force-download"
    response = HttpResponse(data, content_type)
    return response
