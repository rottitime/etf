import pathlib
import math

import pandas as pd

from etf.evaluation import models


# Assumptions
# Sheets with relevant data to import are precisely the ones whose names are integers
# Assume columns and titles are always the same




RSM_FILENAME = "test.xlsx"
__here__ = pathlib.Path(__file__).parent
DATA_DIR = __here__ / "data"
FULL_PATH = DATA_DIR / RSM_FILENAME

INFO_NOT_IDENTIFIED = "Information not identified within the report"


# MANY OF THESE:
# - Evaluation costs and budget
# - Documents
# - Event dates
# - Intervention
# - Outcome measure
# - Other measure
# - Processes and standards


def get_all_import_data():
    data = pd.read_excel(FULL_PATH, sheet_name=None, header=[0, 1])
    sheet_names = list(data.keys())
    relevant_sheet_names = [i for i in sheet_names if i.isdigit()]
    relevant_data = {n: df for n, df in data.items() if n in relevant_sheet_names}
    return relevant_data


def tidy_column_titles(df):
    df.columns = df.columns.to_flat_index()
    df.columns = ["_".join(col).strip() for col in df.columns.values]
    df.columns = [col.replace("/", " ") for col in df.columns.values]
    df.columns = [col.replace("  ", " ") for col in df.columns.values]
    df.columns = [col.replace(" ", "_") for col in df.columns.values]
    df.columns = [col.lower() for col in df.columns.values]
    assert len(df.columns) == 142
    return df


def get_all_import_data_df():
    data = get_all_import_data()
    all_dfs = list(data.values())
    transformed_dfs = [tidy_column_titles(df) for df in all_dfs]
    df = pd.concat(transformed_dfs)
    df = df.replace(INFO_NOT_IDENTIFIED, math.nan)
    evaluation_ids = df["metadata_evaluation_id"].unique()
    evaluation_ids = [id for id in evaluation_ids if not math.isnan(id)]
    return evaluation_ids, df


def get_data_for_field(data_for_eval, fieldname_in_rsm):
    """Standard field in evaluation ie one field, may need to aggregate data,
    though in most cases there will only be one value."""
    all_non_null_data = data_for_eval[data_for_eval[fieldname_in_rsm].notnull()][fieldname_in_rsm]
    string_summary = all_non_null_data.to_string(index=False)
    return string_summary


def get_evaluation_types(data_for_eval):
    evaluation_types = []
    # if "Y" in data_for_eval[""]
    # if 
    # Check for any Y in columns for process/impact/economic
    # If there is not a N in other evaluation type - add that value
    
    return evaluation_types


def import_data_for_id(all_df, evaluation_id):
    eval_df = all_df[all_df["metadata_evaluation_id"] == evaluation_id]
    title_field = "evaluation_information_evaluation_title"
    title = eval_df[eval_df[title_field].notnull()][title_field].iloc[0]
    evaluation = models.Evaluation(title=title)
    
    