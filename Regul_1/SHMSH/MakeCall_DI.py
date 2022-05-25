#encoding:utf-8
from __future__ import print_function
CONTENT_var = """\
 repTime: INT;
"""
CONTENT_body = """\
repTime := 3600; // время ремонта дискретных входов
//================ Инициализация настроек дискретных входов(вызывается один раз при старте) ================
IF NOT SHMSH_GVL.init THEN
//------------------------------- аргументы функции инициализации --------------------------------
//                             максимальное время в ремонте, сек. Не может быть меньше или равно «0»
//                                |       задержка от дребезга
//                               |       |    признак инверсии
//                               |       |    |   номер по порядку
//DI_init(GPA_DI_Settings.BK_OF,repTime,0.0,false,0);
//-------------------------------------------------------------------------------------------
	// [A1.3:1]Контроль питания ШМШ ~220 В
VGSig.fnDI_init(setStruct => SHMSH_GVL.DGI.Check_U_SHMSH_AC_V.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 1);
	// [A1.3:2]Исправность БП ШМШ
VGSig.fnDI_init(setStruct => SHMSH_GVL.DGI.Ispr_BP_SHMSH.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 2);
	// [A1.3:3]Исправность БП БУЗ
VGSig.fnDI_init(setStruct => SHMSH_GVL.DGI.Ispr_BP_BUZ.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 3);
	// [A1.3:4]Исправность БП БКД
VGSig.fnDI_init(setStruct => SHMSH_GVL.DGI.Ispr_BP_N.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 4);
	// [A1.3:5]Исправность БП блока согласующего системы контроля вибрации
VGSig.fnDI_init(setStruct => SHMSH_GVL.DGI.Ispr_BP_BS_SKV.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 5);
	// [A1.3:6]Автоматы питания включены
VGSig.fnDI_init(setStruct => SHMSH_GVL.DGI.AvtPwr_ON.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 6);
	// [A1.3:7]Кнопка "Предыдущий экран"
VGSig.fnDI_init(setStruct => SHMSH_GVL.DGI.Btn_PrevScr.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 7);
	// [A1.3:8]Кнопка "Следующий экран"
VGSig.fnDI_init(setStruct => SHMSH_GVL.DGI.Btn_NextScr.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 8);
	// [A1.4:1]Кнопка "Выбор цилиндра"
VGSig.fnDI_init(setStruct => SHMSH_GVL.DGI.Btn_Vybor_Cyl.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 9);
	// [A1.4:2]Кнопка "УОЗ меньше"
VGSig.fnDI_init(setStruct => SHMSH_GVL.DGI.Btn_UOZ_Down.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 10);
	// [A1.4:3]Кнопка "УОЗ больше"
VGSig.fnDI_init(setStruct => SHMSH_GVL.DGI.Btn_UOZ_Up.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 11);
	// [A1.4:4]Кнопка "Принудительный останов"
VGSig.fnDI_init(setStruct => SHMSH_GVL.DGI.Btn_AO.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 12);
	// [A1.4:5]Кнопка "Нормальный останов"
VGSig.fnDI_init(setStruct => SHMSH_GVL.DGI.Btn_NO.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 13);
	// [A1.4:6]Кнопка "Пуск ГПА"
VGSig.fnDI_init(setStruct => SHMSH_GVL.DGI.Btn_Pusk_GPA.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 14);
	// [A1.4:7]Кнопка "Деблокировка"
VGSig.fnDI_init(setStruct => SHMSH_GVL.DGI.Btn_Deblock.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 15);
END_IF;

//================ Обработчик дискретных входов================
// [A1.3:1] Контроль питания ШМШ ~220 В
VGSig.fnDI_Processing(IN := SHMSH_GVL.DGI.Check_U_SHMSH_AC_V.DRV, externalFault := FALSE, set := SHMSH_GVL.DGI.Check_U_SHMSH_AC_V.Settings, FromHMI := SHMSH_GVL.DGI.Check_U_SHMSH_AC_V.FromHMI, ToHMI := SHMSH_GVL.DGI.Check_U_SHMSH_AC_V.ToHMI, my := SHMSH_GVL.DGI.Check_U_SHMSH_AC_V.Intern, out := SHMSH_GVL.DGI.Check_U_SHMSH_AC_V.PV);
// [A1.3:2] Исправность БП ШМШ
VGSig.fnDI_Processing(IN := SHMSH_GVL.DGI.Ispr_BP_SHMSH.DRV, externalFault := FALSE, set := SHMSH_GVL.DGI.Ispr_BP_SHMSH.Settings, FromHMI := SHMSH_GVL.DGI.Ispr_BP_SHMSH.FromHMI, ToHMI := SHMSH_GVL.DGI.Ispr_BP_SHMSH.ToHMI, my := SHMSH_GVL.DGI.Ispr_BP_SHMSH.Intern, out := SHMSH_GVL.DGI.Ispr_BP_SHMSH.PV);
// [A1.3:3] Исправность БП БУЗ
VGSig.fnDI_Processing(IN := SHMSH_GVL.DGI.Ispr_BP_BUZ.DRV, externalFault := FALSE, set := SHMSH_GVL.DGI.Ispr_BP_BUZ.Settings, FromHMI := SHMSH_GVL.DGI.Ispr_BP_BUZ.FromHMI, ToHMI := SHMSH_GVL.DGI.Ispr_BP_BUZ.ToHMI, my := SHMSH_GVL.DGI.Ispr_BP_BUZ.Intern, out := SHMSH_GVL.DGI.Ispr_BP_BUZ.PV);
// [A1.3:4] Исправность БП БКД
VGSig.fnDI_Processing(IN := SHMSH_GVL.DGI.Ispr_BP_N.DRV, externalFault := FALSE, set := SHMSH_GVL.DGI.Ispr_BP_N.Settings, FromHMI := SHMSH_GVL.DGI.Ispr_BP_N.FromHMI, ToHMI := SHMSH_GVL.DGI.Ispr_BP_N.ToHMI, my := SHMSH_GVL.DGI.Ispr_BP_N.Intern, out := SHMSH_GVL.DGI.Ispr_BP_N.PV);
// [A1.3:5] Исправность БП блока согласующего системы контроля вибрации
VGSig.fnDI_Processing(IN := SHMSH_GVL.DGI.Ispr_BP_BS_SKV.DRV, externalFault := FALSE, set := SHMSH_GVL.DGI.Ispr_BP_BS_SKV.Settings, FromHMI := SHMSH_GVL.DGI.Ispr_BP_BS_SKV.FromHMI, ToHMI := SHMSH_GVL.DGI.Ispr_BP_BS_SKV.ToHMI, my := SHMSH_GVL.DGI.Ispr_BP_BS_SKV.Intern, out := SHMSH_GVL.DGI.Ispr_BP_BS_SKV.PV);
// [A1.3:6] Автоматы питания включены
VGSig.fnDI_Processing(IN := SHMSH_GVL.DGI.AvtPwr_ON.DRV, externalFault := FALSE, set := SHMSH_GVL.DGI.AvtPwr_ON.Settings, FromHMI := SHMSH_GVL.DGI.AvtPwr_ON.FromHMI, ToHMI := SHMSH_GVL.DGI.AvtPwr_ON.ToHMI, my := SHMSH_GVL.DGI.AvtPwr_ON.Intern, out := SHMSH_GVL.DGI.AvtPwr_ON.PV);
// [A1.3:7] Кнопка "Предыдущий экран"
VGSig.fnDI_Processing(IN := SHMSH_GVL.DGI.Btn_PrevScr.DRV, externalFault := FALSE, set := SHMSH_GVL.DGI.Btn_PrevScr.Settings, FromHMI := SHMSH_GVL.DGI.Btn_PrevScr.FromHMI, ToHMI := SHMSH_GVL.DGI.Btn_PrevScr.ToHMI, my := SHMSH_GVL.DGI.Btn_PrevScr.Intern, out := SHMSH_GVL.DGI.Btn_PrevScr.PV);
// [A1.3:8] Кнопка "Следующий экран"
VGSig.fnDI_Processing(IN := SHMSH_GVL.DGI.Btn_NextScr.DRV, externalFault := FALSE, set := SHMSH_GVL.DGI.Btn_NextScr.Settings, FromHMI := SHMSH_GVL.DGI.Btn_NextScr.FromHMI, ToHMI := SHMSH_GVL.DGI.Btn_NextScr.ToHMI, my := SHMSH_GVL.DGI.Btn_NextScr.Intern, out := SHMSH_GVL.DGI.Btn_NextScr.PV);
// [A1.4:1] Кнопка "Выбор цилиндра"
VGSig.fnDI_Processing(IN := SHMSH_GVL.DGI.Btn_Vybor_Cyl.DRV, externalFault := FALSE, set := SHMSH_GVL.DGI.Btn_Vybor_Cyl.Settings, FromHMI := SHMSH_GVL.DGI.Btn_Vybor_Cyl.FromHMI, ToHMI := SHMSH_GVL.DGI.Btn_Vybor_Cyl.ToHMI, my := SHMSH_GVL.DGI.Btn_Vybor_Cyl.Intern, out := SHMSH_GVL.DGI.Btn_Vybor_Cyl.PV);
// [A1.4:2] Кнопка "УОЗ меньше"
VGSig.fnDI_Processing(IN := SHMSH_GVL.DGI.Btn_UOZ_Down.DRV, externalFault := FALSE, set := SHMSH_GVL.DGI.Btn_UOZ_Down.Settings, FromHMI := SHMSH_GVL.DGI.Btn_UOZ_Down.FromHMI, ToHMI := SHMSH_GVL.DGI.Btn_UOZ_Down.ToHMI, my := SHMSH_GVL.DGI.Btn_UOZ_Down.Intern, out := SHMSH_GVL.DGI.Btn_UOZ_Down.PV);
// [A1.4:3] Кнопка "УОЗ больше"
VGSig.fnDI_Processing(IN := SHMSH_GVL.DGI.Btn_UOZ_Up.DRV, externalFault := FALSE, set := SHMSH_GVL.DGI.Btn_UOZ_Up.Settings, FromHMI := SHMSH_GVL.DGI.Btn_UOZ_Up.FromHMI, ToHMI := SHMSH_GVL.DGI.Btn_UOZ_Up.ToHMI, my := SHMSH_GVL.DGI.Btn_UOZ_Up.Intern, out := SHMSH_GVL.DGI.Btn_UOZ_Up.PV);
// [A1.4:4] Кнопка "Принудительный останов"
VGSig.fnDI_Processing(IN := SHMSH_GVL.DGI.Btn_AO.DRV, externalFault := FALSE, set := SHMSH_GVL.DGI.Btn_AO.Settings, FromHMI := SHMSH_GVL.DGI.Btn_AO.FromHMI, ToHMI := SHMSH_GVL.DGI.Btn_AO.ToHMI, my := SHMSH_GVL.DGI.Btn_AO.Intern, out := SHMSH_GVL.DGI.Btn_AO.PV);
// [A1.4:5] Кнопка "Нормальный останов"
VGSig.fnDI_Processing(IN := SHMSH_GVL.DGI.Btn_NO.DRV, externalFault := FALSE, set := SHMSH_GVL.DGI.Btn_NO.Settings, FromHMI := SHMSH_GVL.DGI.Btn_NO.FromHMI, ToHMI := SHMSH_GVL.DGI.Btn_NO.ToHMI, my := SHMSH_GVL.DGI.Btn_NO.Intern, out := SHMSH_GVL.DGI.Btn_NO.PV);
// [A1.4:6] Кнопка "Пуск ГПА"
VGSig.fnDI_Processing(IN := SHMSH_GVL.DGI.Btn_Pusk_GPA.DRV, externalFault := FALSE, set := SHMSH_GVL.DGI.Btn_Pusk_GPA.Settings, FromHMI := SHMSH_GVL.DGI.Btn_Pusk_GPA.FromHMI, ToHMI := SHMSH_GVL.DGI.Btn_Pusk_GPA.ToHMI, my := SHMSH_GVL.DGI.Btn_Pusk_GPA.Intern, out := SHMSH_GVL.DGI.Btn_Pusk_GPA.PV);
// [A1.4:7] Кнопка "Деблокировка"
VGSig.fnDI_Processing(IN := SHMSH_GVL.DGI.Btn_Deblock.DRV, externalFault := FALSE, set := SHMSH_GVL.DGI.Btn_Deblock.Settings, FromHMI := SHMSH_GVL.DGI.Btn_Deblock.FromHMI, ToHMI := SHMSH_GVL.DGI.Btn_Deblock.ToHMI, my := SHMSH_GVL.DGI.Btn_Deblock.Intern, out := SHMSH_GVL.DGI.Btn_Deblock.PV);
"""
proj = projects.primary
folder = proj.find('DI SHMSH', recursive=True)[0]
struktur = folder.create_pou('SHMSH_DI_Call', type = PouType.Function,language=None, return_type='BOOL', base_type=None, interfaces=None)
struktur.textual_declaration.insert(4, 0, CONTENT_var)
struktur.textual_implementation.insert(0, 0, CONTENT_body)
