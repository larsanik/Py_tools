#encoding:utf-8
from __future__ import print_function
CONTENT_POU = """\
	repTime: INT;
"""
CONTENT_POU_2 = """\
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
	// [A1.4:1] [:F1:1,F1:3] Температура силового цилиндра 1
	VGSig.fnAI_init(setStruct => SHU_GVL.AI.Tsc_1.Settings, min_PV := 0.0, max_PV := 600.0, minADC := 4.0, maxADC := 20.0, loLim := -18.0, hiLim := 618.0, loBrk := -36.0, hiBrk := 636.0, maxROC := 0.0, recoveryTime := 5.0, repairTime := repTime, tau := 1.0, id := 1, corrADC := 0.0);
	// [A1.4:2] [:F1:5,F1:7] Температура силового цилиндра 2
	VGSig.fnAI_init(setStruct => SHU_GVL.AI.Tsc_2.Settings, min_PV := 0.0, max_PV := 600.0, minADC := 4.0, maxADC := 20.0, loLim := -18.0, hiLim := 618.0, loBrk := -36.0, hiBrk := 636.0, maxROC := 0.0, recoveryTime := 5.0, repairTime := repTime, tau := 1.0, id := 1, corrADC := 0.0);
END_IF;
//================ Обработчик аналоговых входов ================ 
 // [A1.4:1] [:F1:1,F1:3] Температура силового цилиндра 1
VGSig.fnAI_Processing(IN := SHU_GVL.AI.Tsc_1.DRV, set := SHU_GVL.AI.Tsc_1.Settings, btn := SHU_GVL.AI.Tsc_1.FromHMI, out := SHU_GVL.AI.Tsc_1.ToHMI, my := SHU_GVL.AI.Tsc_1.Intern, nOk := SHU_GVL.AI_FLT);
// [A1.4:2] [:F1:5,F1:7] Температура силового цилиндра 2
VGSig.fnAI_Processing(IN := SHU_GVL.AI.Tsc_2.DRV, set := SHU_GVL.AI.Tsc_2.Settings, btn := SHU_GVL.AI.Tsc_2.FromHMI, out := SHU_GVL.AI.Tsc_2.ToHMI, my := SHU_GVL.AI.Tsc_2.Intern, nOk := SHU_GVL.AI_FLT);
"""

proj = projects.primary
folder = proj.find('Parameter lists SHU', recursive=True)[0]
#struktur = folder.create_pou(name='Fn_POU', type=PouType.Function)#, language=None, return_type=None, base_type=None, interfaces=None)
struktur = folder.create_pou(name='Fn_POU', type = PouType.Function,language=None, return_type='BOOL', base_type=None, interfaces=None)
struktur.textual_declaration.insert(4, 0, CONTENT_POU)
struktur.textual_implementation.insert(0, 0, CONTENT_POU_2)