import pandas as pd


RSM_FILENAME = "test.xlsx"

# Assumptions 
# Sheets with relevant data to import are precisely the ones whose names are integers
# Assume columns and titles

def get_all_import_data():
    data = pd.read_excel(RSM_FILENAME, sheet_name=None, header=[0,1])
    sheet_names = list(data.keys())
    relevant_sheet_names = [i for i in sheet_names if i.isdigit()]
    relevant_data = {n: df for n, df in data if n in relevant_sheet_names}
    return relevant_data


def tidy_column_titles(df):
    df.columns = df.columns.to_flat_index()
    df.columns = ["_".join(col).strip() for col in df.columns.values]
    df.columns = [col.replace(" ", "_") for col in df.columns.values]
    df.columns = [col.lower() for col in df.columns.values]
    # TODO - assert number of columns
    # TODO - assert columns names
    return df


def get_all_import_data_df():
    data = get_all_import_data()
    all_dfs = list(data.values())
    transformed_dfs = [tidy_column_titles(df) for df in all_dfs]
    df = pd.concat(transformed_dfs)
    return df
    







