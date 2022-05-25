import pandas

excel_data_df = pandas.read_excel('IO.xls', sheet_name='AI1')
# print whole sheet data
print(excel_data_df.columns.ravel(1))