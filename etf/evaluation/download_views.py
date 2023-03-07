import csv

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from flatten_json import flatten
from django.shortcuts import redirect, render
from django.urls import reverse

from etf.evaluation.models import Evaluation, EvaluationStatus
from etf.evaluation.schemas import EvaluationSchema


@login_required
def download_json_view(request):
    print(request.GET.get("my_evaluations"))
    print(request.POST.dict())
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
def download_data_view(request, include_my_evals, include_cs_only, include_public, type):
    visible_statuses_to_include = []
    if include_cs_only:
        visible_statuses_to_include.append(EvaluationStatus.CIVIL_SERVICE)
    elif include_public:
        visible_statuses_to_include.append(EvaluationStatus.PUBLIC)
    if include_my_evals:
        user = request.user


@login_required
def download_page_view(request):
    # TODO - errors, data?
    type = None
    if "json" in request.GET:
        type = "json"
    elif "csv" in request.GET:
        type = "csv"

    if not type:
        return render(request, "data-download.html", {"errors": {}, "data": {}})

    include_my_evals = False
    include_cs = False
    include_public = False
    if "my_evaluations" in request.GET:
        include_my_evals = True
    if "civil_service_only" in request.GET:
        include_cs = True
    if "public" in request.GET:
        include_public = True
    return download_data_view(request, include_my_evals, include_cs, include_public, type)
