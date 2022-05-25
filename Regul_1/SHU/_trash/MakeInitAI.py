import IO_AI

for i in range(len(IO_AI.AI_Struct)):
	print('	// [' + IO_AI.AI_Struct[i]['Address'] + '] [' + IO_AI.AI_Struct[i]['AdrCh'] + '] ' + IO_AI.AI_Struct[i]['Comment'])
	min_PV_s = IO_AI.AI_Struct[i]['LL']
	max_PV_s = IO_AI.AI_Struct[i]['HL']
	min_PV_s = min_PV_s.replace(',','.')
	max_PV_s = max_PV_s.replace(',','.')
	f_min_PV = float(min_PV_s)
	f_max_PV = float(max_PV_s)
	min_PV = str(f_min_PV)
	max_PV = str(f_max_PV)
	minADC = '4.0'
	maxADC = '20.0'
	span = f_max_PV - f_min_PV
	loLim = str(f_min_PV - span * 0.03)
	hiLim = str(f_max_PV + span * 0.03)
	loBrk = str(f_min_PV - span * 0.06)
	hiBrk = str(f_max_PV + span * 0.06)
	Name = IO_AI.AI_Struct[i]['Name']

	out = '	VGSig.fnAI_init(setStruct => algGVL.AI.' + Name + '.Settings, min_PV := ' + min_PV +', max_PV := ' + max_PV + ', minADC := ' + minADC + ', maxADC := ' + maxADC + ', loLim := ' + loLim + ', hiLim := ' + hiLim + ', loBrk := ' + loBrk + ', hiBrk := ' + hiBrk + ', maxROC := 0.0, recoveryTime := 5.0, repairTime := repTime, tau := 1.0, id := 1, corrADC := 0.0);'

	print(out)


