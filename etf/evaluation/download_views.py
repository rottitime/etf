from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from etf.evaluation.models import Evaluation, EvaluationStatus
from etf.evaluation.schemas import EvaluationSchema


@login_required
def download_json_view(request):
    visible_qs = Evaluation.objects.exclude(status=EvaluationStatus.DRAFT)
    eval_schema = EvaluationSchema()
    # TODO - remove this once have figured out how to serialize multiple evals
    evaluations_qs = Evaluation.objects.all()
    x = evaluations_qs.first()
    print(x)
    data = eval_schema.dumps(x)
    headers = {
        "Content-Type": "application/json",
        "Content-Disposition": "attachment; filename='data.json'",
    }
    response = HttpResponse(data, headers=headers)
    return response


@login_required
def download_data_view(request):
    visible_qs = Evaluation.objects.exclude(status=EvaluationStatus.DRAFT)
    return render(request, "data-download.html", {})
