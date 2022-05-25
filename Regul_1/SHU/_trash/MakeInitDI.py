import IO_DI

for i in range(len(IO_DI.DI_Struct)):
	print('	// [' + IO_DI.DI_Struct[i]['Address'] + '] [' + IO_DI.DI_Struct[i]['AdrCh'] + '] ' + IO_DI.DI_Struct[i]['Comment'])
	Name = IO_DI.DI_Struct[i]['Name']
	out = '	VGSig.fnDI_init(setStruct => algGVL.DGI.' + Name + '.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := ' + str(i+1) + ');'
	print(out)


