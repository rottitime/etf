from django.core.management.base import BaseCommand

from etf.evaluation.management import utils


class Command(BaseCommand):
    help = "Populate Evaluation Registry with data from RSM"

    def add_arguments(self, parser):
        parser.add_argument("-f", "--filename", type=str, default="test.xlsx", help="Filename of data to upload")

    def handle(self, *args, **kwargs):
        filename = kwargs["filename"]
        utils.upload_all_data(filename)
