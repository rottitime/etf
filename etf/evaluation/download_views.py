from schemas import EvaluationSchema
from models import Evaluation, EvaluationStatus
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def download_json(evaluations_qs):
    eval_schema = EvaluationSchema()
    data = eval_schema.dump(evaluations_qs)
    return data


@login_required
def download_data_view(request):
    visible_qs = Evaluation.objects.exclude(status=EvaluationStatus.DRAFT)
    data = download_json(visible_qs)
    return render(request, "templates/data-download.html", data)
