import IO_AI
import IO_DI
import IO_DO

f_w = open('StructContent.py','w', encoding='UTF8')
f_w.write('#encoding:utf-8')
f_w.write('STRUCT_CONTENT_AI = """\\' + '\n')

for i in range(len(IO_AI.AI_Struct)):
	out = '	' + IO_AI.AI_Struct[i]['Name']  + ':str_AI;' + ' //' + IO_AI.AI_Struct[i]['Comment'] +  '\n'
	f_w.write(out)
f_w.write('"""' + '\n')

f_w.write('STRUCT_CONTENT_DI = """\\' + '\n')

for i in range(len(IO_DI.DI_Struct)):
	out = '	' + IO_DI.DI_Struct[i]['Name']  + ':str_DI;'  + ' //' + IO_DI.DI_Struct[i]['Comment']+ '\n'
	f_w.write(out)
f_w.write('"""' + '\n')

f_w.write('STRUCT_CONTENT_DO = """\\' + '\n')

for i in range(len(IO_DO.DO_Struct)):
	out = '	' + IO_DO.DO_Struct[i]['Name']  + ':str_DO;' + ' //' + IO_DO.DO_Struct[i]['Comment'] + '\n'
	f_w.write(out)
f_w.write('"""')

f_w.close
