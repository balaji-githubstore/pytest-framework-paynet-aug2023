import pandas


def get_sheet_into_list(file, sheet_name):
    df = pandas.read_excel(io=file, sheet_name=sheet_name)
    return df.values.tolist()


def get_csv_into_list(file):
    df = pandas.read_csv(filepath_or_buffer=file, delimiter=";")
    return df.values.tolist()
