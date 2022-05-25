import config #файл с настройками
import xlrd #модуль для работы с excel

rb = xlrd.open_workbook(config.srcData, formatting_info=True)#открываем файл
sheets = rb.sheet_names() #получаем наименования всех лимтов книги
print(sheets)#печатаем наименования всех лимтов книги
selectedSheet = input()#запрос имени листа с которым работаем
try:
    indexSheet=sheets.index(selectedSheet)#получаем индекс выбранного листа
    print(indexSheet) #control
except:
    print('Not find sheet ', selectedSheet )

sheet = rb.sheet_by_index(indexSheet)
#val = sheet.row_values(3)[5]
#print(val)
rows = []
for i in range(sheet.nrows):
    columns = []
    for j in range(sheet.ncols):
        columns.append(sheet.cell(i, j).value)
    rows.append(columns)
print(rows)
