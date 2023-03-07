from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from etf.evaluation.models import Evaluation, EvaluationStatus
from etf.evaluation.schemas import EvaluationSchema


@login_required
def download_json_view(request):
    visible_qs = Evaluation.objects.exclude(status=EvaluationStatus.DRAFT)
    eval_schema = EvaluationSchema()
    data = eval_schema.dumps(visible_qs, many=True)
    headers = {
        "Content-Type": "application/json",
        "Content-Disposition": "attachment; filename=data.json",
    }
    response = HttpResponse(data, headers=headers)
    return response


@login_required
def download_csv_view(request):
    visible_qs = Evaluation.objects.exclude(status=EvaluationStatus.DRAFT)
    eval_schema = EvaluationSchema()
    data = eval_schema.dumps(visible_qs, many=True)
    headers = {
        "Content-Type": "text/csv",
        "Content-Disposition": "attachment; filename=data.csv",
    }
    response = HttpResponse(data, headers=headers)
    return response


# @login_required
# def download_data_view(request, type, headers, include_civil_service=False):
#     assert type in ["json"]  # TODO - add other types
#     visible_qs = Evaluation.objects.exclude(status=EvaluationStatus.DRAFT)
#     if not include_civil_service:
#         visible_qs = visible_qs.filter(status=EvaluationStatus.PUBLIC)


@login_required
def download_page_view(request):
    visible_qs = Evaluation.objects.exclude(status=EvaluationStatus.DRAFT)
    return render(request, "data-download.html", {})
