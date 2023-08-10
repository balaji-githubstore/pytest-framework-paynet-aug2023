from utilities import read_utils


class DataSource:
    test_valid_login_data = [
        ["physician", "physician", "English (Indian)", "OpenEMR"],
        ["accountant", "accountant", "English (Indian)", "OpenEMR"]
    ]

    test_invalid_data = [
        ["saul", "saul123", "German", "Invalid username or password"],
        ["kim", "kim123", "Dutch", "Invalid username or password"]
    ]

    test_valid_login_data_excel = read_utils.get_sheet_into_list("../test_data/open_emr_data.xlsx",
                                                                 "test_valid_login")

    test_valid_login_data_csv=read_utils.get_csv_into_list("../test_data/test_valid_login.csv")