import IO_DO

for i in range(len(IO_DO.DO_Struct)):
	caption = '// [' + IO_DO.DO_Struct[i]['Address'] + '] [' + IO_DO.DO_Struct[i]['AdrCh'] + '] ' + IO_DO.DO_Struct[i]['Comment']
	print(caption)
	Name = IO_DO.DO_Struct[i]['Name']
	out = 'VGSig.fnDO_Processing(algOut := algGVL.DGO.' + Name + '.PV, fromHMI := algGVL.DGO.' + Name + '.FromHMI, toHMI := algGVL.DGO.' + Name + '.ToHMI, drv => algGVL.DGO.' + Name + '.DRV);'
	print(out)


