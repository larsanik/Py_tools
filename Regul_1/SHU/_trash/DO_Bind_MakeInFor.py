import IO_DO
j = 0
k = 11
for i in range(len(IO_DO.DO_Struct)):
	#algGVL.DGI.Kr1_OF.DRV := algGVL.A1_8_DW.0;
	out =   'algGVL.A1_' + str(k) + '_DW.' + str(j) + ' := algGVL.DGO.' + IO_DO.DO_Struct[i]['Name']  + '.DRV' + '; //' + IO_DO.DO_Struct[i]['Address'] + ' ' + IO_DO.DO_Struct[i]['Comment']
	j += 1
	if j > 31:
		j = 0
		k += 1
	print(out)