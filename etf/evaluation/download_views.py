import csv

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from flatten_json import flatten

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

    data = eval_schema.dump(visible_qs, many=True)
    flattened_dict = [flatten(d) for d in data]
    # TODO - this doesn't get data in the format that we want it
    # Also need headers for rows

    headers = {
        "Content-Type": "text/csv",
        "Content-Disposition": "attachment; filename=data.csv",
    }
    response = HttpResponse(headers=headers)
    writer = csv.writer(response)
    for row in flattened_dict:
        writer.writerow(row)
    return response


@login_required
def download_page_view(request):
    visible_qs = Evaluation.objects.exclude(status=EvaluationStatus.DRAFT)
    return render(request, "data-download.html", {})
