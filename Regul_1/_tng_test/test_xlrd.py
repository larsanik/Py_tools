#import config
import xlrd
rb = xlrd.open_workbook('IO.xls')
sheets = rb.sheet_names()
#sheet = rb.sheet_names('AI1')#sheet_by_index(0)
#val = sheet.row_values(3)[5]
#print(val)
print(sheets)
sheet = rb.sheet_by_index(sheets.index('AI1'))
print(range(sheet.nrows))
#rows = []
for i in range(sheet.nrows):
    if i > 2:
        val = sheet.cell(i, 5).value
        if val == '':
            print('Empty')
        else:
            print(val)
    #columns = []
    #for j in range(sheet.ncols):
    #    columns.append(sheet.cell(i, j).value)
    #rows.append(columns)
#print(rows)
