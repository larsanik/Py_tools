#encoding:utf-8
from __future__ import print_function
CONTENT_var = """\
 repTime: INT;
"""
CONTENT_body = """\
repTime := 3600; // время ремонта аналоговых входов
//================ Инициализация настроек аналоговых выходов(вызывается один раз при старте) ================
IF NOT SHU_GVL.init THEN
//------------------------------- аргументы функции инициализации --------------------------------
//                                  минимум шкалы канала, ед.изм. Не может быть >= max
//                                 |   максимум шкалы канала, ед.изм. Не может быть <= min
//                                 |   |   значение АЦП, соответствующее минимуму шкалы канала, б.р.
//                                 |   |   |   значение АЦП, соотв. макс. шкалы, б.р. Не может быть равно minADC
//                                 |   |   |   |
//                                 |   |   |   |   номер по порядку
//AO_init(UPG_AO_Settings.Pg_in_UPG,0.0,6.0,2.0,10.0,0);
//-------------------------------------------------------------------------------------------
	// [A1.12:1]Управление запорно-регулирующим клапаном на приёме ГМК PV4601.1
	VGSig.fnAO_init(setStruct => SHU_GVL.AO.Set_RegKr1.Settings, min_PV := 0, max_PV := 100, minDAC := 4, maxDAC := 20, id := 1);
END_IF;

//================ Обработчик аналоговых входов================
// [A1.12:1] Управление запорно-регулирующим клапаном на приёме ГМК PV4601.1
VGSig.fnAO_Processing(IN := SHU_GVL.AO.Set_RegKr1.ToHMI.PV, set := SHU_GVL.AO.Set_RegKr1.Settings, hmi := SHU_GVL.AO.Set_RegKr1.FromHMI, plc := SHU_GVL.AO.Set_RegKr1.ToHMI, out => SHU_GVL.AO.Set_RegKr1.DRV);
"""
proj = projects.primary
folder = proj.find('AO SHU', recursive=True)[0]
struktur = folder.create_pou('SHU_AO_Call', type = PouType.Function,language=None, return_type='BOOL', base_type=None, interfaces=None)
struktur.textual_declaration.insert(4, 0, CONTENT_var)
struktur.textual_implementation.insert(0, 0, CONTENT_body)
