# """Will be deleted - not part of the framework"""
import pandas
#
# from utilities import read_utils
#
# df=pandas.read_excel(io="../test_data/open_emr_data.xlsx",sheet_name="test_valid_login")
# print(df)
#
# print(df.values.tolist())
#
#
# res=read_utils.get_sheet_into_list("../test_data/open_emr_data.xlsx","test_valid_login")
# print(res)

df=pandas.read_csv(filepath_or_buffer="../test_data/test_valid_login.csv",delimiter=";")
print(df)
print(df.values.tolist())