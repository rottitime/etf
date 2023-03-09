import csv

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from etf.evaluation.models import Evaluation
from etf.evaluation.schemas import EvaluationSchema


def filter_evaluations_to_download(request):
    output_evaluations_qs = Evaluation.objects.none()
    if "civil_service_only" in request.GET:
        civil_service_evals = Evaluation.objects.filter(status="CIVIL_SERVICE")
        output_evaluations_qs = output_evaluations_qs | civil_service_evals
    if "public" in request.GET:
        public_evals = Evaluation.objects.filter(status="PUBLIC")
        output_evaluations_qs = output_evaluations_qs | public_evals
    if "my_evaluations" in request.GET:
        user = request.user
        user_evals = user.evaluations.all()
        output_evaluations_qs = output_evaluations_qs | user_evals
    return output_evaluations_qs


def download_json_view(request):
    evaluations_qs = filter_evaluations_to_download(request)
    evaluation_schema = EvaluationSchema()
    data = evaluation_schema.dumps(evaluations_qs, many=True)
    headers = {
        "Content-Type": "application/json",
        "Content-Disposition": "attachment; filename=evaluation-data.json",
    }
    response = HttpResponse(data, headers=headers)
    return response


def download_csv_view(request):
    evaluations_qs = filter_evaluations_to_download(request)
    evaluation_schema = EvaluationSchema()
    data = evaluation_schema.dump(evaluations_qs, many=True)
    headers = {
        "Content-Type": "text/csv",
        "Content-Disposition": "attachment; filename=evaluation-data.csv",
    }
    response = HttpResponse(headers=headers)
    # TODO - do we want only selected fields, and in what order?
    fieldnames = []
    if data:
        fieldnames = list(data[0].keys())
    writer = csv.DictWriter(response, fieldnames=fieldnames)
    writer.writeheader()
    for row in data:
        writer.writerow(row)
    return response


@login_required
def download_page_view(request):
    if "json" in request.GET:
        return download_json_view(request)
    elif "csv" in request.GET:
        return download_csv_view(request)
    return render(request, "data-download.html", {"errors": {}, "data": {}})
