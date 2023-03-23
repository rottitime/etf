import pandas as pd


RSM_FILENAME = "test.xlsx"

# Assumptions 
# Sheets with relevant data to import are precisely the ones whose names are integers

def get_all_data():
    data = pd.read_excel(RSM_FILENAME, sheet_name=None, header=[0,1])
    sheet_names = list(data.keys())
    relevant_sheet_names = [i for i in sheet_names if i.isdigit()]
    return relevant_sheet_names, data


def tidy_column_titles(df):
    df.columns = df.columns.to_flat_index()
    df.columns = ["_".join(col).strip() for col in df.columns.values]
    df.columns = [col.replace(" ", "_") for col in df.columns.values]
    df.columns = [col.lower() for col in df.columns.values]
    return df









