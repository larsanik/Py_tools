#encoding:utf-8
from __future__ import print_function
CONTENT_var = """\
 repTime: INT;
"""
CONTENT_body = """\
repTime := 3600; // время ремонта аналоговых входов
//================ Инициализация настроек аналоговых входов(вызывается один раз при старте) ================
IF NOT SHU_GVL.init THEN
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
	// [A1.4:1]Температура силового цилиндра 1
	VGSig.fnAI_init(setStruct => SHU_GVL.AI.Tsc_1.Settings, min_PV := 0.0, max_PV := 600.0, minADC := 4.0, maxADC := 20.0, loLim := -18.0, hiLim := 618.0, loBrk := -36.0, hiBrk := 636.0, maxROC := 0.0, recoveryTime := 5.0, repairTime := repTime, tau := 1.0, id := 1, corrADC := 0.0);
	// [A1.4:2]Температура силового цилиндра 2
	VGSig.fnAI_init(setStruct => SHU_GVL.AI.Tsc_2.Settings, min_PV := 0.0, max_PV := 600.0, minADC := 4.0, maxADC := 20.0, loLim := -18.0, hiLim := 618.0, loBrk := -36.0, hiBrk := 636.0, maxROC := 0.0, recoveryTime := 5.0, repairTime := repTime, tau := 1.0, id := 1, corrADC := 0.0);
	// [A1.4:3]Температура силового цилиндра 3
	VGSig.fnAI_init(setStruct => SHU_GVL.AI.Tsc_3.Settings, min_PV := 0.0, max_PV := 600.0, minADC := 4.0, maxADC := 20.0, loLim := -18.0, hiLim := 618.0, loBrk := -36.0, hiBrk := 636.0, maxROC := 0.0, recoveryTime := 5.0, repairTime := repTime, tau := 1.0, id := 1, corrADC := 0.0);
	// [A1.4:4]Температура силового цилиндра 4
	VGSig.fnAI_init(setStruct => SHU_GVL.AI.Tsc_4.Settings, min_PV := 0.0, max_PV := 600.0, minADC := 4.0, maxADC := 20.0, loLim := -18.0, hiLim := 618.0, loBrk := -36.0, hiBrk := 636.0, maxROC := 0.0, recoveryTime := 5.0, repairTime := repTime, tau := 1.0, id := 1, corrADC := 0.0);
	// [A1.4:5]Температура силового цилиндра 5
	VGSig.fnAI_init(setStruct => SHU_GVL.AI.Tsc_5.Settings, min_PV := 0.0, max_PV := 600.0, minADC := 4.0, maxADC := 20.0, loLim := -18.0, hiLim := 618.0, loBrk := -36.0, hiBrk := 636.0, maxROC := 0.0, recoveryTime := 5.0, repairTime := repTime, tau := 1.0, id := 1, corrADC := 0.0);
	// [A1.4:6]Температура силового цилиндра 6
	VGSig.fnAI_init(setStruct => SHU_GVL.AI.Tsc_6.Settings, min_PV := 0.0, max_PV := 600.0, minADC := 4.0, maxADC := 20.0, loLim := -18.0, hiLim := 618.0, loBrk := -36.0, hiBrk := 636.0, maxROC := 0.0, recoveryTime := 5.0, repairTime := repTime, tau := 1.0, id := 1, corrADC := 0.0);
	// [A1.4:7]Температура силового цилиндра 7
	VGSig.fnAI_init(setStruct => SHU_GVL.AI.Tsc_7.Settings, min_PV := 0.0, max_PV := 600.0, minADC := 4.0, maxADC := 20.0, loLim := -18.0, hiLim := 618.0, loBrk := -36.0, hiBrk := 636.0, maxROC := 0.0, recoveryTime := 5.0, repairTime := repTime, tau := 1.0, id := 1, corrADC := 0.0);
	// [A1.4:8]Температура силового цилиндра 8
	VGSig.fnAI_init(setStruct => SHU_GVL.AI.Tsc_8.Settings, min_PV := 0.0, max_PV := 600.0, minADC := 4.0, maxADC := 20.0, loLim := -18.0, hiLim := 618.0, loBrk := -36.0, hiBrk := 636.0, maxROC := 0.0, recoveryTime := 5.0, repairTime := repTime, tau := 1.0, id := 1, corrADC := 0.0);
	// [A1.4:9]Температура силового цилиндра 9
	VGSig.fnAI_init(setStruct => SHU_GVL.AI.Tsc_9.Settings, min_PV := 0.0, max_PV := 600.0, minADC := 4.0, maxADC := 20.0, loLim := -18.0, hiLim := 618.0, loBrk := -36.0, hiBrk := 636.0, maxROC := 0.0, recoveryTime := 5.0, repairTime := repTime, tau := 1.0, id := 1, corrADC := 0.0);
	// [A1.4:10]Температура силового цилиндра 10
	VGSig.fnAI_init(setStruct => SHU_GVL.AI.Tsc_10.Settings, min_PV := 0.0, max_PV := 600.0, minADC := 4.0, maxADC := 20.0, loLim := -18.0, hiLim := 618.0, loBrk := -36.0, hiBrk := 636.0, maxROC := 0.0, recoveryTime := 5.0, repairTime := repTime, tau := 1.0, id := 1, corrADC := 0.0);
	// [A1.4:11]Температура выхлопных газов в левом коллекторе
	VGSig.fnAI_init(setStruct => SHU_GVL.AI.Tvg_lk.Settings, min_PV := 0.0, max_PV := 600.0, minADC := 4.0, maxADC := 20.0, loLim := -18.0, hiLim := 618.0, loBrk := -36.0, hiBrk := 636.0, maxROC := 0.0, recoveryTime := 5.0, repairTime := repTime, tau := 1.0, id := 1, corrADC := 0.0);
	// [A1.4:12]Температура выхлопных газов в правом коллекторе
	VGSig.fnAI_init(setStruct => SHU_GVL.AI.Tvg_pk.Settings, min_PV := 0.0, max_PV := 600.0, minADC := 4.0, maxADC := 20.0, loLim := -18.0, hiLim := 618.0, loBrk := -36.0, hiBrk := 636.0, maxROC := 0.0, recoveryTime := 5.0, repairTime := repTime, tau := 1.0, id := 1, corrADC := 0.0);
	// [A1.4:13]Резерв
	VGSig.fnAI_init(setStruct => SHU_GVL.AI.Reserv_0.Settings, min_PV := 4.0, max_PV := 20.0, minADC := 4.0, maxADC := 20.0, loLim := 3.52, hiLim := 20.48, loBrk := 3.04, hiBrk := 20.96, maxROC := 0.0, recoveryTime := 5.0, repairTime := repTime, tau := 1.0, id := 1, corrADC := 0.0);
	// [A1.4:14]Резерв
	VGSig.fnAI_init(setStruct => SHU_GVL.AI.Reserv_1.Settings, min_PV := 4.0, max_PV := 20.0, minADC := 4.0, maxADC := 20.0, loLim := 3.52, hiLim := 20.48, loBrk := 3.04, hiBrk := 20.96, maxROC := 0.0, recoveryTime := 5.0, repairTime := repTime, tau := 1.0, id := 1, corrADC := 0.0);
	// [A1.4:15]Резерв
	VGSig.fnAI_init(setStruct => SHU_GVL.AI.Reserv_2.Settings, min_PV := 4.0, max_PV := 20.0, minADC := 4.0, maxADC := 20.0, loLim := 3.52, hiLim := 20.48, loBrk := 3.04, hiBrk := 20.96, maxROC := 0.0, recoveryTime := 5.0, repairTime := repTime, tau := 1.0, id := 1, corrADC := 0.0);
	// [A1.4:16]Резерв
	VGSig.fnAI_init(setStruct => SHU_GVL.AI.Reserv_3.Settings, min_PV := 4.0, max_PV := 20.0, minADC := 4.0, maxADC := 20.0, loLim := 3.52, hiLim := 20.48, loBrk := 3.04, hiBrk := 20.96, maxROC := 0.0, recoveryTime := 5.0, repairTime := repTime, tau := 1.0, id := 1, corrADC := 0.0);
	// [A1.5:1]Температура коренного подшипника № 1
	VGSig.fnAI_init(setStruct => SHU_GVL.AI.Tkp_1.Settings, min_PV := 0.0, max_PV := 150.0, minADC := 4.0, maxADC := 20.0, loLim := -4.5, hiLim := 154.5, loBrk := -9.0, hiBrk := 159.0, maxROC := 0.0, recoveryTime := 5.0, repairTime := repTime, tau := 1.0, id := 1, corrADC := 0.0);
	// [A1.5:2]Температура коренного подшипника № 2
	VGSig.fnAI_init(setStruct => SHU_GVL.AI.Tkp_2.Settings, min_PV := 0.0, max_PV := 150.0, minADC := 4.0, maxADC := 20.0, loLim := -4.5, hiLim := 154.5, loBrk := -9.0, hiBrk := 159.0, maxROC := 0.0, recoveryTime := 5.0, repairTime := repTime, tau := 1.0, id := 1, corrADC := 0.0);
	// [A1.5:3]Температура коренного подшипника № 3
	VGSig.fnAI_init(setStruct => SHU_GVL.AI.Tkp_3.Settings, min_PV := 0.0, max_PV := 150.0, minADC := 4.0, maxADC := 20.0, loLim := -4.5, hiLim := 154.5, loBrk := -9.0, hiBrk := 159.0, maxROC := 0.0, recoveryTime := 5.0, repairTime := repTime, tau := 1.0, id := 1, corrADC := 0.0);
	// [A1.5:4]Температура коренного подшипника № 4
	VGSig.fnAI_init(setStruct => SHU_GVL.AI.Tkp_4.Settings, min_PV := 0.0, max_PV := 150.0, minADC := 4.0, maxADC := 20.0, loLim := -4.5, hiLim := 154.5, loBrk := -9.0, hiBrk := 159.0, maxROC := 0.0, recoveryTime := 5.0, repairTime := repTime, tau := 1.0, id := 1, corrADC := 0.0);
	// [A1.5:5]Температура коренного подшипника № 5
	VGSig.fnAI_init(setStruct => SHU_GVL.AI.Tkp_5.Settings, min_PV := 0.0, max_PV := 150.0, minADC := 4.0, maxADC := 20.0, loLim := -4.5, hiLim := 154.5, loBrk := -9.0, hiBrk := 159.0, maxROC := 0.0, recoveryTime := 5.0, repairTime := repTime, tau := 1.0, id := 1, corrADC := 0.0);
	// [A1.5:6]Температура коренного подшипника № 6
	VGSig.fnAI_init(setStruct => SHU_GVL.AI.Tkp_6.Settings, min_PV := 0.0, max_PV := 150.0, minADC := 4.0, maxADC := 20.0, loLim := -4.5, hiLim := 154.5, loBrk := -9.0, hiBrk := 159.0, maxROC := 0.0, recoveryTime := 5.0, repairTime := repTime, tau := 1.0, id := 1, corrADC := 0.0);
	// [A1.5:7]Температура коренного подшипника № 7
	VGSig.fnAI_init(setStruct => SHU_GVL.AI.Tkp_7.Settings, min_PV := 0.0, max_PV := 150.0, minADC := 4.0, maxADC := 20.0, loLim := -4.5, hiLim := 154.5, loBrk := -9.0, hiBrk := 159.0, maxROC := 0.0, recoveryTime := 5.0, repairTime := repTime, tau := 1.0, id := 1, corrADC := 0.0);
	// [A1.5:8]Температура коренного подшипника № 8
	VGSig.fnAI_init(setStruct => SHU_GVL.AI.Tkp_8.Settings, min_PV := 0.0, max_PV := 150.0, minADC := 4.0, maxADC := 20.0, loLim := -4.5, hiLim := 154.5, loBrk := -9.0, hiBrk := 159.0, maxROC := 0.0, recoveryTime := 5.0, repairTime := repTime, tau := 1.0, id := 1, corrADC := 0.0);
	// [A1.5:9]Температура коренного подшипника № 9
	VGSig.fnAI_init(setStruct => SHU_GVL.AI.Tkp_9.Settings, min_PV := 0.0, max_PV := 150.0, minADC := 4.0, maxADC := 20.0, loLim := -4.5, hiLim := 154.5, loBrk := -9.0, hiBrk := 159.0, maxROC := 0.0, recoveryTime := 5.0, repairTime := repTime, tau := 1.0, id := 1, corrADC := 0.0);
	// [A1.5:10]Температура коренного подшипника № 10
	VGSig.fnAI_init(setStruct => SHU_GVL.AI.Tkp_10.Settings, min_PV := 0.0, max_PV := 150.0, minADC := 4.0, maxADC := 20.0, loLim := -4.5, hiLim := 154.5, loBrk := -9.0, hiBrk := 159.0, maxROC := 0.0, recoveryTime := 5.0, repairTime := repTime, tau := 1.0, id := 1, corrADC := 0.0);
	// [A1.5:11]Температура воды на входе в двигатель
	VGSig.fnAI_init(setStruct => SHU_GVL.AI.Tv_inD.Settings, min_PV := 0.0, max_PV := 100.0, minADC := 4.0, maxADC := 20.0, loLim := -3.0, hiLim := 103.0, loBrk := -6.0, hiBrk := 106.0, maxROC := 0.0, recoveryTime := 5.0, repairTime := repTime, tau := 1.0, id := 1, corrADC := 0.0);
	// [A1.5:12]Температура воды на выходе из двигателя
	VGSig.fnAI_init(setStruct => SHU_GVL.AI.Tv_outD.Settings, min_PV := 0.0, max_PV := 100.0, minADC := 4.0, maxADC := 20.0, loLim := -3.0, hiLim := 103.0, loBrk := -6.0, hiBrk := 106.0, maxROC := 0.0, recoveryTime := 5.0, repairTime := repTime, tau := 1.0, id := 1, corrADC := 0.0);
	// [A1.5:13]Температура воздуха наддува
	VGSig.fnAI_init(setStruct => SHU_GVL.AI.Tvn.Settings, min_PV := 0.0, max_PV := 100.0, minADC := 4.0, maxADC := 20.0, loLim := -3.0, hiLim := 103.0, loBrk := -6.0, hiBrk := 106.0, maxROC := 0.0, recoveryTime := 5.0, repairTime := repTime, tau := 1.0, id := 1, corrADC := 0.0);
	// [A1.5:14]Температура масла на входе в ГМК
	VGSig.fnAI_init(setStruct => SHU_GVL.AI.Tm_inGMK.Settings, min_PV := 0.0, max_PV := 100.0, minADC := 4.0, maxADC := 20.0, loLim := -3.0, hiLim := 103.0, loBrk := -6.0, hiBrk := 106.0, maxROC := 0.0, recoveryTime := 5.0, repairTime := repTime, tau := 1.0, id := 1, corrADC := 0.0);
	// [A1.5:15]Температура масла на выходе из ГМК
	VGSig.fnAI_init(setStruct => SHU_GVL.AI.Tm_outGMK.Settings, min_PV := 0.0, max_PV := 100.0, minADC := 4.0, maxADC := 20.0, loLim := -3.0, hiLim := 103.0, loBrk := -6.0, hiBrk := 106.0, maxROC := 0.0, recoveryTime := 5.0, repairTime := repTime, tau := 1.0, id := 1, corrADC := 0.0);
	// [A1.5:16]Резерв
	VGSig.fnAI_init(setStruct => SHU_GVL.AI.Reserv_4.Settings, min_PV := 4.0, max_PV := 20.0, minADC := 4.0, maxADC := 20.0, loLim := 3.52, hiLim := 20.48, loBrk := 3.04, hiBrk := 20.96, maxROC := 0.0, recoveryTime := 5.0, repairTime := repTime, tau := 1.0, id := 1, corrADC := 0.0);
	// [A1.6:1]Температура газа на выходе компрессорного цилиндра 1
	VGSig.fnAI_init(setStruct => SHU_GVL.AI.Tg_outKC_1.Settings, min_PV := 0.0, max_PV := 150.0, minADC := 4.0, maxADC := 20.0, loLim := -4.5, hiLim := 154.5, loBrk := -9.0, hiBrk := 159.0, maxROC := 0.0, recoveryTime := 5.0, repairTime := repTime, tau := 1.0, id := 1, corrADC := 0.0);
	// [A1.6:2]Температура газа на выходе компрессорного цилиндра 2
	VGSig.fnAI_init(setStruct => SHU_GVL.AI.Tg_outKC_2.Settings, min_PV := 0.0, max_PV := 150.0, minADC := 4.0, maxADC := 20.0, loLim := -4.5, hiLim := 154.5, loBrk := -9.0, hiBrk := 159.0, maxROC := 0.0, recoveryTime := 5.0, repairTime := repTime, tau := 1.0, id := 1, corrADC := 0.0);
	// [A1.6:3]Температура газа на выходе компрессорного цилиндра 3
	VGSig.fnAI_init(setStruct => SHU_GVL.AI.Tg_outKC_3.Settings, min_PV := 0.0, max_PV := 150.0, minADC := 4.0, maxADC := 20.0, loLim := -4.5, hiLim := 154.5, loBrk := -9.0, hiBrk := 159.0, maxROC := 0.0, recoveryTime := 5.0, repairTime := repTime, tau := 1.0, id := 1, corrADC := 0.0);
	// [A1.6:4]Температура газа на выходе компрессорного цилиндра 4
	VGSig.fnAI_init(setStruct => SHU_GVL.AI.Tg_outKC_4.Settings, min_PV := 0.0, max_PV := 150.0, minADC := 4.0, maxADC := 20.0, loLim := -4.5, hiLim := 154.5, loBrk := -9.0, hiBrk := 159.0, maxROC := 0.0, recoveryTime := 5.0, repairTime := repTime, tau := 1.0, id := 1, corrADC := 0.0);
	// [A1.6:5]Температура газа на выходе компрессорного цилиндра 5
	VGSig.fnAI_init(setStruct => SHU_GVL.AI.Tg_outKC_5.Settings, min_PV := 0.0, max_PV := 150.0, minADC := 4.0, maxADC := 20.0, loLim := -4.5, hiLim := 154.5, loBrk := -9.0, hiBrk := 159.0, maxROC := 0.0, recoveryTime := 5.0, repairTime := repTime, tau := 1.0, id := 1, corrADC := 0.0);
	// [A1.6:6]Резерв
	VGSig.fnAI_init(setStruct => SHU_GVL.AI.Reserv_5.Settings, min_PV := 4.0, max_PV := 20.0, minADC := 4.0, maxADC := 20.0, loLim := 3.52, hiLim := 20.48, loBrk := 3.04, hiBrk := 20.96, maxROC := 0.0, recoveryTime := 5.0, repairTime := repTime, tau := 1.0, id := 1, corrADC := 0.0);
	// [A1.6:7]Резерв
	VGSig.fnAI_init(setStruct => SHU_GVL.AI.Reserv_6.Settings, min_PV := 4.0, max_PV := 20.0, minADC := 4.0, maxADC := 20.0, loLim := 3.52, hiLim := 20.48, loBrk := 3.04, hiBrk := 20.96, maxROC := 0.0, recoveryTime := 5.0, repairTime := repTime, tau := 1.0, id := 1, corrADC := 0.0);
	// [A1.6:8]Резерв
	VGSig.fnAI_init(setStruct => SHU_GVL.AI.Reserv_7.Settings, min_PV := 4.0, max_PV := 20.0, minADC := 4.0, maxADC := 20.0, loLim := 3.52, hiLim := 20.48, loBrk := 3.04, hiBrk := 20.96, maxROC := 0.0, recoveryTime := 5.0, repairTime := repTime, tau := 1.0, id := 1, corrADC := 0.0);
	// [A1.6:9]Резерв
	VGSig.fnAI_init(setStruct => SHU_GVL.AI.Reserv_8.Settings, min_PV := 4.0, max_PV := 20.0, minADC := 4.0, maxADC := 20.0, loLim := 3.52, hiLim := 20.48, loBrk := 3.04, hiBrk := 20.96, maxROC := 0.0, recoveryTime := 5.0, repairTime := repTime, tau := 1.0, id := 1, corrADC := 0.0);
	// [A1.6:10]Резерв
	VGSig.fnAI_init(setStruct => SHU_GVL.AI.Reserv_9.Settings, min_PV := 4.0, max_PV := 20.0, minADC := 4.0, maxADC := 20.0, loLim := 3.52, hiLim := 20.48, loBrk := 3.04, hiBrk := 20.96, maxROC := 0.0, recoveryTime := 5.0, repairTime := repTime, tau := 1.0, id := 1, corrADC := 0.0);
	// [A1.6:14]Управление запорно-регулирующим клапаном на приёме ГМК PV4601.1. КЦУ
	VGSig.fnAI_init(setStruct => SHU_GVL.AI.RegKr1_KCU.Settings, min_PV := 4.0, max_PV := 20.0, minADC := 4.0, maxADC := 20.0, loLim := 3.52, hiLim := 20.48, loBrk := 3.04, hiBrk := 20.96, maxROC := 0.0, recoveryTime := 5.0, repairTime := repTime, tau := 1.0, id := 1, corrADC := 0.0);
	// [A1.6:15]Напряжение основного питания ~220 В
	VGSig.fnAI_init(setStruct => SHU_GVL.AI.U_Osn_AC.Settings, min_PV := 0.0, max_PV := 370.0, minADC := 4.0, maxADC := 20.0, loLim := -11.1, hiLim := 381.1, loBrk := -22.2, hiBrk := 392.2, maxROC := 0.0, recoveryTime := 5.0, repairTime := repTime, tau := 1.0, id := 1, corrADC := 0.0);
	// [A1.6:16]Напряжение резервного питания ~220 В
	VGSig.fnAI_init(setStruct => SHU_GVL.AI.U_Res_AC.Settings, min_PV := 0.0, max_PV := 370.0, minADC := 4.0, maxADC := 20.0, loLim := -11.1, hiLim := 381.1, loBrk := -22.2, hiBrk := 392.2, maxROC := 0.0, recoveryTime := 5.0, repairTime := repTime, tau := 1.0, id := 1, corrADC := 0.0);
	// [A1.7:1]Давление газа на входе в ГМК
	VGSig.fnAI_init(setStruct => SHU_GVL.AI.Pg_inGMK.Settings, min_PV := 0.0, max_PV := 2.5, minADC := 4.0, maxADC := 20.0, loLim := -0.075, hiLim := 2.575, loBrk := -0.15, hiBrk := 2.65, maxROC := 0.0, recoveryTime := 5.0, repairTime := repTime, tau := 1.0, id := 1, corrADC := 0.0);
	// [A1.7:2]Давление газа на выходе из ГМК
	VGSig.fnAI_init(setStruct => SHU_GVL.AI.Pg_outGMK.Settings, min_PV := 0.0, max_PV := 10.0, minADC := 4.0, maxADC := 20.0, loLim := -0.3, hiLim := 10.3, loBrk := -0.6, hiBrk := 10.6, maxROC := 0.0, recoveryTime := 5.0, repairTime := repTime, tau := 1.0, id := 1, corrADC := 0.0);
	// [A1.7:3]Давление пускового воздуха
	VGSig.fnAI_init(setStruct => SHU_GVL.AI.Ppv.Settings, min_PV := 0.0, max_PV := 2.5, minADC := 4.0, maxADC := 20.0, loLim := -0.075, hiLim := 2.575, loBrk := -0.15, hiBrk := 2.65, maxROC := 0.0, recoveryTime := 5.0, repairTime := repTime, tau := 1.0, id := 1, corrADC := 0.0);
	// [A1.7:4]Давление топливного газа до ТРК
	VGSig.fnAI_init(setStruct => SHU_GVL.AI.Ptg_inTRK.Settings, min_PV := 0.0, max_PV := 0.6, minADC := 4.0, maxADC := 20.0, loLim := -0.018, hiLim := 0.618, loBrk := -0.036, hiBrk := 0.636, maxROC := 0.0, recoveryTime := 5.0, repairTime := repTime, tau := 1.0, id := 1, corrADC := 0.0);
	// [A1.7:5]Давление топливного газа после ТРК
	VGSig.fnAI_init(setStruct => SHU_GVL.AI.Ptg_outTRK.Settings, min_PV := 0.0, max_PV := 0.6, minADC := 4.0, maxADC := 20.0, loLim := -0.018, hiLim := 0.618, loBrk := -0.036, hiBrk := 0.636, maxROC := 0.0, recoveryTime := 5.0, repairTime := repTime, tau := 1.0, id := 1, corrADC := 0.0);
	// [A1.7:6]Давление воздуха наддува
	VGSig.fnAI_init(setStruct => SHU_GVL.AI.Pvn.Settings, min_PV := 0.0, max_PV := 2.5, minADC := 4.0, maxADC := 20.0, loLim := -0.075, hiLim := 2.575, loBrk := -0.15, hiBrk := 2.65, maxROC := 0.0, recoveryTime := 5.0, repairTime := repTime, tau := 1.0, id := 1, corrADC := 0.0);
	// [A1.7:7]Давление масла на входе в турбокомпрессоры
	VGSig.fnAI_init(setStruct => SHU_GVL.AI.Pm_inTK.Settings, min_PV := 0.0, max_PV := 0.6, minADC := 4.0, maxADC := 20.0, loLim := -0.018, hiLim := 0.618, loBrk := -0.036, hiBrk := 0.636, maxROC := 0.0, recoveryTime := 5.0, repairTime := repTime, tau := 1.0, id := 1, corrADC := 0.0);
	// [A1.7:8]Давление масла на входе в двигатель
	VGSig.fnAI_init(setStruct => SHU_GVL.AI.Pm_inD.Settings, min_PV := 0.0, max_PV := 0.4, minADC := 4.0, maxADC := 20.0, loLim := -0.012, hiLim := 0.41200000000000003, loBrk := -0.024, hiBrk := 0.42400000000000004, maxROC := 0.0, recoveryTime := 5.0, repairTime := repTime, tau := 1.0, id := 1, corrADC := 0.0);
	// [A1.7:9]Перепад давления масла на фильтре
	VGSig.fnAI_init(setStruct => SHU_GVL.AI.dPmf.Settings, min_PV := 0.0, max_PV := 0.25, minADC := 4.0, maxADC := 20.0, loLim := -0.0075, hiLim := 0.2575, loBrk := -0.015, hiBrk := 0.265, maxROC := 0.0, recoveryTime := 5.0, repairTime := repTime, tau := 1.0, id := 1, corrADC := 0.0);
	// [A1.7:10]Давление воды на выходе из двигателя
	VGSig.fnAI_init(setStruct => SHU_GVL.AI.Pv_outD.Settings, min_PV := 0.0, max_PV := 0.4, minADC := 4.0, maxADC := 20.0, loLim := -0.012, hiLim := 0.41200000000000003, loBrk := -0.024, hiBrk := 0.42400000000000004, maxROC := 0.0, recoveryTime := 5.0, repairTime := repTime, tau := 1.0, id := 1, corrADC := 0.0);
	// [A1.7:11]Положение ТРК PV9604.1
	VGSig.fnAI_init(setStruct => SHU_GVL.AI.Pos_TRK.Settings, min_PV := 0.0, max_PV := 100.0, minADC := 4.0, maxADC := 20.0, loLim := -3.0, hiLim := 103.0, loBrk := -6.0, hiBrk := 106.0, maxROC := 0.0, recoveryTime := 5.0, repairTime := repTime, tau := 1.0, id := 1, corrADC := 0.0);
	// [A1.7:12]Положение запорно-регулирующего клапана на приёме ГМК PV4601.1
	VGSig.fnAI_init(setStruct => SHU_GVL.AI.Pos_RegKr1.Settings, min_PV := 0.0, max_PV := 100.0, minADC := 4.0, maxADC := 20.0, loLim := -3.0, hiLim := 103.0, loBrk := -6.0, hiBrk := 106.0, maxROC := 0.0, recoveryTime := 5.0, repairTime := repTime, tau := 1.0, id := 1, corrADC := 0.0);
	// [A1.7:13]Уровень вибрации ГМК (виброскорость), канал 1
	VGSig.fnAI_init(setStruct => SHU_GVL.AI.Vb_Ch_1.Settings, min_PV := 0.0, max_PV := 40.0, minADC := 4.0, maxADC := 20.0, loLim := -1.2, hiLim := 41.2, loBrk := -2.4, hiBrk := 42.4, maxROC := 0.0, recoveryTime := 5.0, repairTime := repTime, tau := 1.0, id := 1, corrADC := 0.0);
	// [A1.7:14]Уровень вибрации ГМК (виброскорость), канал 2
	VGSig.fnAI_init(setStruct => SHU_GVL.AI.Vb_Ch_2.Settings, min_PV := 0.0, max_PV := 40.0, minADC := 4.0, maxADC := 20.0, loLim := -1.2, hiLim := 41.2, loBrk := -2.4, hiBrk := 42.4, maxROC := 0.0, recoveryTime := 5.0, repairTime := repTime, tau := 1.0, id := 1, corrADC := 0.0);
	// [A1.7:15]Резерв
	VGSig.fnAI_init(setStruct => SHU_GVL.AI.Reserv_10.Settings, min_PV := 4.0, max_PV := 20.0, minADC := 4.0, maxADC := 20.0, loLim := 3.52, hiLim := 20.48, loBrk := 3.04, hiBrk := 20.96, maxROC := 0.0, recoveryTime := 5.0, repairTime := repTime, tau := 1.0, id := 1, corrADC := 0.0);
	// [A1.7:16]Резерв
	VGSig.fnAI_init(setStruct => SHU_GVL.AI.Reserv_11.Settings, min_PV := 4.0, max_PV := 20.0, minADC := 4.0, maxADC := 20.0, loLim := 3.52, hiLim := 20.48, loBrk := 3.04, hiBrk := 20.96, maxROC := 0.0, recoveryTime := 5.0, repairTime := repTime, tau := 1.0, id := 1, corrADC := 0.0);
END_IF;

//================ Обработчик аналоговых входов================
// [A1.4:1] Температура силового цилиндра 1
VGSig.fnAI_Processing(IN := SHU_GVL.AI.Tsc_1.DRV, set := SHU_GVL.AI.Tsc_1.Settings, btn := SHU_GVL.AI.Tsc_1.FromHMI, out := SHU_GVL.AI.Tsc_1.ToHMI, my := SHU_GVL.AI.Tsc_1.Intern, nOk := SHU_GVL.AI_FLT);
// [A1.4:2] Температура силового цилиндра 2
VGSig.fnAI_Processing(IN := SHU_GVL.AI.Tsc_2.DRV, set := SHU_GVL.AI.Tsc_2.Settings, btn := SHU_GVL.AI.Tsc_2.FromHMI, out := SHU_GVL.AI.Tsc_2.ToHMI, my := SHU_GVL.AI.Tsc_2.Intern, nOk := SHU_GVL.AI_FLT);
// [A1.4:3] Температура силового цилиндра 3
VGSig.fnAI_Processing(IN := SHU_GVL.AI.Tsc_3.DRV, set := SHU_GVL.AI.Tsc_3.Settings, btn := SHU_GVL.AI.Tsc_3.FromHMI, out := SHU_GVL.AI.Tsc_3.ToHMI, my := SHU_GVL.AI.Tsc_3.Intern, nOk := SHU_GVL.AI_FLT);
// [A1.4:4] Температура силового цилиндра 4
VGSig.fnAI_Processing(IN := SHU_GVL.AI.Tsc_4.DRV, set := SHU_GVL.AI.Tsc_4.Settings, btn := SHU_GVL.AI.Tsc_4.FromHMI, out := SHU_GVL.AI.Tsc_4.ToHMI, my := SHU_GVL.AI.Tsc_4.Intern, nOk := SHU_GVL.AI_FLT);
// [A1.4:5] Температура силового цилиндра 5
VGSig.fnAI_Processing(IN := SHU_GVL.AI.Tsc_5.DRV, set := SHU_GVL.AI.Tsc_5.Settings, btn := SHU_GVL.AI.Tsc_5.FromHMI, out := SHU_GVL.AI.Tsc_5.ToHMI, my := SHU_GVL.AI.Tsc_5.Intern, nOk := SHU_GVL.AI_FLT);
// [A1.4:6] Температура силового цилиндра 6
VGSig.fnAI_Processing(IN := SHU_GVL.AI.Tsc_6.DRV, set := SHU_GVL.AI.Tsc_6.Settings, btn := SHU_GVL.AI.Tsc_6.FromHMI, out := SHU_GVL.AI.Tsc_6.ToHMI, my := SHU_GVL.AI.Tsc_6.Intern, nOk := SHU_GVL.AI_FLT);
// [A1.4:7] Температура силового цилиндра 7
VGSig.fnAI_Processing(IN := SHU_GVL.AI.Tsc_7.DRV, set := SHU_GVL.AI.Tsc_7.Settings, btn := SHU_GVL.AI.Tsc_7.FromHMI, out := SHU_GVL.AI.Tsc_7.ToHMI, my := SHU_GVL.AI.Tsc_7.Intern, nOk := SHU_GVL.AI_FLT);
// [A1.4:8] Температура силового цилиндра 8
VGSig.fnAI_Processing(IN := SHU_GVL.AI.Tsc_8.DRV, set := SHU_GVL.AI.Tsc_8.Settings, btn := SHU_GVL.AI.Tsc_8.FromHMI, out := SHU_GVL.AI.Tsc_8.ToHMI, my := SHU_GVL.AI.Tsc_8.Intern, nOk := SHU_GVL.AI_FLT);
// [A1.4:9] Температура силового цилиндра 9
VGSig.fnAI_Processing(IN := SHU_GVL.AI.Tsc_9.DRV, set := SHU_GVL.AI.Tsc_9.Settings, btn := SHU_GVL.AI.Tsc_9.FromHMI, out := SHU_GVL.AI.Tsc_9.ToHMI, my := SHU_GVL.AI.Tsc_9.Intern, nOk := SHU_GVL.AI_FLT);
// [A1.4:10] Температура силового цилиндра 10
VGSig.fnAI_Processing(IN := SHU_GVL.AI.Tsc_10.DRV, set := SHU_GVL.AI.Tsc_10.Settings, btn := SHU_GVL.AI.Tsc_10.FromHMI, out := SHU_GVL.AI.Tsc_10.ToHMI, my := SHU_GVL.AI.Tsc_10.Intern, nOk := SHU_GVL.AI_FLT);
// [A1.4:11] Температура выхлопных газов в левом коллекторе
VGSig.fnAI_Processing(IN := SHU_GVL.AI.Tvg_lk.DRV, set := SHU_GVL.AI.Tvg_lk.Settings, btn := SHU_GVL.AI.Tvg_lk.FromHMI, out := SHU_GVL.AI.Tvg_lk.ToHMI, my := SHU_GVL.AI.Tvg_lk.Intern, nOk := SHU_GVL.AI_FLT);
// [A1.4:12] Температура выхлопных газов в правом коллекторе
VGSig.fnAI_Processing(IN := SHU_GVL.AI.Tvg_pk.DRV, set := SHU_GVL.AI.Tvg_pk.Settings, btn := SHU_GVL.AI.Tvg_pk.FromHMI, out := SHU_GVL.AI.Tvg_pk.ToHMI, my := SHU_GVL.AI.Tvg_pk.Intern, nOk := SHU_GVL.AI_FLT);
// [A1.4:13] Резерв
VGSig.fnAI_Processing(IN := SHU_GVL.AI.Reserv_0.DRV, set := SHU_GVL.AI.Reserv_0.Settings, btn := SHU_GVL.AI.Reserv_0.FromHMI, out := SHU_GVL.AI.Reserv_0.ToHMI, my := SHU_GVL.AI.Reserv_0.Intern, nOk := SHU_GVL.AI_FLT);
// [A1.4:14] Резерв
VGSig.fnAI_Processing(IN := SHU_GVL.AI.Reserv_1.DRV, set := SHU_GVL.AI.Reserv_1.Settings, btn := SHU_GVL.AI.Reserv_1.FromHMI, out := SHU_GVL.AI.Reserv_1.ToHMI, my := SHU_GVL.AI.Reserv_1.Intern, nOk := SHU_GVL.AI_FLT);
// [A1.4:15] Резерв
VGSig.fnAI_Processing(IN := SHU_GVL.AI.Reserv_2.DRV, set := SHU_GVL.AI.Reserv_2.Settings, btn := SHU_GVL.AI.Reserv_2.FromHMI, out := SHU_GVL.AI.Reserv_2.ToHMI, my := SHU_GVL.AI.Reserv_2.Intern, nOk := SHU_GVL.AI_FLT);
// [A1.4:16] Резерв
VGSig.fnAI_Processing(IN := SHU_GVL.AI.Reserv_3.DRV, set := SHU_GVL.AI.Reserv_3.Settings, btn := SHU_GVL.AI.Reserv_3.FromHMI, out := SHU_GVL.AI.Reserv_3.ToHMI, my := SHU_GVL.AI.Reserv_3.Intern, nOk := SHU_GVL.AI_FLT);
// [A1.5:1] Температура коренного подшипника № 1
VGSig.fnAI_Processing(IN := SHU_GVL.AI.Tkp_1.DRV, set := SHU_GVL.AI.Tkp_1.Settings, btn := SHU_GVL.AI.Tkp_1.FromHMI, out := SHU_GVL.AI.Tkp_1.ToHMI, my := SHU_GVL.AI.Tkp_1.Intern, nOk := SHU_GVL.AI_FLT);
// [A1.5:2] Температура коренного подшипника № 2
VGSig.fnAI_Processing(IN := SHU_GVL.AI.Tkp_2.DRV, set := SHU_GVL.AI.Tkp_2.Settings, btn := SHU_GVL.AI.Tkp_2.FromHMI, out := SHU_GVL.AI.Tkp_2.ToHMI, my := SHU_GVL.AI.Tkp_2.Intern, nOk := SHU_GVL.AI_FLT);
// [A1.5:3] Температура коренного подшипника № 3
VGSig.fnAI_Processing(IN := SHU_GVL.AI.Tkp_3.DRV, set := SHU_GVL.AI.Tkp_3.Settings, btn := SHU_GVL.AI.Tkp_3.FromHMI, out := SHU_GVL.AI.Tkp_3.ToHMI, my := SHU_GVL.AI.Tkp_3.Intern, nOk := SHU_GVL.AI_FLT);
// [A1.5:4] Температура коренного подшипника № 4
VGSig.fnAI_Processing(IN := SHU_GVL.AI.Tkp_4.DRV, set := SHU_GVL.AI.Tkp_4.Settings, btn := SHU_GVL.AI.Tkp_4.FromHMI, out := SHU_GVL.AI.Tkp_4.ToHMI, my := SHU_GVL.AI.Tkp_4.Intern, nOk := SHU_GVL.AI_FLT);
// [A1.5:5] Температура коренного подшипника № 5
VGSig.fnAI_Processing(IN := SHU_GVL.AI.Tkp_5.DRV, set := SHU_GVL.AI.Tkp_5.Settings, btn := SHU_GVL.AI.Tkp_5.FromHMI, out := SHU_GVL.AI.Tkp_5.ToHMI, my := SHU_GVL.AI.Tkp_5.Intern, nOk := SHU_GVL.AI_FLT);
// [A1.5:6] Температура коренного подшипника № 6
VGSig.fnAI_Processing(IN := SHU_GVL.AI.Tkp_6.DRV, set := SHU_GVL.AI.Tkp_6.Settings, btn := SHU_GVL.AI.Tkp_6.FromHMI, out := SHU_GVL.AI.Tkp_6.ToHMI, my := SHU_GVL.AI.Tkp_6.Intern, nOk := SHU_GVL.AI_FLT);
// [A1.5:7] Температура коренного подшипника № 7
VGSig.fnAI_Processing(IN := SHU_GVL.AI.Tkp_7.DRV, set := SHU_GVL.AI.Tkp_7.Settings, btn := SHU_GVL.AI.Tkp_7.FromHMI, out := SHU_GVL.AI.Tkp_7.ToHMI, my := SHU_GVL.AI.Tkp_7.Intern, nOk := SHU_GVL.AI_FLT);
// [A1.5:8] Температура коренного подшипника № 8
VGSig.fnAI_Processing(IN := SHU_GVL.AI.Tkp_8.DRV, set := SHU_GVL.AI.Tkp_8.Settings, btn := SHU_GVL.AI.Tkp_8.FromHMI, out := SHU_GVL.AI.Tkp_8.ToHMI, my := SHU_GVL.AI.Tkp_8.Intern, nOk := SHU_GVL.AI_FLT);
// [A1.5:9] Температура коренного подшипника № 9
VGSig.fnAI_Processing(IN := SHU_GVL.AI.Tkp_9.DRV, set := SHU_GVL.AI.Tkp_9.Settings, btn := SHU_GVL.AI.Tkp_9.FromHMI, out := SHU_GVL.AI.Tkp_9.ToHMI, my := SHU_GVL.AI.Tkp_9.Intern, nOk := SHU_GVL.AI_FLT);
// [A1.5:10] Температура коренного подшипника № 10
VGSig.fnAI_Processing(IN := SHU_GVL.AI.Tkp_10.DRV, set := SHU_GVL.AI.Tkp_10.Settings, btn := SHU_GVL.AI.Tkp_10.FromHMI, out := SHU_GVL.AI.Tkp_10.ToHMI, my := SHU_GVL.AI.Tkp_10.Intern, nOk := SHU_GVL.AI_FLT);
// [A1.5:11] Температура воды на входе в двигатель
VGSig.fnAI_Processing(IN := SHU_GVL.AI.Tv_inD.DRV, set := SHU_GVL.AI.Tv_inD.Settings, btn := SHU_GVL.AI.Tv_inD.FromHMI, out := SHU_GVL.AI.Tv_inD.ToHMI, my := SHU_GVL.AI.Tv_inD.Intern, nOk := SHU_GVL.AI_FLT);
// [A1.5:12] Температура воды на выходе из двигателя
VGSig.fnAI_Processing(IN := SHU_GVL.AI.Tv_outD.DRV, set := SHU_GVL.AI.Tv_outD.Settings, btn := SHU_GVL.AI.Tv_outD.FromHMI, out := SHU_GVL.AI.Tv_outD.ToHMI, my := SHU_GVL.AI.Tv_outD.Intern, nOk := SHU_GVL.AI_FLT);
// [A1.5:13] Температура воздуха наддува
VGSig.fnAI_Processing(IN := SHU_GVL.AI.Tvn.DRV, set := SHU_GVL.AI.Tvn.Settings, btn := SHU_GVL.AI.Tvn.FromHMI, out := SHU_GVL.AI.Tvn.ToHMI, my := SHU_GVL.AI.Tvn.Intern, nOk := SHU_GVL.AI_FLT);
// [A1.5:14] Температура масла на входе в ГМК
VGSig.fnAI_Processing(IN := SHU_GVL.AI.Tm_inGMK.DRV, set := SHU_GVL.AI.Tm_inGMK.Settings, btn := SHU_GVL.AI.Tm_inGMK.FromHMI, out := SHU_GVL.AI.Tm_inGMK.ToHMI, my := SHU_GVL.AI.Tm_inGMK.Intern, nOk := SHU_GVL.AI_FLT);
// [A1.5:15] Температура масла на выходе из ГМК
VGSig.fnAI_Processing(IN := SHU_GVL.AI.Tm_outGMK.DRV, set := SHU_GVL.AI.Tm_outGMK.Settings, btn := SHU_GVL.AI.Tm_outGMK.FromHMI, out := SHU_GVL.AI.Tm_outGMK.ToHMI, my := SHU_GVL.AI.Tm_outGMK.Intern, nOk := SHU_GVL.AI_FLT);
// [A1.5:16] Резерв
VGSig.fnAI_Processing(IN := SHU_GVL.AI.Reserv_4.DRV, set := SHU_GVL.AI.Reserv_4.Settings, btn := SHU_GVL.AI.Reserv_4.FromHMI, out := SHU_GVL.AI.Reserv_4.ToHMI, my := SHU_GVL.AI.Reserv_4.Intern, nOk := SHU_GVL.AI_FLT);
// [A1.6:1] Температура газа на выходе компрессорного цилиндра 1
VGSig.fnAI_Processing(IN := SHU_GVL.AI.Tg_outKC_1.DRV, set := SHU_GVL.AI.Tg_outKC_1.Settings, btn := SHU_GVL.AI.Tg_outKC_1.FromHMI, out := SHU_GVL.AI.Tg_outKC_1.ToHMI, my := SHU_GVL.AI.Tg_outKC_1.Intern, nOk := SHU_GVL.AI_FLT);
// [A1.6:2] Температура газа на выходе компрессорного цилиндра 2
VGSig.fnAI_Processing(IN := SHU_GVL.AI.Tg_outKC_2.DRV, set := SHU_GVL.AI.Tg_outKC_2.Settings, btn := SHU_GVL.AI.Tg_outKC_2.FromHMI, out := SHU_GVL.AI.Tg_outKC_2.ToHMI, my := SHU_GVL.AI.Tg_outKC_2.Intern, nOk := SHU_GVL.AI_FLT);
// [A1.6:3] Температура газа на выходе компрессорного цилиндра 3
VGSig.fnAI_Processing(IN := SHU_GVL.AI.Tg_outKC_3.DRV, set := SHU_GVL.AI.Tg_outKC_3.Settings, btn := SHU_GVL.AI.Tg_outKC_3.FromHMI, out := SHU_GVL.AI.Tg_outKC_3.ToHMI, my := SHU_GVL.AI.Tg_outKC_3.Intern, nOk := SHU_GVL.AI_FLT);
// [A1.6:4] Температура газа на выходе компрессорного цилиндра 4
VGSig.fnAI_Processing(IN := SHU_GVL.AI.Tg_outKC_4.DRV, set := SHU_GVL.AI.Tg_outKC_4.Settings, btn := SHU_GVL.AI.Tg_outKC_4.FromHMI, out := SHU_GVL.AI.Tg_outKC_4.ToHMI, my := SHU_GVL.AI.Tg_outKC_4.Intern, nOk := SHU_GVL.AI_FLT);
// [A1.6:5] Температура газа на выходе компрессорного цилиндра 5
VGSig.fnAI_Processing(IN := SHU_GVL.AI.Tg_outKC_5.DRV, set := SHU_GVL.AI.Tg_outKC_5.Settings, btn := SHU_GVL.AI.Tg_outKC_5.FromHMI, out := SHU_GVL.AI.Tg_outKC_5.ToHMI, my := SHU_GVL.AI.Tg_outKC_5.Intern, nOk := SHU_GVL.AI_FLT);
// [A1.6:6] Резерв
VGSig.fnAI_Processing(IN := SHU_GVL.AI.Reserv_5.DRV, set := SHU_GVL.AI.Reserv_5.Settings, btn := SHU_GVL.AI.Reserv_5.FromHMI, out := SHU_GVL.AI.Reserv_5.ToHMI, my := SHU_GVL.AI.Reserv_5.Intern, nOk := SHU_GVL.AI_FLT);
// [A1.6:7] Резерв
VGSig.fnAI_Processing(IN := SHU_GVL.AI.Reserv_6.DRV, set := SHU_GVL.AI.Reserv_6.Settings, btn := SHU_GVL.AI.Reserv_6.FromHMI, out := SHU_GVL.AI.Reserv_6.ToHMI, my := SHU_GVL.AI.Reserv_6.Intern, nOk := SHU_GVL.AI_FLT);
// [A1.6:8] Резерв
VGSig.fnAI_Processing(IN := SHU_GVL.AI.Reserv_7.DRV, set := SHU_GVL.AI.Reserv_7.Settings, btn := SHU_GVL.AI.Reserv_7.FromHMI, out := SHU_GVL.AI.Reserv_7.ToHMI, my := SHU_GVL.AI.Reserv_7.Intern, nOk := SHU_GVL.AI_FLT);
// [A1.6:9] Резерв
VGSig.fnAI_Processing(IN := SHU_GVL.AI.Reserv_8.DRV, set := SHU_GVL.AI.Reserv_8.Settings, btn := SHU_GVL.AI.Reserv_8.FromHMI, out := SHU_GVL.AI.Reserv_8.ToHMI, my := SHU_GVL.AI.Reserv_8.Intern, nOk := SHU_GVL.AI_FLT);
// [A1.6:10] Резерв
VGSig.fnAI_Processing(IN := SHU_GVL.AI.Reserv_9.DRV, set := SHU_GVL.AI.Reserv_9.Settings, btn := SHU_GVL.AI.Reserv_9.FromHMI, out := SHU_GVL.AI.Reserv_9.ToHMI, my := SHU_GVL.AI.Reserv_9.Intern, nOk := SHU_GVL.AI_FLT);
// [A1.6:14] Управление запорно-регулирующим клапаном на приёме ГМК PV4601.1. КЦУ
VGSig.fnAI_Processing(IN := SHU_GVL.AI.RegKr1_KCU.DRV, set := SHU_GVL.AI.RegKr1_KCU.Settings, btn := SHU_GVL.AI.RegKr1_KCU.FromHMI, out := SHU_GVL.AI.RegKr1_KCU.ToHMI, my := SHU_GVL.AI.RegKr1_KCU.Intern, nOk := SHU_GVL.AI_FLT);
// [A1.6:15] Напряжение основного питания ~220 В
VGSig.fnAI_Processing(IN := SHU_GVL.AI.U_Osn_AC.DRV, set := SHU_GVL.AI.U_Osn_AC.Settings, btn := SHU_GVL.AI.U_Osn_AC.FromHMI, out := SHU_GVL.AI.U_Osn_AC.ToHMI, my := SHU_GVL.AI.U_Osn_AC.Intern, nOk := SHU_GVL.AI_FLT);
// [A1.6:16] Напряжение резервного питания ~220 В
VGSig.fnAI_Processing(IN := SHU_GVL.AI.U_Res_AC.DRV, set := SHU_GVL.AI.U_Res_AC.Settings, btn := SHU_GVL.AI.U_Res_AC.FromHMI, out := SHU_GVL.AI.U_Res_AC.ToHMI, my := SHU_GVL.AI.U_Res_AC.Intern, nOk := SHU_GVL.AI_FLT);
// [A1.7:1] Давление газа на входе в ГМК
VGSig.fnAI_Processing(IN := SHU_GVL.AI.Pg_inGMK.DRV, set := SHU_GVL.AI.Pg_inGMK.Settings, btn := SHU_GVL.AI.Pg_inGMK.FromHMI, out := SHU_GVL.AI.Pg_inGMK.ToHMI, my := SHU_GVL.AI.Pg_inGMK.Intern, nOk := SHU_GVL.AI_FLT);
// [A1.7:2] Давление газа на выходе из ГМК
VGSig.fnAI_Processing(IN := SHU_GVL.AI.Pg_outGMK.DRV, set := SHU_GVL.AI.Pg_outGMK.Settings, btn := SHU_GVL.AI.Pg_outGMK.FromHMI, out := SHU_GVL.AI.Pg_outGMK.ToHMI, my := SHU_GVL.AI.Pg_outGMK.Intern, nOk := SHU_GVL.AI_FLT);
// [A1.7:3] Давление пускового воздуха
VGSig.fnAI_Processing(IN := SHU_GVL.AI.Ppv.DRV, set := SHU_GVL.AI.Ppv.Settings, btn := SHU_GVL.AI.Ppv.FromHMI, out := SHU_GVL.AI.Ppv.ToHMI, my := SHU_GVL.AI.Ppv.Intern, nOk := SHU_GVL.AI_FLT);
// [A1.7:4] Давление топливного газа до ТРК
VGSig.fnAI_Processing(IN := SHU_GVL.AI.Ptg_inTRK.DRV, set := SHU_GVL.AI.Ptg_inTRK.Settings, btn := SHU_GVL.AI.Ptg_inTRK.FromHMI, out := SHU_GVL.AI.Ptg_inTRK.ToHMI, my := SHU_GVL.AI.Ptg_inTRK.Intern, nOk := SHU_GVL.AI_FLT);
// [A1.7:5] Давление топливного газа после ТРК
VGSig.fnAI_Processing(IN := SHU_GVL.AI.Ptg_outTRK.DRV, set := SHU_GVL.AI.Ptg_outTRK.Settings, btn := SHU_GVL.AI.Ptg_outTRK.FromHMI, out := SHU_GVL.AI.Ptg_outTRK.ToHMI, my := SHU_GVL.AI.Ptg_outTRK.Intern, nOk := SHU_GVL.AI_FLT);
// [A1.7:6] Давление воздуха наддува
VGSig.fnAI_Processing(IN := SHU_GVL.AI.Pvn.DRV, set := SHU_GVL.AI.Pvn.Settings, btn := SHU_GVL.AI.Pvn.FromHMI, out := SHU_GVL.AI.Pvn.ToHMI, my := SHU_GVL.AI.Pvn.Intern, nOk := SHU_GVL.AI_FLT);
// [A1.7:7] Давление масла на входе в турбокомпрессоры
VGSig.fnAI_Processing(IN := SHU_GVL.AI.Pm_inTK.DRV, set := SHU_GVL.AI.Pm_inTK.Settings, btn := SHU_GVL.AI.Pm_inTK.FromHMI, out := SHU_GVL.AI.Pm_inTK.ToHMI, my := SHU_GVL.AI.Pm_inTK.Intern, nOk := SHU_GVL.AI_FLT);
// [A1.7:8] Давление масла на входе в двигатель
VGSig.fnAI_Processing(IN := SHU_GVL.AI.Pm_inD.DRV, set := SHU_GVL.AI.Pm_inD.Settings, btn := SHU_GVL.AI.Pm_inD.FromHMI, out := SHU_GVL.AI.Pm_inD.ToHMI, my := SHU_GVL.AI.Pm_inD.Intern, nOk := SHU_GVL.AI_FLT);
// [A1.7:9] Перепад давления масла на фильтре
VGSig.fnAI_Processing(IN := SHU_GVL.AI.dPmf.DRV, set := SHU_GVL.AI.dPmf.Settings, btn := SHU_GVL.AI.dPmf.FromHMI, out := SHU_GVL.AI.dPmf.ToHMI, my := SHU_GVL.AI.dPmf.Intern, nOk := SHU_GVL.AI_FLT);
// [A1.7:10] Давление воды на выходе из двигателя
VGSig.fnAI_Processing(IN := SHU_GVL.AI.Pv_outD.DRV, set := SHU_GVL.AI.Pv_outD.Settings, btn := SHU_GVL.AI.Pv_outD.FromHMI, out := SHU_GVL.AI.Pv_outD.ToHMI, my := SHU_GVL.AI.Pv_outD.Intern, nOk := SHU_GVL.AI_FLT);
// [A1.7:11] Положение ТРК PV9604.1
VGSig.fnAI_Processing(IN := SHU_GVL.AI.Pos_TRK.DRV, set := SHU_GVL.AI.Pos_TRK.Settings, btn := SHU_GVL.AI.Pos_TRK.FromHMI, out := SHU_GVL.AI.Pos_TRK.ToHMI, my := SHU_GVL.AI.Pos_TRK.Intern, nOk := SHU_GVL.AI_FLT);
// [A1.7:12] Положение запорно-регулирующего клапана на приёме ГМК PV4601.1
VGSig.fnAI_Processing(IN := SHU_GVL.AI.Pos_RegKr1.DRV, set := SHU_GVL.AI.Pos_RegKr1.Settings, btn := SHU_GVL.AI.Pos_RegKr1.FromHMI, out := SHU_GVL.AI.Pos_RegKr1.ToHMI, my := SHU_GVL.AI.Pos_RegKr1.Intern, nOk := SHU_GVL.AI_FLT);
// [A1.7:13] Уровень вибрации ГМК (виброскорость), канал 1
VGSig.fnAI_Processing(IN := SHU_GVL.AI.Vb_Ch_1.DRV, set := SHU_GVL.AI.Vb_Ch_1.Settings, btn := SHU_GVL.AI.Vb_Ch_1.FromHMI, out := SHU_GVL.AI.Vb_Ch_1.ToHMI, my := SHU_GVL.AI.Vb_Ch_1.Intern, nOk := SHU_GVL.AI_FLT);
// [A1.7:14] Уровень вибрации ГМК (виброскорость), канал 2
VGSig.fnAI_Processing(IN := SHU_GVL.AI.Vb_Ch_2.DRV, set := SHU_GVL.AI.Vb_Ch_2.Settings, btn := SHU_GVL.AI.Vb_Ch_2.FromHMI, out := SHU_GVL.AI.Vb_Ch_2.ToHMI, my := SHU_GVL.AI.Vb_Ch_2.Intern, nOk := SHU_GVL.AI_FLT);
// [A1.7:15] Резерв
VGSig.fnAI_Processing(IN := SHU_GVL.AI.Reserv_10.DRV, set := SHU_GVL.AI.Reserv_10.Settings, btn := SHU_GVL.AI.Reserv_10.FromHMI, out := SHU_GVL.AI.Reserv_10.ToHMI, my := SHU_GVL.AI.Reserv_10.Intern, nOk := SHU_GVL.AI_FLT);
// [A1.7:16] Резерв
VGSig.fnAI_Processing(IN := SHU_GVL.AI.Reserv_11.DRV, set := SHU_GVL.AI.Reserv_11.Settings, btn := SHU_GVL.AI.Reserv_11.FromHMI, out := SHU_GVL.AI.Reserv_11.ToHMI, my := SHU_GVL.AI.Reserv_11.Intern, nOk := SHU_GVL.AI_FLT);
"""
proj = projects.primary
folder = proj.find('AI SHU', recursive=True)[0]
struktur = folder.create_pou('SHU_AI_Call', type = PouType.Function,language=None, return_type='BOOL', base_type=None, interfaces=None)
struktur.textual_declaration.insert(4, 0, CONTENT_var)
struktur.textual_implementation.insert(0, 0, CONTENT_body)
