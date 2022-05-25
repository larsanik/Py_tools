import IO_DI
j = 0
k = 8
for i in range(len(IO_DI.DI_Struct)):
	#algGVL.DGI.Kr1_OF.DRV := algGVL.A1_8_DW.0;
	out = 'algGVL.DGI.' + IO_DI.DI_Struct[i]['Name']  + '.DRV := algGVL.A1_' + str(k) + '_DW.' + str(j) + ';'  + ' //' + IO_DI.DI_Struct[i]['Address'] + ' ' + IO_DI.DI_Struct[i]['Comment']
	j += 1
	if j > 31:
		j = 0
		k += 1
	print(out)