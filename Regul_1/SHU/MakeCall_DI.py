#encoding:utf-8
from __future__ import print_function
CONTENT_var = """\
 repTime: INT;
"""
CONTENT_body = """\
repTime := 3600; // время ремонта дискретных входов
//================ Инициализация настроек дискретных входов(вызывается один раз при старте) ================
IF NOT SHU_GVL.init THEN
//------------------------------- аргументы функции инициализации --------------------------------
//                             максимальное время в ремонте, сек. Не может быть меньше или равно «0»
//                                |       задержка от дребезга
//                               |       |    признак инверсии
//                               |       |    |   номер по порядку
//DI_init(GPA_DI_Settings.BK_OF,repTime,0.0,false,0);
//-------------------------------------------------------------------------------------------
	// [A1.8:1]Клапан ESDV9601.1 на приёме ГМК открыт
VGSig.fnDI_init(setStruct => SHU_GVL.DGI.Kr1_ON.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 1);
	// [A1.8:2]Клапан ESDV9601.1 на приёме ГМК закрыт
VGSig.fnDI_init(setStruct => SHU_GVL.DGI.Kr1_OF.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 2);
	// [A1.8:3]Клапан ESDV9602.1 на выходе ГМК открыт
VGSig.fnDI_init(setStruct => SHU_GVL.DGI.Kr2_ON.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 3);
	// [A1.8:4]Клапан ESDV9602.1 на выходе ГМК закрыт
VGSig.fnDI_init(setStruct => SHU_GVL.DGI.Kr2_OF.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 4);
	// [A1.8:5]Клапан XV9605.1 на перемычке открыт
VGSig.fnDI_init(setStruct => SHU_GVL.DGI.Kr5_ON.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 5);
	// [A1.8:6]Клапан XV9605.1 на перемычке закрыт
VGSig.fnDI_init(setStruct => SHU_GVL.DGI.Kr5_OF.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 6);
	// [A1.8:7]Клапан XV9613.1 на сбросе приёмной линии открыт
VGSig.fnDI_init(setStruct => SHU_GVL.DGI.Kr13_ON.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 7);
	// [A1.8:8]Клапан XV9613.1 на сбросе приёмной линии закрыт
VGSig.fnDI_init(setStruct => SHU_GVL.DGI.Kr13_OF.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 8);
	// [A1.8:9]Резерв
VGSig.fnDI_init(setStruct => SHU_GVL.DGI.Reserv_0.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 9);
	// [A1.8:10]Резерв
VGSig.fnDI_init(setStruct => SHU_GVL.DGI.Reserv_1.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 10);
	// [A1.8:11]Резерв
VGSig.fnDI_init(setStruct => SHU_GVL.DGI.Reserv_2.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 11);
	// [A1.8:12]Резерв
VGSig.fnDI_init(setStruct => SHU_GVL.DGI.Reserv_3.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 12);
	// [A1.8:13]Трехходовой клапан XV9610.1 на топливной линии открыт
VGSig.fnDI_init(setStruct => SHU_GVL.DGI.Kr10_ON.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 13);
	// [A1.8:14]Трехходовой клапан XV9610.1 на топливной линии закрыт
VGSig.fnDI_init(setStruct => SHU_GVL.DGI.Kr10_OF.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 14);
	// [A1.8:15]Клапан пускового воздуха XV9608.1 открыт
VGSig.fnDI_init(setStruct => SHU_GVL.DGI.Kr8_ON.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 15);
	// [A1.8:16]Клапан пускового воздуха XV9608.1 закрыт
VGSig.fnDI_init(setStruct => SHU_GVL.DGI.Kr8_OF.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 16);
	// [A1.8:17]Насос прокачки масла включен
VGSig.fnDI_init(setStruct => SHU_GVL.DGI.Pmp_ppm_ON.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 17);
	// [A1.8:18]Насос прокачки масла в автоматическом управлении
VGSig.fnDI_init(setStruct => SHU_GVL.DGI.Pmp_ppm_AU.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 18);
	// [A1.8:19]Авария насоса прокачки масла
VGSig.fnDI_init(setStruct => SHU_GVL.DGI.A_Pmp_ppm.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 19);
	// [A1.8:20]Резерв
VGSig.fnDI_init(setStruct => SHU_GVL.DGI.Reserv_4.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 20);
	// [A1.8:21]Резерв
VGSig.fnDI_init(setStruct => SHU_GVL.DGI.Reserv_5.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 21);
	// [A1.8:22]Резерв
VGSig.fnDI_init(setStruct => SHU_GVL.DGI.Reserv_6.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 22);
	// [A1.8:23]Резерв
VGSig.fnDI_init(setStruct => SHU_GVL.DGI.Reserv_7.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 23);
	// [A1.8:24]Резерв
VGSig.fnDI_init(setStruct => SHU_GVL.DGI.Reserv_8.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 24);
	// [A1.8:25]Зажигание в работе
VGSig.fnDI_init(setStruct => SHU_GVL.DGI.Zazh_ON.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 25);
	// [A1.8:26]Клапан ESDV9611.1 на топливной линии открыт
VGSig.fnDI_init(setStruct => SHU_GVL.DGI.Kr11_ON.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 26);
	// [A1.8:27]Клапан ESDV9611.1 на топливной линии закрыт
VGSig.fnDI_init(setStruct => SHU_GVL.DGI.Kr11_OF.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 27);
	// [A1.8:28]Резерв
VGSig.fnDI_init(setStruct => SHU_GVL.DGI.Reserv_9.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 28);
	// [A1.9:9]Контроль основного пит. ШУ ГМК ~220 В
VGSig.fnDI_init(setStruct => SHU_GVL.DGI.U_Osn_AC_ON.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 29);
	// [A1.9:10]Контроль резервного пит. ШУ ГМК ~220 В
VGSig.fnDI_init(setStruct => SHU_GVL.DGI.U_Res_AC_ON.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 30);
	// [A1.9:11]Контроль исправности разрядников
VGSig.fnDI_init(setStruct => SHU_GVL.DGI.RazrGood.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 31);
	// [A1.9:12]Автоматы питания включены
VGSig.fnDI_init(setStruct => SHU_GVL.DGI.AvtPwr_ON.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 32);
	// [A1.9:13]Двери ШУ ГМК открыты
VGSig.fnDI_init(setStruct => SHU_GVL.DGI.DoorOpen.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 33);
	// [A1.9:14]Исправность осн. ИП =24 В внутр. цепей
VGSig.fnDI_init(setStruct => SHU_GVL.DGI.Ispr_Osn_DC_inC.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 34);
	// [A1.9:15]Исправность рез. ИП =24 В внутр. цепей
VGSig.fnDI_init(setStruct => SHU_GVL.DGI.Ispr_Res_DC_inC.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 35);
	// [A1.9:16]Исправность осн. ИП =24 В AI
VGSig.fnDI_init(setStruct => SHU_GVL.DGI.Ispr_Osn_DC_AI.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 36);
	// [A1.9:17]Исправность рез. ИП =24 В AI
VGSig.fnDI_init(setStruct => SHU_GVL.DGI.Ispr_Res_DC_AI.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 37);
	// [A1.9:18]Исправность осн. ИП =24 В DI (внеш.)
VGSig.fnDI_init(setStruct => SHU_GVL.DGI.Ispr_Osn_DC_DI.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 38);
	// [A1.9:19]Исправность рез. ИП =24 В DI (внеш.)
VGSig.fnDI_init(setStruct => SHU_GVL.DGI.Ispr_Res_DC_DI.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 39);
	// [A1.9:20]Исправность осн. ИП =24 В DO (внеш.)
VGSig.fnDI_init(setStruct => SHU_GVL.DGI.Ispr_Osn_DC_DO.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 40);
	// [A1.9:21]Исправность рез. ИП =24 В DO (внеш.)
VGSig.fnDI_init(setStruct => SHU_GVL.DGI.Ispr_Res_DC_DO.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 41);
	// [A1.9:22]Кнопка на двери "Аварийный останов"
VGSig.fnDI_init(setStruct => SHU_GVL.DGI.Btn_AO.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 42);
	// [A1.9:23]Кнопка на двери "Нормальный останов"
VGSig.fnDI_init(setStruct => SHU_GVL.DGI.Btn_NO.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 43);
	// [A1.9:24]Кнопка на двери "Деблокировка"
VGSig.fnDI_init(setStruct => SHU_GVL.DGI.Btn_Deblock.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 44);
	// [A1.9:25]Контроль внешнего питания ~220 В от ШУ ГМК
VGSig.fnDI_init(setStruct => SHU_GVL.DGI.U_AC_outC_ON.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 45);
END_IF;

//================ Обработчик дискретных входов================
// [A1.8:1] Клапан ESDV9601.1 на приёме ГМК открыт
VGSig.fnDI_Processing(IN := SHU_GVL.DGI.Kr1_ON.DRV, externalFault := FALSE, set := SHU_GVL.DGI.Kr1_ON.Settings, FromHMI := SHU_GVL.DGI.Kr1_ON.FromHMI, ToHMI := SHU_GVL.DGI.Kr1_ON.ToHMI, my := SHU_GVL.DGI.Kr1_ON.Intern, out := SHU_GVL.DGI.Kr1_ON.PV);
// [A1.8:2] Клапан ESDV9601.1 на приёме ГМК закрыт
VGSig.fnDI_Processing(IN := SHU_GVL.DGI.Kr1_OF.DRV, externalFault := FALSE, set := SHU_GVL.DGI.Kr1_OF.Settings, FromHMI := SHU_GVL.DGI.Kr1_OF.FromHMI, ToHMI := SHU_GVL.DGI.Kr1_OF.ToHMI, my := SHU_GVL.DGI.Kr1_OF.Intern, out := SHU_GVL.DGI.Kr1_OF.PV);
// [A1.8:3] Клапан ESDV9602.1 на выходе ГМК открыт
VGSig.fnDI_Processing(IN := SHU_GVL.DGI.Kr2_ON.DRV, externalFault := FALSE, set := SHU_GVL.DGI.Kr2_ON.Settings, FromHMI := SHU_GVL.DGI.Kr2_ON.FromHMI, ToHMI := SHU_GVL.DGI.Kr2_ON.ToHMI, my := SHU_GVL.DGI.Kr2_ON.Intern, out := SHU_GVL.DGI.Kr2_ON.PV);
// [A1.8:4] Клапан ESDV9602.1 на выходе ГМК закрыт
VGSig.fnDI_Processing(IN := SHU_GVL.DGI.Kr2_OF.DRV, externalFault := FALSE, set := SHU_GVL.DGI.Kr2_OF.Settings, FromHMI := SHU_GVL.DGI.Kr2_OF.FromHMI, ToHMI := SHU_GVL.DGI.Kr2_OF.ToHMI, my := SHU_GVL.DGI.Kr2_OF.Intern, out := SHU_GVL.DGI.Kr2_OF.PV);
// [A1.8:5] Клапан XV9605.1 на перемычке открыт
VGSig.fnDI_Processing(IN := SHU_GVL.DGI.Kr5_ON.DRV, externalFault := FALSE, set := SHU_GVL.DGI.Kr5_ON.Settings, FromHMI := SHU_GVL.DGI.Kr5_ON.FromHMI, ToHMI := SHU_GVL.DGI.Kr5_ON.ToHMI, my := SHU_GVL.DGI.Kr5_ON.Intern, out := SHU_GVL.DGI.Kr5_ON.PV);
// [A1.8:6] Клапан XV9605.1 на перемычке закрыт
VGSig.fnDI_Processing(IN := SHU_GVL.DGI.Kr5_OF.DRV, externalFault := FALSE, set := SHU_GVL.DGI.Kr5_OF.Settings, FromHMI := SHU_GVL.DGI.Kr5_OF.FromHMI, ToHMI := SHU_GVL.DGI.Kr5_OF.ToHMI, my := SHU_GVL.DGI.Kr5_OF.Intern, out := SHU_GVL.DGI.Kr5_OF.PV);
// [A1.8:7] Клапан XV9613.1 на сбросе приёмной линии открыт
VGSig.fnDI_Processing(IN := SHU_GVL.DGI.Kr13_ON.DRV, externalFault := FALSE, set := SHU_GVL.DGI.Kr13_ON.Settings, FromHMI := SHU_GVL.DGI.Kr13_ON.FromHMI, ToHMI := SHU_GVL.DGI.Kr13_ON.ToHMI, my := SHU_GVL.DGI.Kr13_ON.Intern, out := SHU_GVL.DGI.Kr13_ON.PV);
// [A1.8:8] Клапан XV9613.1 на сбросе приёмной линии закрыт
VGSig.fnDI_Processing(IN := SHU_GVL.DGI.Kr13_OF.DRV, externalFault := FALSE, set := SHU_GVL.DGI.Kr13_OF.Settings, FromHMI := SHU_GVL.DGI.Kr13_OF.FromHMI, ToHMI := SHU_GVL.DGI.Kr13_OF.ToHMI, my := SHU_GVL.DGI.Kr13_OF.Intern, out := SHU_GVL.DGI.Kr13_OF.PV);
// [A1.8:9] Резерв
VGSig.fnDI_Processing(IN := SHU_GVL.DGI.Reserv_0.DRV, externalFault := FALSE, set := SHU_GVL.DGI.Reserv_0.Settings, FromHMI := SHU_GVL.DGI.Reserv_0.FromHMI, ToHMI := SHU_GVL.DGI.Reserv_0.ToHMI, my := SHU_GVL.DGI.Reserv_0.Intern, out := SHU_GVL.DGI.Reserv_0.PV);
// [A1.8:10] Резерв
VGSig.fnDI_Processing(IN := SHU_GVL.DGI.Reserv_1.DRV, externalFault := FALSE, set := SHU_GVL.DGI.Reserv_1.Settings, FromHMI := SHU_GVL.DGI.Reserv_1.FromHMI, ToHMI := SHU_GVL.DGI.Reserv_1.ToHMI, my := SHU_GVL.DGI.Reserv_1.Intern, out := SHU_GVL.DGI.Reserv_1.PV);
// [A1.8:11] Резерв
VGSig.fnDI_Processing(IN := SHU_GVL.DGI.Reserv_2.DRV, externalFault := FALSE, set := SHU_GVL.DGI.Reserv_2.Settings, FromHMI := SHU_GVL.DGI.Reserv_2.FromHMI, ToHMI := SHU_GVL.DGI.Reserv_2.ToHMI, my := SHU_GVL.DGI.Reserv_2.Intern, out := SHU_GVL.DGI.Reserv_2.PV);
// [A1.8:12] Резерв
VGSig.fnDI_Processing(IN := SHU_GVL.DGI.Reserv_3.DRV, externalFault := FALSE, set := SHU_GVL.DGI.Reserv_3.Settings, FromHMI := SHU_GVL.DGI.Reserv_3.FromHMI, ToHMI := SHU_GVL.DGI.Reserv_3.ToHMI, my := SHU_GVL.DGI.Reserv_3.Intern, out := SHU_GVL.DGI.Reserv_3.PV);
// [A1.8:13] Трехходовой клапан XV9610.1 на топливной линии открыт
VGSig.fnDI_Processing(IN := SHU_GVL.DGI.Kr10_ON.DRV, externalFault := FALSE, set := SHU_GVL.DGI.Kr10_ON.Settings, FromHMI := SHU_GVL.DGI.Kr10_ON.FromHMI, ToHMI := SHU_GVL.DGI.Kr10_ON.ToHMI, my := SHU_GVL.DGI.Kr10_ON.Intern, out := SHU_GVL.DGI.Kr10_ON.PV);
// [A1.8:14] Трехходовой клапан XV9610.1 на топливной линии закрыт
VGSig.fnDI_Processing(IN := SHU_GVL.DGI.Kr10_OF.DRV, externalFault := FALSE, set := SHU_GVL.DGI.Kr10_OF.Settings, FromHMI := SHU_GVL.DGI.Kr10_OF.FromHMI, ToHMI := SHU_GVL.DGI.Kr10_OF.ToHMI, my := SHU_GVL.DGI.Kr10_OF.Intern, out := SHU_GVL.DGI.Kr10_OF.PV);
// [A1.8:15] Клапан пускового воздуха XV9608.1 открыт
VGSig.fnDI_Processing(IN := SHU_GVL.DGI.Kr8_ON.DRV, externalFault := FALSE, set := SHU_GVL.DGI.Kr8_ON.Settings, FromHMI := SHU_GVL.DGI.Kr8_ON.FromHMI, ToHMI := SHU_GVL.DGI.Kr8_ON.ToHMI, my := SHU_GVL.DGI.Kr8_ON.Intern, out := SHU_GVL.DGI.Kr8_ON.PV);
// [A1.8:16] Клапан пускового воздуха XV9608.1 закрыт
VGSig.fnDI_Processing(IN := SHU_GVL.DGI.Kr8_OF.DRV, externalFault := FALSE, set := SHU_GVL.DGI.Kr8_OF.Settings, FromHMI := SHU_GVL.DGI.Kr8_OF.FromHMI, ToHMI := SHU_GVL.DGI.Kr8_OF.ToHMI, my := SHU_GVL.DGI.Kr8_OF.Intern, out := SHU_GVL.DGI.Kr8_OF.PV);
// [A1.8:17] Насос прокачки масла включен
VGSig.fnDI_Processing(IN := SHU_GVL.DGI.Pmp_ppm_ON.DRV, externalFault := FALSE, set := SHU_GVL.DGI.Pmp_ppm_ON.Settings, FromHMI := SHU_GVL.DGI.Pmp_ppm_ON.FromHMI, ToHMI := SHU_GVL.DGI.Pmp_ppm_ON.ToHMI, my := SHU_GVL.DGI.Pmp_ppm_ON.Intern, out := SHU_GVL.DGI.Pmp_ppm_ON.PV);
// [A1.8:18] Насос прокачки масла в автоматическом управлении
VGSig.fnDI_Processing(IN := SHU_GVL.DGI.Pmp_ppm_AU.DRV, externalFault := FALSE, set := SHU_GVL.DGI.Pmp_ppm_AU.Settings, FromHMI := SHU_GVL.DGI.Pmp_ppm_AU.FromHMI, ToHMI := SHU_GVL.DGI.Pmp_ppm_AU.ToHMI, my := SHU_GVL.DGI.Pmp_ppm_AU.Intern, out := SHU_GVL.DGI.Pmp_ppm_AU.PV);
// [A1.8:19] Авария насоса прокачки масла
VGSig.fnDI_Processing(IN := SHU_GVL.DGI.A_Pmp_ppm.DRV, externalFault := FALSE, set := SHU_GVL.DGI.A_Pmp_ppm.Settings, FromHMI := SHU_GVL.DGI.A_Pmp_ppm.FromHMI, ToHMI := SHU_GVL.DGI.A_Pmp_ppm.ToHMI, my := SHU_GVL.DGI.A_Pmp_ppm.Intern, out := SHU_GVL.DGI.A_Pmp_ppm.PV);
// [A1.8:20] Резерв
VGSig.fnDI_Processing(IN := SHU_GVL.DGI.Reserv_4.DRV, externalFault := FALSE, set := SHU_GVL.DGI.Reserv_4.Settings, FromHMI := SHU_GVL.DGI.Reserv_4.FromHMI, ToHMI := SHU_GVL.DGI.Reserv_4.ToHMI, my := SHU_GVL.DGI.Reserv_4.Intern, out := SHU_GVL.DGI.Reserv_4.PV);
// [A1.8:21] Резерв
VGSig.fnDI_Processing(IN := SHU_GVL.DGI.Reserv_5.DRV, externalFault := FALSE, set := SHU_GVL.DGI.Reserv_5.Settings, FromHMI := SHU_GVL.DGI.Reserv_5.FromHMI, ToHMI := SHU_GVL.DGI.Reserv_5.ToHMI, my := SHU_GVL.DGI.Reserv_5.Intern, out := SHU_GVL.DGI.Reserv_5.PV);
// [A1.8:22] Резерв
VGSig.fnDI_Processing(IN := SHU_GVL.DGI.Reserv_6.DRV, externalFault := FALSE, set := SHU_GVL.DGI.Reserv_6.Settings, FromHMI := SHU_GVL.DGI.Reserv_6.FromHMI, ToHMI := SHU_GVL.DGI.Reserv_6.ToHMI, my := SHU_GVL.DGI.Reserv_6.Intern, out := SHU_GVL.DGI.Reserv_6.PV);
// [A1.8:23] Резерв
VGSig.fnDI_Processing(IN := SHU_GVL.DGI.Reserv_7.DRV, externalFault := FALSE, set := SHU_GVL.DGI.Reserv_7.Settings, FromHMI := SHU_GVL.DGI.Reserv_7.FromHMI, ToHMI := SHU_GVL.DGI.Reserv_7.ToHMI, my := SHU_GVL.DGI.Reserv_7.Intern, out := SHU_GVL.DGI.Reserv_7.PV);
// [A1.8:24] Резерв
VGSig.fnDI_Processing(IN := SHU_GVL.DGI.Reserv_8.DRV, externalFault := FALSE, set := SHU_GVL.DGI.Reserv_8.Settings, FromHMI := SHU_GVL.DGI.Reserv_8.FromHMI, ToHMI := SHU_GVL.DGI.Reserv_8.ToHMI, my := SHU_GVL.DGI.Reserv_8.Intern, out := SHU_GVL.DGI.Reserv_8.PV);
// [A1.8:25] Зажигание в работе
VGSig.fnDI_Processing(IN := SHU_GVL.DGI.Zazh_ON.DRV, externalFault := FALSE, set := SHU_GVL.DGI.Zazh_ON.Settings, FromHMI := SHU_GVL.DGI.Zazh_ON.FromHMI, ToHMI := SHU_GVL.DGI.Zazh_ON.ToHMI, my := SHU_GVL.DGI.Zazh_ON.Intern, out := SHU_GVL.DGI.Zazh_ON.PV);
// [A1.8:26] Клапан ESDV9611.1 на топливной линии открыт
VGSig.fnDI_Processing(IN := SHU_GVL.DGI.Kr11_ON.DRV, externalFault := FALSE, set := SHU_GVL.DGI.Kr11_ON.Settings, FromHMI := SHU_GVL.DGI.Kr11_ON.FromHMI, ToHMI := SHU_GVL.DGI.Kr11_ON.ToHMI, my := SHU_GVL.DGI.Kr11_ON.Intern, out := SHU_GVL.DGI.Kr11_ON.PV);
// [A1.8:27] Клапан ESDV9611.1 на топливной линии закрыт
VGSig.fnDI_Processing(IN := SHU_GVL.DGI.Kr11_OF.DRV, externalFault := FALSE, set := SHU_GVL.DGI.Kr11_OF.Settings, FromHMI := SHU_GVL.DGI.Kr11_OF.FromHMI, ToHMI := SHU_GVL.DGI.Kr11_OF.ToHMI, my := SHU_GVL.DGI.Kr11_OF.Intern, out := SHU_GVL.DGI.Kr11_OF.PV);
// [A1.8:28] Резерв
VGSig.fnDI_Processing(IN := SHU_GVL.DGI.Reserv_9.DRV, externalFault := FALSE, set := SHU_GVL.DGI.Reserv_9.Settings, FromHMI := SHU_GVL.DGI.Reserv_9.FromHMI, ToHMI := SHU_GVL.DGI.Reserv_9.ToHMI, my := SHU_GVL.DGI.Reserv_9.Intern, out := SHU_GVL.DGI.Reserv_9.PV);
// [A1.9:9] Контроль основного пит. ШУ ГМК ~220 В
VGSig.fnDI_Processing(IN := SHU_GVL.DGI.U_Osn_AC_ON.DRV, externalFault := FALSE, set := SHU_GVL.DGI.U_Osn_AC_ON.Settings, FromHMI := SHU_GVL.DGI.U_Osn_AC_ON.FromHMI, ToHMI := SHU_GVL.DGI.U_Osn_AC_ON.ToHMI, my := SHU_GVL.DGI.U_Osn_AC_ON.Intern, out := SHU_GVL.DGI.U_Osn_AC_ON.PV);
// [A1.9:10] Контроль резервного пит. ШУ ГМК ~220 В
VGSig.fnDI_Processing(IN := SHU_GVL.DGI.U_Res_AC_ON.DRV, externalFault := FALSE, set := SHU_GVL.DGI.U_Res_AC_ON.Settings, FromHMI := SHU_GVL.DGI.U_Res_AC_ON.FromHMI, ToHMI := SHU_GVL.DGI.U_Res_AC_ON.ToHMI, my := SHU_GVL.DGI.U_Res_AC_ON.Intern, out := SHU_GVL.DGI.U_Res_AC_ON.PV);
// [A1.9:11] Контроль исправности разрядников
VGSig.fnDI_Processing(IN := SHU_GVL.DGI.RazrGood.DRV, externalFault := FALSE, set := SHU_GVL.DGI.RazrGood.Settings, FromHMI := SHU_GVL.DGI.RazrGood.FromHMI, ToHMI := SHU_GVL.DGI.RazrGood.ToHMI, my := SHU_GVL.DGI.RazrGood.Intern, out := SHU_GVL.DGI.RazrGood.PV);
// [A1.9:12] Автоматы питания включены
VGSig.fnDI_Processing(IN := SHU_GVL.DGI.AvtPwr_ON.DRV, externalFault := FALSE, set := SHU_GVL.DGI.AvtPwr_ON.Settings, FromHMI := SHU_GVL.DGI.AvtPwr_ON.FromHMI, ToHMI := SHU_GVL.DGI.AvtPwr_ON.ToHMI, my := SHU_GVL.DGI.AvtPwr_ON.Intern, out := SHU_GVL.DGI.AvtPwr_ON.PV);
// [A1.9:13] Двери ШУ ГМК открыты
VGSig.fnDI_Processing(IN := SHU_GVL.DGI.DoorOpen.DRV, externalFault := FALSE, set := SHU_GVL.DGI.DoorOpen.Settings, FromHMI := SHU_GVL.DGI.DoorOpen.FromHMI, ToHMI := SHU_GVL.DGI.DoorOpen.ToHMI, my := SHU_GVL.DGI.DoorOpen.Intern, out := SHU_GVL.DGI.DoorOpen.PV);
// [A1.9:14] Исправность осн. ИП =24 В внутр. цепей
VGSig.fnDI_Processing(IN := SHU_GVL.DGI.Ispr_Osn_DC_inC.DRV, externalFault := FALSE, set := SHU_GVL.DGI.Ispr_Osn_DC_inC.Settings, FromHMI := SHU_GVL.DGI.Ispr_Osn_DC_inC.FromHMI, ToHMI := SHU_GVL.DGI.Ispr_Osn_DC_inC.ToHMI, my := SHU_GVL.DGI.Ispr_Osn_DC_inC.Intern, out := SHU_GVL.DGI.Ispr_Osn_DC_inC.PV);
// [A1.9:15] Исправность рез. ИП =24 В внутр. цепей
VGSig.fnDI_Processing(IN := SHU_GVL.DGI.Ispr_Res_DC_inC.DRV, externalFault := FALSE, set := SHU_GVL.DGI.Ispr_Res_DC_inC.Settings, FromHMI := SHU_GVL.DGI.Ispr_Res_DC_inC.FromHMI, ToHMI := SHU_GVL.DGI.Ispr_Res_DC_inC.ToHMI, my := SHU_GVL.DGI.Ispr_Res_DC_inC.Intern, out := SHU_GVL.DGI.Ispr_Res_DC_inC.PV);
// [A1.9:16] Исправность осн. ИП =24 В AI
VGSig.fnDI_Processing(IN := SHU_GVL.DGI.Ispr_Osn_DC_AI.DRV, externalFault := FALSE, set := SHU_GVL.DGI.Ispr_Osn_DC_AI.Settings, FromHMI := SHU_GVL.DGI.Ispr_Osn_DC_AI.FromHMI, ToHMI := SHU_GVL.DGI.Ispr_Osn_DC_AI.ToHMI, my := SHU_GVL.DGI.Ispr_Osn_DC_AI.Intern, out := SHU_GVL.DGI.Ispr_Osn_DC_AI.PV);
// [A1.9:17] Исправность рез. ИП =24 В AI
VGSig.fnDI_Processing(IN := SHU_GVL.DGI.Ispr_Res_DC_AI.DRV, externalFault := FALSE, set := SHU_GVL.DGI.Ispr_Res_DC_AI.Settings, FromHMI := SHU_GVL.DGI.Ispr_Res_DC_AI.FromHMI, ToHMI := SHU_GVL.DGI.Ispr_Res_DC_AI.ToHMI, my := SHU_GVL.DGI.Ispr_Res_DC_AI.Intern, out := SHU_GVL.DGI.Ispr_Res_DC_AI.PV);
// [A1.9:18] Исправность осн. ИП =24 В DI (внеш.)
VGSig.fnDI_Processing(IN := SHU_GVL.DGI.Ispr_Osn_DC_DI.DRV, externalFault := FALSE, set := SHU_GVL.DGI.Ispr_Osn_DC_DI.Settings, FromHMI := SHU_GVL.DGI.Ispr_Osn_DC_DI.FromHMI, ToHMI := SHU_GVL.DGI.Ispr_Osn_DC_DI.ToHMI, my := SHU_GVL.DGI.Ispr_Osn_DC_DI.Intern, out := SHU_GVL.DGI.Ispr_Osn_DC_DI.PV);
// [A1.9:19] Исправность рез. ИП =24 В DI (внеш.)
VGSig.fnDI_Processing(IN := SHU_GVL.DGI.Ispr_Res_DC_DI.DRV, externalFault := FALSE, set := SHU_GVL.DGI.Ispr_Res_DC_DI.Settings, FromHMI := SHU_GVL.DGI.Ispr_Res_DC_DI.FromHMI, ToHMI := SHU_GVL.DGI.Ispr_Res_DC_DI.ToHMI, my := SHU_GVL.DGI.Ispr_Res_DC_DI.Intern, out := SHU_GVL.DGI.Ispr_Res_DC_DI.PV);
// [A1.9:20] Исправность осн. ИП =24 В DO (внеш.)
VGSig.fnDI_Processing(IN := SHU_GVL.DGI.Ispr_Osn_DC_DO.DRV, externalFault := FALSE, set := SHU_GVL.DGI.Ispr_Osn_DC_DO.Settings, FromHMI := SHU_GVL.DGI.Ispr_Osn_DC_DO.FromHMI, ToHMI := SHU_GVL.DGI.Ispr_Osn_DC_DO.ToHMI, my := SHU_GVL.DGI.Ispr_Osn_DC_DO.Intern, out := SHU_GVL.DGI.Ispr_Osn_DC_DO.PV);
// [A1.9:21] Исправность рез. ИП =24 В DO (внеш.)
VGSig.fnDI_Processing(IN := SHU_GVL.DGI.Ispr_Res_DC_DO.DRV, externalFault := FALSE, set := SHU_GVL.DGI.Ispr_Res_DC_DO.Settings, FromHMI := SHU_GVL.DGI.Ispr_Res_DC_DO.FromHMI, ToHMI := SHU_GVL.DGI.Ispr_Res_DC_DO.ToHMI, my := SHU_GVL.DGI.Ispr_Res_DC_DO.Intern, out := SHU_GVL.DGI.Ispr_Res_DC_DO.PV);
// [A1.9:22] Кнопка на двери "Аварийный останов"
VGSig.fnDI_Processing(IN := SHU_GVL.DGI.Btn_AO.DRV, externalFault := FALSE, set := SHU_GVL.DGI.Btn_AO.Settings, FromHMI := SHU_GVL.DGI.Btn_AO.FromHMI, ToHMI := SHU_GVL.DGI.Btn_AO.ToHMI, my := SHU_GVL.DGI.Btn_AO.Intern, out := SHU_GVL.DGI.Btn_AO.PV);
// [A1.9:23] Кнопка на двери "Нормальный останов"
VGSig.fnDI_Processing(IN := SHU_GVL.DGI.Btn_NO.DRV, externalFault := FALSE, set := SHU_GVL.DGI.Btn_NO.Settings, FromHMI := SHU_GVL.DGI.Btn_NO.FromHMI, ToHMI := SHU_GVL.DGI.Btn_NO.ToHMI, my := SHU_GVL.DGI.Btn_NO.Intern, out := SHU_GVL.DGI.Btn_NO.PV);
// [A1.9:24] Кнопка на двери "Деблокировка"
VGSig.fnDI_Processing(IN := SHU_GVL.DGI.Btn_Deblock.DRV, externalFault := FALSE, set := SHU_GVL.DGI.Btn_Deblock.Settings, FromHMI := SHU_GVL.DGI.Btn_Deblock.FromHMI, ToHMI := SHU_GVL.DGI.Btn_Deblock.ToHMI, my := SHU_GVL.DGI.Btn_Deblock.Intern, out := SHU_GVL.DGI.Btn_Deblock.PV);
// [A1.9:25] Контроль внешнего питания ~220 В от ШУ ГМК
VGSig.fnDI_Processing(IN := SHU_GVL.DGI.U_AC_outC_ON.DRV, externalFault := FALSE, set := SHU_GVL.DGI.U_AC_outC_ON.Settings, FromHMI := SHU_GVL.DGI.U_AC_outC_ON.FromHMI, ToHMI := SHU_GVL.DGI.U_AC_outC_ON.ToHMI, my := SHU_GVL.DGI.U_AC_outC_ON.Intern, out := SHU_GVL.DGI.U_AC_outC_ON.PV);
"""
proj = projects.primary
folder = proj.find('DI SHU', recursive=True)[0]
struktur = folder.create_pou('SHU_DI_Call', type = PouType.Function,language=None, return_type='BOOL', base_type=None, interfaces=None)
struktur.textual_declaration.insert(4, 0, CONTENT_var)
struktur.textual_implementation.insert(0, 0, CONTENT_body)
