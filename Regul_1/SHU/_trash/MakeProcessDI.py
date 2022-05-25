import IO_DI

for i in range(len(IO_DI.DI_Struct)):
	print('// [' + IO_DI.DI_Struct[i]['Address'] + '] [' + IO_DI.DI_Struct[i]['AdrCh'] + '] ' + IO_DI.DI_Struct[i]['Comment'])
	Name = IO_DI.DI_Struct[i]['Name']
	out = 'VGSig.fnDI_Processing(IN := algGVL.DGI.' + Name + '.DRV, externalFault := FALSE, set := algGVL.DGI.' + Name + '.Settings, FromHMI := algGVL.DGI.' + Name + '.FromHMI, ToHMI := algGVL.DGI.' + Name + '.ToHMI, my := algGVL.DGI.' + Name + '.Intern, out := algGVL.DGI.' + Name + '.PV);'
	print(out)


