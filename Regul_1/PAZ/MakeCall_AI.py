#encoding:utf-8
from __future__ import print_function
CONTENT_var = """\
 repTime: INT;
"""
CONTENT_body = """\
repTime := 3600; // время ремонта аналоговых входов
//================ Инициализация настроек аналоговых входов(вызывается один раз при старте) ================
IF NOT PAZ_GVL.init THEN
//------------------------------- аргументы функции инициализации --------------------------------
// 1                                минимум шкалы канала, ед.изм. Не может быть >= max
// 2                                |   максимум шкалы канала, ед.изм. Не может быть <= min
// 3                                |   |   значение АЦП, соответствующее минимуму шкалы канала, б.р.
// 4                                |   |   |   значение АЦП, соотв. макс. шкалы, б.р. Не может быть равно minADC
// 5                                |   |   |   |     уровень зашкала вниз, ед.изм. Не может быть >= hiLim и < min
// 6                                |   |   |   |     |    уровень зашкала вверх, ед.изм. Не может быть <= loLim и > max
// 7                                |   |   |   |     |    |   уровень обрыва вниз, ед.изм. Не может быть >= loLim
// 8                                |   |   |   |     |    |    |   уровень обрыва вверх, ед.изм. Не может быть <= hiLim
// 9                                |   |   |   |     |    |    |   |  макс. допустимая скорость роста, ед.изм./сек. Если «0» - скорость роста не анализируется
//10                                |   |   |   |     |    |    |   |   |   время восстановления после неисправности, сек. Не может быть меньше "0"
//11                                |   |   |   |     |    |    |   |   |   |   максимальное время в ремонте, сек. Не может быть меньше или равно «0»
//12                                |   |   |   |     |    |    |   |   |   |   |    тау фильтра, сек. Если «0» - фильтрация отсутствует
//13                                |   |   |   |     |    |    |   |   |   |   |    |  номер по порядку	
//AI_init(UPG_AI_Settings.Pg_in_UPG,0.0,6.0,2.0,10.0,-0.5,6.5,-1.0,7.0,0.0,1.0,3600,1.0,0);
//-------------------------------------------------------------------------------------------
	// [A1.3:1]Давление газа на выходе из ГМК №44
	VGSig.fnAI_init(setStruct => PAZ_GVL.AI.Pg_outGMK_44.Settings, min_PV := 0.0, max_PV := 10.0, minADC := 4.0, maxADC := 20.0, loLim := -0.3, hiLim := 10.3, loBrk := -0.6, hiBrk := 10.6, maxROC := 0.0, recoveryTime := 5.0, repairTime := repTime, tau := 1.0, id := 1, corrADC := 0.0);
	// [A1.3:2]Давление газа на выходе из ГМК №45
	VGSig.fnAI_init(setStruct => PAZ_GVL.AI.Pg_outGMK_45.Settings, min_PV := 0.0, max_PV := 10.0, minADC := 4.0, maxADC := 20.0, loLim := -0.3, hiLim := 10.3, loBrk := -0.6, hiBrk := 10.6, maxROC := 0.0, recoveryTime := 5.0, repairTime := repTime, tau := 1.0, id := 1, corrADC := 0.0);
	// [A1.3:3]Давление газа на выходе из ГМК №46
	VGSig.fnAI_init(setStruct => PAZ_GVL.AI.Pg_outGMK_46.Settings, min_PV := 0.0, max_PV := 10.0, minADC := 4.0, maxADC := 20.0, loLim := -0.3, hiLim := 10.3, loBrk := -0.6, hiBrk := 10.6, maxROC := 0.0, recoveryTime := 5.0, repairTime := repTime, tau := 1.0, id := 1, corrADC := 0.0);
	// [A1.3:4]Давление газа на выходе из ГМК №47
	VGSig.fnAI_init(setStruct => PAZ_GVL.AI.Pg_outGMK_47.Settings, min_PV := 0.0, max_PV := 10.0, minADC := 4.0, maxADC := 20.0, loLim := -0.3, hiLim := 10.3, loBrk := -0.6, hiBrk := 10.6, maxROC := 0.0, recoveryTime := 5.0, repairTime := repTime, tau := 1.0, id := 1, corrADC := 0.0);
	// [A1.3:5]Давление газа на выходе из ГМК №48
	VGSig.fnAI_init(setStruct => PAZ_GVL.AI.Pg_outGMK_48.Settings, min_PV := 0.0, max_PV := 10.0, minADC := 4.0, maxADC := 20.0, loLim := -0.3, hiLim := 10.3, loBrk := -0.6, hiBrk := 10.6, maxROC := 0.0, recoveryTime := 5.0, repairTime := repTime, tau := 1.0, id := 1, corrADC := 0.0);
	// [A1.3:6]Давление газа на выходе из ГМК №51
	VGSig.fnAI_init(setStruct => PAZ_GVL.AI.Pg_outGMK_51.Settings, min_PV := 0.0, max_PV := 10.0, minADC := 4.0, maxADC := 20.0, loLim := -0.3, hiLim := 10.3, loBrk := -0.6, hiBrk := 10.6, maxROC := 0.0, recoveryTime := 5.0, repairTime := repTime, tau := 1.0, id := 1, corrADC := 0.0);
	// [A1.3:7]Давление газа на выходе из ГМК №52
	VGSig.fnAI_init(setStruct => PAZ_GVL.AI.Pg_outGMK_52.Settings, min_PV := 0.0, max_PV := 10.0, minADC := 4.0, maxADC := 20.0, loLim := -0.3, hiLim := 10.3, loBrk := -0.6, hiBrk := 10.6, maxROC := 0.0, recoveryTime := 5.0, repairTime := repTime, tau := 1.0, id := 1, corrADC := 0.0);
	// [A1.3:8]Давление масла на входе в двигатель ГМК №44
	VGSig.fnAI_init(setStruct => PAZ_GVL.AI.Pm_inD_GMK_44.Settings, min_PV := 0.0, max_PV := 0.4, minADC := 4.0, maxADC := 20.0, loLim := -0.012, hiLim := 0.41200000000000003, loBrk := -0.024, hiBrk := 0.42400000000000004, maxROC := 0.0, recoveryTime := 5.0, repairTime := repTime, tau := 1.0, id := 1, corrADC := 0.0);
	// [A1.3:1]Давление масла на входе в двигатель ГМК №45
	VGSig.fnAI_init(setStruct => PAZ_GVL.AI.Pm_inD_GMK_45.Settings, min_PV := 0.0, max_PV := 0.4, minADC := 4.0, maxADC := 20.0, loLim := -0.012, hiLim := 0.41200000000000003, loBrk := -0.024, hiBrk := 0.42400000000000004, maxROC := 0.0, recoveryTime := 5.0, repairTime := repTime, tau := 1.0, id := 1, corrADC := 0.0);
	// [A1.3:2]Давление масла на входе в двигатель ГМК №46
	VGSig.fnAI_init(setStruct => PAZ_GVL.AI.Pm_inD_GMK_46.Settings, min_PV := 0.0, max_PV := 0.4, minADC := 4.0, maxADC := 20.0, loLim := -0.012, hiLim := 0.41200000000000003, loBrk := -0.024, hiBrk := 0.42400000000000004, maxROC := 0.0, recoveryTime := 5.0, repairTime := repTime, tau := 1.0, id := 1, corrADC := 0.0);
	// [A1.3:3]Давление масла на входе в двигатель ГМК №47
	VGSig.fnAI_init(setStruct => PAZ_GVL.AI.Pm_inD_GMK_47.Settings, min_PV := 0.0, max_PV := 0.4, minADC := 4.0, maxADC := 20.0, loLim := -0.012, hiLim := 0.41200000000000003, loBrk := -0.024, hiBrk := 0.42400000000000004, maxROC := 0.0, recoveryTime := 5.0, repairTime := repTime, tau := 1.0, id := 1, corrADC := 0.0);
	// [A1.3:4]Давление масла на входе в двигатель ГМК №48
	VGSig.fnAI_init(setStruct => PAZ_GVL.AI.Pm_inD_GMK_48.Settings, min_PV := 0.0, max_PV := 0.4, minADC := 4.0, maxADC := 20.0, loLim := -0.012, hiLim := 0.41200000000000003, loBrk := -0.024, hiBrk := 0.42400000000000004, maxROC := 0.0, recoveryTime := 5.0, repairTime := repTime, tau := 1.0, id := 1, corrADC := 0.0);
	// [A1.3:5]Давление масла на входе в двигатель ГМК №51
	VGSig.fnAI_init(setStruct => PAZ_GVL.AI.Pm_inD_GMK_51.Settings, min_PV := 0.0, max_PV := 0.4, minADC := 4.0, maxADC := 20.0, loLim := -0.012, hiLim := 0.41200000000000003, loBrk := -0.024, hiBrk := 0.42400000000000004, maxROC := 0.0, recoveryTime := 5.0, repairTime := repTime, tau := 1.0, id := 1, corrADC := 0.0);
	// [A1.3:6]Давление масла на входе в двигатель ГМК №52
	VGSig.fnAI_init(setStruct => PAZ_GVL.AI.Pm_inD_GMK_52.Settings, min_PV := 0.0, max_PV := 0.4, minADC := 4.0, maxADC := 20.0, loLim := -0.012, hiLim := 0.41200000000000003, loBrk := -0.024, hiBrk := 0.42400000000000004, maxROC := 0.0, recoveryTime := 5.0, repairTime := repTime, tau := 1.0, id := 1, corrADC := 0.0);
	// [A1.3:7]Резерв
	VGSig.fnAI_init(setStruct => PAZ_GVL.AI.Reserv_0.Settings, min_PV := 4.0, max_PV := 20.0, minADC := 4.0, maxADC := 20.0, loLim := 3.52, hiLim := 20.48, loBrk := 3.04, hiBrk := 20.96, maxROC := 0.0, recoveryTime := 5.0, repairTime := repTime, tau := 1.0, id := 1, corrADC := 0.0);
	// [A1.3:8]Резерв
	VGSig.fnAI_init(setStruct => PAZ_GVL.AI.Reserv_1.Settings, min_PV := 4.0, max_PV := 20.0, minADC := 4.0, maxADC := 20.0, loLim := 3.52, hiLim := 20.48, loBrk := 3.04, hiBrk := 20.96, maxROC := 0.0, recoveryTime := 5.0, repairTime := repTime, tau := 1.0, id := 1, corrADC := 0.0);
	// [A1.5:1]Напряжение основного питания ~220 В
	VGSig.fnAI_init(setStruct => PAZ_GVL.AI.U_Osn_AC.Settings, min_PV := 0.0, max_PV := 370.0, minADC := 4.0, maxADC := 20.0, loLim := -11.1, hiLim := 381.1, loBrk := -22.2, hiBrk := 392.2, maxROC := 0.0, recoveryTime := 5.0, repairTime := repTime, tau := 1.0, id := 1, corrADC := 0.0);
	// [A1.5:2]Напряжение резервного питания ~220 В
	VGSig.fnAI_init(setStruct => PAZ_GVL.AI.U_Res_AC.Settings, min_PV := 0.0, max_PV := 370.0, minADC := 4.0, maxADC := 20.0, loLim := -11.1, hiLim := 381.1, loBrk := -22.2, hiBrk := 392.2, maxROC := 0.0, recoveryTime := 5.0, repairTime := repTime, tau := 1.0, id := 1, corrADC := 0.0);
END_IF;

//================ Обработчик аналоговых входов================
// [A1.3:1] Давление газа на выходе из ГМК №44
VGSig.fnAI_Processing(IN := PAZ_GVL.AI.Pg_outGMK_44.DRV, set := PAZ_GVL.AI.Pg_outGMK_44.Settings, btn := PAZ_GVL.AI.Pg_outGMK_44.FromHMI, out := PAZ_GVL.AI.Pg_outGMK_44.ToHMI, my := PAZ_GVL.AI.Pg_outGMK_44.Intern, nOk := PAZ_GVL.AI_FLT);
// [A1.3:2] Давление газа на выходе из ГМК №45
VGSig.fnAI_Processing(IN := PAZ_GVL.AI.Pg_outGMK_45.DRV, set := PAZ_GVL.AI.Pg_outGMK_45.Settings, btn := PAZ_GVL.AI.Pg_outGMK_45.FromHMI, out := PAZ_GVL.AI.Pg_outGMK_45.ToHMI, my := PAZ_GVL.AI.Pg_outGMK_45.Intern, nOk := PAZ_GVL.AI_FLT);
// [A1.3:3] Давление газа на выходе из ГМК №46
VGSig.fnAI_Processing(IN := PAZ_GVL.AI.Pg_outGMK_46.DRV, set := PAZ_GVL.AI.Pg_outGMK_46.Settings, btn := PAZ_GVL.AI.Pg_outGMK_46.FromHMI, out := PAZ_GVL.AI.Pg_outGMK_46.ToHMI, my := PAZ_GVL.AI.Pg_outGMK_46.Intern, nOk := PAZ_GVL.AI_FLT);
// [A1.3:4] Давление газа на выходе из ГМК №47
VGSig.fnAI_Processing(IN := PAZ_GVL.AI.Pg_outGMK_47.DRV, set := PAZ_GVL.AI.Pg_outGMK_47.Settings, btn := PAZ_GVL.AI.Pg_outGMK_47.FromHMI, out := PAZ_GVL.AI.Pg_outGMK_47.ToHMI, my := PAZ_GVL.AI.Pg_outGMK_47.Intern, nOk := PAZ_GVL.AI_FLT);
// [A1.3:5] Давление газа на выходе из ГМК №48
VGSig.fnAI_Processing(IN := PAZ_GVL.AI.Pg_outGMK_48.DRV, set := PAZ_GVL.AI.Pg_outGMK_48.Settings, btn := PAZ_GVL.AI.Pg_outGMK_48.FromHMI, out := PAZ_GVL.AI.Pg_outGMK_48.ToHMI, my := PAZ_GVL.AI.Pg_outGMK_48.Intern, nOk := PAZ_GVL.AI_FLT);
// [A1.3:6] Давление газа на выходе из ГМК №51
VGSig.fnAI_Processing(IN := PAZ_GVL.AI.Pg_outGMK_51.DRV, set := PAZ_GVL.AI.Pg_outGMK_51.Settings, btn := PAZ_GVL.AI.Pg_outGMK_51.FromHMI, out := PAZ_GVL.AI.Pg_outGMK_51.ToHMI, my := PAZ_GVL.AI.Pg_outGMK_51.Intern, nOk := PAZ_GVL.AI_FLT);
// [A1.3:7] Давление газа на выходе из ГМК №52
VGSig.fnAI_Processing(IN := PAZ_GVL.AI.Pg_outGMK_52.DRV, set := PAZ_GVL.AI.Pg_outGMK_52.Settings, btn := PAZ_GVL.AI.Pg_outGMK_52.FromHMI, out := PAZ_GVL.AI.Pg_outGMK_52.ToHMI, my := PAZ_GVL.AI.Pg_outGMK_52.Intern, nOk := PAZ_GVL.AI_FLT);
// [A1.3:8] Давление масла на входе в двигатель ГМК №44
VGSig.fnAI_Processing(IN := PAZ_GVL.AI.Pm_inD_GMK_44.DRV, set := PAZ_GVL.AI.Pm_inD_GMK_44.Settings, btn := PAZ_GVL.AI.Pm_inD_GMK_44.FromHMI, out := PAZ_GVL.AI.Pm_inD_GMK_44.ToHMI, my := PAZ_GVL.AI.Pm_inD_GMK_44.Intern, nOk := PAZ_GVL.AI_FLT);
// [A1.3:1] Давление масла на входе в двигатель ГМК №45
VGSig.fnAI_Processing(IN := PAZ_GVL.AI.Pm_inD_GMK_45.DRV, set := PAZ_GVL.AI.Pm_inD_GMK_45.Settings, btn := PAZ_GVL.AI.Pm_inD_GMK_45.FromHMI, out := PAZ_GVL.AI.Pm_inD_GMK_45.ToHMI, my := PAZ_GVL.AI.Pm_inD_GMK_45.Intern, nOk := PAZ_GVL.AI_FLT);
// [A1.3:2] Давление масла на входе в двигатель ГМК №46
VGSig.fnAI_Processing(IN := PAZ_GVL.AI.Pm_inD_GMK_46.DRV, set := PAZ_GVL.AI.Pm_inD_GMK_46.Settings, btn := PAZ_GVL.AI.Pm_inD_GMK_46.FromHMI, out := PAZ_GVL.AI.Pm_inD_GMK_46.ToHMI, my := PAZ_GVL.AI.Pm_inD_GMK_46.Intern, nOk := PAZ_GVL.AI_FLT);
// [A1.3:3] Давление масла на входе в двигатель ГМК №47
VGSig.fnAI_Processing(IN := PAZ_GVL.AI.Pm_inD_GMK_47.DRV, set := PAZ_GVL.AI.Pm_inD_GMK_47.Settings, btn := PAZ_GVL.AI.Pm_inD_GMK_47.FromHMI, out := PAZ_GVL.AI.Pm_inD_GMK_47.ToHMI, my := PAZ_GVL.AI.Pm_inD_GMK_47.Intern, nOk := PAZ_GVL.AI_FLT);
// [A1.3:4] Давление масла на входе в двигатель ГМК №48
VGSig.fnAI_Processing(IN := PAZ_GVL.AI.Pm_inD_GMK_48.DRV, set := PAZ_GVL.AI.Pm_inD_GMK_48.Settings, btn := PAZ_GVL.AI.Pm_inD_GMK_48.FromHMI, out := PAZ_GVL.AI.Pm_inD_GMK_48.ToHMI, my := PAZ_GVL.AI.Pm_inD_GMK_48.Intern, nOk := PAZ_GVL.AI_FLT);
// [A1.3:5] Давление масла на входе в двигатель ГМК №51
VGSig.fnAI_Processing(IN := PAZ_GVL.AI.Pm_inD_GMK_51.DRV, set := PAZ_GVL.AI.Pm_inD_GMK_51.Settings, btn := PAZ_GVL.AI.Pm_inD_GMK_51.FromHMI, out := PAZ_GVL.AI.Pm_inD_GMK_51.ToHMI, my := PAZ_GVL.AI.Pm_inD_GMK_51.Intern, nOk := PAZ_GVL.AI_FLT);
// [A1.3:6] Давление масла на входе в двигатель ГМК №52
VGSig.fnAI_Processing(IN := PAZ_GVL.AI.Pm_inD_GMK_52.DRV, set := PAZ_GVL.AI.Pm_inD_GMK_52.Settings, btn := PAZ_GVL.AI.Pm_inD_GMK_52.FromHMI, out := PAZ_GVL.AI.Pm_inD_GMK_52.ToHMI, my := PAZ_GVL.AI.Pm_inD_GMK_52.Intern, nOk := PAZ_GVL.AI_FLT);
// [A1.3:7] Резерв
VGSig.fnAI_Processing(IN := PAZ_GVL.AI.Reserv_0.DRV, set := PAZ_GVL.AI.Reserv_0.Settings, btn := PAZ_GVL.AI.Reserv_0.FromHMI, out := PAZ_GVL.AI.Reserv_0.ToHMI, my := PAZ_GVL.AI.Reserv_0.Intern, nOk := PAZ_GVL.AI_FLT);
// [A1.3:8] Резерв
VGSig.fnAI_Processing(IN := PAZ_GVL.AI.Reserv_1.DRV, set := PAZ_GVL.AI.Reserv_1.Settings, btn := PAZ_GVL.AI.Reserv_1.FromHMI, out := PAZ_GVL.AI.Reserv_1.ToHMI, my := PAZ_GVL.AI.Reserv_1.Intern, nOk := PAZ_GVL.AI_FLT);
// [A1.5:1] Напряжение основного питания ~220 В
VGSig.fnAI_Processing(IN := PAZ_GVL.AI.U_Osn_AC.DRV, set := PAZ_GVL.AI.U_Osn_AC.Settings, btn := PAZ_GVL.AI.U_Osn_AC.FromHMI, out := PAZ_GVL.AI.U_Osn_AC.ToHMI, my := PAZ_GVL.AI.U_Osn_AC.Intern, nOk := PAZ_GVL.AI_FLT);
// [A1.5:2] Напряжение резервного питания ~220 В
VGSig.fnAI_Processing(IN := PAZ_GVL.AI.U_Res_AC.DRV, set := PAZ_GVL.AI.U_Res_AC.Settings, btn := PAZ_GVL.AI.U_Res_AC.FromHMI, out := PAZ_GVL.AI.U_Res_AC.ToHMI, my := PAZ_GVL.AI.U_Res_AC.Intern, nOk := PAZ_GVL.AI_FLT);
"""
proj = projects.primary
folder = proj.find('AI PAZ', recursive=True)[0]
struktur = folder.create_pou('PAZ_AI_Call', type = PouType.Function,language=None, return_type='BOOL', base_type=None, interfaces=None)
struktur.textual_declaration.insert(4, 0, CONTENT_var)
struktur.textual_implementation.insert(0, 0, CONTENT_body)
