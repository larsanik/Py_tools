#encoding:utf-8
from __future__ import print_function
CONTENT_var = """\
 repTime: INT;
"""
CONTENT_body = """\
repTime := 3600; // время ремонта дискретных входов
//================ Инициализация настроек дискретных входов(вызывается один раз при старте) ================
IF NOT PAZ_GVL.init THEN
//------------------------------- аргументы функции инициализации --------------------------------
//                             максимальное время в ремонте, сек. Не может быть меньше или равно «0»
//                                |       задержка от дребезга
//                               |       |    признак инверсии
//                               |       |    |   номер по порядку
//DI_init(GPA_DI_Settings.BK_OF,repTime,0.0,false,0);
//-------------------------------------------------------------------------------------------
	// [A1.6:1]Частота вращения коленчатого вала ГМК №44 (канал 1)
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.Fvkv_GMK_44_Ch_1.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 1);
	// [A1.6:2]Частота вращения коленчатого вала ГМК №45 (канал 1)
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.Fvkv_GMK_45_Ch_1.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 2);
	// [A1.6:3]Частота вращения коленчатого вала ГМК №46 (канал 1)
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.Fvkv_GMK_46_Ch_1.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 3);
	// [A1.6:4]Частота вращения коленчатого вала ГМК №47 (канал 1)
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.Fvkv_GMK_47_Ch_1.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 4);
	// [A1.6:5]Частота вращения коленчатого вала ГМК №48 (канал 1)
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.Fvkv_GMK_48_Ch_1.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 5);
	// [A1.6:6]Частота вращения коленчатого вала ГМК №51 (канал 1)
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.Fvkv_GMK_51_Ch_1.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 6);
	// [A1.6:7]Частота вращения коленчатого вала ГМК №52 (канал 1)
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.Fvkv_GMK_52_Ch_1.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 7);
	// [A1.6:8]Резерв
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.Reserv_0.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 8);
	// [A1.6:9]Резерв
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.Reserv_1.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 9);
	// [A1.6:10]Резерв
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.Reserv_2.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 10);
	// [A1.6:11]Резерв
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.Reserv_3.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 11);
	// [A1.6:12]Резерв
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.Reserv_4.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 12);
	// [A1.6:13]Резерв
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.Reserv_5.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 13);
	// [A1.6:14]Разрешение на внесение изменений
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.RazrVnesIzm.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 14);
	// [A1.6:15]Блокировка ПАЗ ГМК №44
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.Block_PAZ_GMK_44.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 15);
	// [A1.6:16]Блокировка ПАЗ ГМК №45
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.Block_PAZ_GMK_45.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 16);
	// [A1.6:17]Блокировка ПАЗ ГМК №46
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.Block_PAZ_GMK_46.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 17);
	// [A1.6:18]Блокировка ПАЗ ГМК №47
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.Block_PAZ_GMK_47.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 18);
	// [A1.6:19]Блокировка ПАЗ ГМК №48
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.Block_PAZ_GMK_48.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 19);
	// [A1.6:20]Блокировка ПАЗ ГМК №51
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.Block_PAZ_GMK_51.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 20);
	// [A1.6:21]Блокировка ПАЗ ГМК №52
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.Block_PAZ_GMK_52.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 21);
	// [A1.6:22]Ввод резервного  ПЛК
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.Vvod_Reserv_PLC.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 22);
	// [A1.6:23]Запуск ПАЗ ГМК №44
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.Pusk_PAZ_GMK_44.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 23);
	// [A1.6:24]Запуск ПАЗ ГМК №45
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.Pusk_PAZ_GMK_45.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 24);
	// [A1.6:25]Запуск ПАЗ ГМК №46
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.Pusk_PAZ_GMK_46.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 25);
	// [A1.6:26]Запуск ПАЗ ГМК №47
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.Pusk_PAZ_GMK_47.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 26);
	// [A1.6:27]Запуск ПАЗ ГМК №48
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.Pusk_PAZ_GMK_48.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 27);
	// [A1.6:28]Запуск ПАЗ ГМК №51
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.Pusk_PAZ_GMK_51.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 28);
	// [A1.7:1]Запуск ПАЗ ГМК №52
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.Pusk_PAZ_GMK_52.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 29);
	// [A1.7:2]Съем звука
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.Sound_OF.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 30);
	// [A1.7:3]Сигналы внутренней диагностики 1
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.SignVnDiag_1.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 31);
	// [A1.7:4]Сигналы внутренней диагностики 2
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.SignVnDiag_2.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 32);
	// [A1.7:5]Сигналы внутренней диагностики 3
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.SignVnDiag_3.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 33);
	// [A1.7:6]Сигналы внутренней диагностики 4
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.SignVnDiag_4.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 34);
	// [A1.7:7]Частота вращения коленчатого вала ГМК №44 (канал 2)
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.Fvkv_GMK_44_Ch_2.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 35);
	// [A1.7:8]Частота вращения коленчатого вала ГМК №45 (канал 2)
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.Fvkv_GMK_45_Ch_2.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 36);
	// [A1.7:9]Частота вращения коленчатого вала ГМК №46 (канал 2)
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.Fvkv_GMK_46_Ch_2.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 37);
	// [A1.7:10]Частота вращения коленчатого вала ГМК №47 (канал 2)
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.Fvkv_GMK_47_Ch_2.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 38);
	// [A1.7:11]Частота вращения коленчатого вала ГМК №48 (канал 2)
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.Fvkv_GMK_48_Ch_2.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 39);
	// [A1.7:12]Частота вращения коленчатого вала ГМК №51 (канал 2)
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.Fvkv_GMK_51_Ch_2.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 40);
	// [A1.7:13]Частота вращения коленчатого вала ГМК №52 (канал 2)
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.Fvkv_GMK_52_Ch_2.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 41);
	// [A1.7:14]Резерв
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.Reserv_6.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 42);
	// [A1.7:15]Клапан ESDV9601.1 на приёме ГМК открыт
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.Kl_ESDV9601_1_ON.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 43);
	// [A1.7:16]Клапан ESDV9601.1 на приёме ГМК закрыт
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.Kl_ESDV9601_1_OF.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 44);
	// [A1.7:17]Клапан ESDV9602.1 на выходе ГМК открыт
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.Kl_ESDV9602_1_ON.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 45);
	// [A1.7:18]Клапан ESDV9602.1 на выходе ГМК закрыт
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.Kl_ESDV9602_1_OF.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 46);
	// [A1.7:19]Клапан ESDV9611.1 на топливной линии открыт
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.Kl_ESDV9611_1_ON.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 47);
	// [A1.7:20]Клапан ESDV9611.1 на топливной линии закрыт
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.Kl_ESDV9611_1_OF.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 48);
	// [A1.7:21]Клапан ESDV9601.2 на приёме ГМК открыт
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.Kl_ESDV9601_2_ON.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 49);
	// [A1.7:22]Клапан ESDV9601.2 на приёме ГМК закрыт
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.Kl_ESDV9601_2_OF.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 50);
	// [A1.7:23]Клапан ESDV9602.2 на выходе ГМК открыт
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.Kl_ESDV9602_2_ON.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 51);
	// [A1.7:24]Клапан ESDV9602.2 на выходе ГМК закрыт
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.Kl_ESDV9602_2_OF.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 52);
	// [A1.7:25]Клапан ESDV9611.2 на топливной линии открыт
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.Kl_ESDV9611_2_ON.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 53);
	// [A1.7:26]Клапан ESDV9611.2 на топливной линии закрыт
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.Kl_ESDV9611_2_OF.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 54);
	// [A1.7:27]Клапан ESDV9601.3 на приёме ГМК открыт
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.Kl_ESDV9601_3_ON.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 55);
	// [A1.7:28]Клапан ESDV9601.3 на приёме ГМК закрыт
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.Kl_ESDV9601_3_OF.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 56);
	// [A1.8:1]Клапан ESDV9602.3 на выходе ГМК открыт
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.Kl_ESDV9602_3_ON.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 57);
	// [A1.8:2]Клапан ESDV9602.3 на выходе ГМК закрыт
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.Kl_ESDV9602_3_OF.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 58);
	// [A1.8:3]Клапан ESDV9611.3 на топливной линии открыт
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.Kl_ESDV9611_3_ON.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 59);
	// [A1.8:4]Клапан ESDV9611.3 на топливной линии закрыт
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.Kl_ESDV9611_3_OF.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 60);
	// [A1.8:5]Клапан ESDV9601.4 на приёме ГМК открыт
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.Kl_ESDV9601_4_ON.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 61);
	// [A1.8:6]Клапан ESDV9601.4 на приёме ГМК закрыт
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.Kl_ESDV9601_4_OF.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 62);
	// [A1.8:7]Клапан ESDV9602.4 на выходе ГМК открыт
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.Kl_ESDV9602_4_ON.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 63);
	// [A1.8:8]Клапан ESDV9602.4 на выходе ГМК закрыт
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.Kl_ESDV9602_4_OF.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 64);
	// [A1.8:9]Клапан ESDV9611.4 на топливной линии открыт
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.Kl_ESDV9611_4_ON.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 65);
	// [A1.8:10]Клапан ESDV9611.4 на топливной линии закрыт
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.Kl_ESDV9611_4_OF.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 66);
	// [A1.8:11]Клапан ESDV9601.5 на приёме ГМК открыт
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.Kl_ESDV9601_5_ON.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 67);
	// [A1.8:12]Клапан ESDV9601.5 на приёме ГМК закрыт
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.Kl_ESDV9601_5_OF.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 68);
	// [A1.8:13]Клапан ESDV9602.5 на выходе ГМК открыт
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.Kl_ESDV9602_5_ON.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 69);
	// [A1.8:14]Клапан ESDV9602.5 на выходе ГМК закрыт
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.Kl_ESDV9602_5_OF.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 70);
	// [A1.8:15]Клапан ESDV9611.5 на топливной линии открыт
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.Kl_ESDV9611_5_ON.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 71);
	// [A1.8:16]Клапан ESDV9611.5 на топливной линии закрыт
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.Kl_ESDV9611_5_OF.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 72);
	// [A1.8:17]Клапан ESDV9601.6 на приёме ГМК открыт
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.Kl_ESDV9601_6_ON.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 73);
	// [A1.8:18]Клапан ESDV9601.6 на приёме ГМК закрыт
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.Kl_ESDV9601_6_OF.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 74);
	// [A1.8:19]Клапан ESDV9602.6 на выходе ГМК открыт
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.Kl_ESDV9602_6_ON.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 75);
	// [A1.8:20]Клапан ESDV9602.6 на выходе ГМК закрыт
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.Kl_ESDV9602_6_OF.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 76);
	// [A1.8:21]Клапан ESDV9611.6 на топливной линии открыт
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.Kl_ESDV9611_6_ON.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 77);
	// [A1.8:22]Клапан ESDV9611.6 на топливной линии закрыт
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.Kl_ESDV9611_6_OF.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 78);
	// [A1.8:23]Клапан ESDV9601.7 на приёме ГМК открыт
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.Kl_ESDV9601_7_ON.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 79);
	// [A1.8:24]Клапан ESDV9601.7 на приёме ГМК закрыт
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.Kl_ESDV9601_7_OF.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 80);
	// [A1.8:25]Клапан ESDV9602.7 на выходе ГМК открыт
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.Kl_ESDV9602_7_ON.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 81);
	// [A1.8:26]Клапан ESDV9602.7 на выходе ГМК закрыт
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.Kl_ESDV9602_7_OF.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 82);
	// [A1.8:27]Клапан ESDV9611.7 на топливной линии открыт
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.Kl_ESDV9611_7_ON.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 83);
	// [A1.8:28]Клапан ESDV9611.7 на топливной линии закрыт
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.Kl_ESDV9611_7_OF.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 84);
	// [A1.9:1]Аварийный останов ГМК №44 (от АСУ ТП КУОГ)
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.AO_GMK_44_ot_ASUTP_KUOG.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 85);
	// [A1.9:2]Кнопка АО на агрегате №44
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.Btn_AO_na_Agr_44.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 86);
	// [A1.9:3]Кнопка АО на агрегате №44 (2)
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.Btn_AO_na_Agr_44_2.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 87);
	// [A1.9:4]Аварийный останов ГМК №45 (от АСУ ТП КУОГ)
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.AO_GMK_45_ot_ASUTP_KUOG.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 88);
	// [A1.9:5]Кнопка АО на агрегате №45
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.Btn_AO_na_Agr_45.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 89);
	// [A1.9:6]Кнопка АО на агрегате №45 (2)
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.Btn_AO_na_Agr_45_2.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 90);
	// [A1.9:7]Аварийный останов ГМК №46 (от АСУ ТП КУОГ)
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.AO_GMK_46_ot_ASUTP_KUOG.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 91);
	// [A1.9:8]Кнопка АО на агрегате №46
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.Btn_AO_na_Agr_46.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 92);
	// [A1.9:9]Кнопка АО на агрегате №46 (2)
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.Btn_AO_na_Agr_46_2.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 93);
	// [A1.9:10]Аварийный останов ГМК №47 (от АСУ ТП КУОГ)
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.AO_GMK_47_ot_ASUTP_KUOG.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 94);
	// [A1.9:11]Кнопка АО на агрегате №47
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.Btn_AO_na_Agr_47.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 95);
	// [A1.9:12]Кнопка АО на агрегате №47 (2)
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.Btn_AO_na_Agr_47_2.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 96);
	// [A1.9:13]Аварийный останов ГМК №48 (от АСУ ТП КУОГ)
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.AO_GMK_48_ot_ASUTP_KUOG.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 97);
	// [A1.9:14]Кнопка АО на агрегате №48
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.Btn_AO_na_Agr_48.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 98);
	// [A1.9:15]Кнопка АО на агрегате №48 (2)
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.Btn_AO_na_Agr_48_2.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 99);
	// [A1.9:16]Аварийный останов ГМК №51 (от АСУ ТП КУОГ)
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.AO_GMK_51_ot_ASUTP_KUOG.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 100);
	// [A1.9:17]Кнопка АО на агрегате №51
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.Btn_AO_na_Agr_51.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 101);
	// [A1.9:18]Кнопка АО на агрегате №51 (2)
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.Btn_AO_na_Agr_51_2.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 102);
	// [A1.9:19]Аварийный останов ГМК №52 (от АСУ ТП КУОГ)
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.AO_GMK_52_ot_ASUTP_KUOG.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 103);
	// [A1.9:20]Кнопка АО на агрегате №52
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.Btn_AO_na_Agr_52.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 104);
	// [A1.9:21]Кнопка АО на агрегате №52 (2)
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.Btn_AO_na_Agr_52_2.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 105);
	// [A1.9:22]Резерв
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.Reserv_7.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 106);
	// [A1.9:23]Резерв
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.Reserv_8.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 107);
	// [A1.9:24]Резерв
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.Reserv_9.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 108);
	// [A1.9:25]Резерв
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.Reserv_10.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 109);
	// [A1.9:26]Резерв
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.Reserv_11.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 110);
	// [A1.9:27]Резерв
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.Reserv_12.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 111);
	// [A1.9:28]Резерв
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.Reserv_13.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 112);
	// [A1.10:1]Разрешение на внесение изменений (2)
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.RazrVnesIzm_2.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 113);
	// [A1.10:2]Блокировка ПАЗ ГМК №44 (2)
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.Block_PAZ_GMK_44_2.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 114);
	// [A1.10:3]Блокировка ПАЗ ГМК №45 (2)
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.Block_PAZ_GMK_45_2.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 115);
	// [A1.10:4]Блокировка ПАЗ ГМК №46 (2)
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.Block_PAZ_GMK_46_2.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 116);
	// [A1.10:5]Блокировка ПАЗ ГМК №47 (2)
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.Block_PAZ_GMK_47_2.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 117);
	// [A1.10:6]Блокировка ПАЗ ГМК №48 (2)
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.Block_PAZ_GMK_48_2.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 118);
	// [A1.10:7]Блокировка ПАЗ ГМК №51 (2)
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.Block_PAZ_GMK_51_2.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 119);
	// [A1.10:8]Блокировка ПАЗ ГМК №52 (2)
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.Block_PAZ_GMK_52_2.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 120);
	// [A1.10:9]Ввод резервного  ПЛК (2)
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.Vvod_Reserv_PLC_2.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 121);
	// [A1.10:10]Запуск ПАЗ ГМК №44 (2)
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.Pusk_PAZ_GMK_44_2.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 122);
	// [A1.10:11]Запуск ПАЗ ГМК №45 (2)
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.Pusk_PAZ_GMK_45_2.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 123);
	// [A1.10:12]Запуск ПАЗ ГМК №46 (2)
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.Pusk_PAZ_GMK_46_2.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 124);
	// [A1.10:13]Запуск ПАЗ ГМК №47 (2)
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.Pusk_PAZ_GMK_47_2.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 125);
	// [A1.10:14]Запуск ПАЗ ГМК №48 (2)
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.Pusk_PAZ_GMK_48_2.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 126);
	// [A1.10:15]Запуск ПАЗ ГМК №51 (2)
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.Pusk_PAZ_GMK_51_2.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 127);
	// [A1.10:16]Запуск ПАЗ ГМК №52 (2)
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.Pusk_PAZ_GMK_52_2.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 128);
	// [A1.10:17]Съем звука (2)
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.Sound_OF_2.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 129);
	// [A1.10:18]Сигналы внутренней диагностики 5
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.SignVnDiag_5.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 130);
	// [A1.10:19]Сигналы внутренней диагностики 6
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.SignVnDiag_6.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 131);
	// [A1.10:20]Сигналы внутренней диагностики 7
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.SignVnDiag_7.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 132);
	// [A1.10:21]Сигналы внутренней диагностики 8
VGSig.fnDI_init(setStruct => PAZ_GVL.DGI.SignVnDiag_8.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := 133);
END_IF;

//================ Обработчик дискретных входов================
// [A1.6:1] Частота вращения коленчатого вала ГМК №44 (канал 1)
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.Fvkv_GMK_44_Ch_1.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.Fvkv_GMK_44_Ch_1.Settings, FromHMI := PAZ_GVL.DGI.Fvkv_GMK_44_Ch_1.FromHMI, ToHMI := PAZ_GVL.DGI.Fvkv_GMK_44_Ch_1.ToHMI, my := PAZ_GVL.DGI.Fvkv_GMK_44_Ch_1.Intern, out := PAZ_GVL.DGI.Fvkv_GMK_44_Ch_1.PV);
// [A1.6:2] Частота вращения коленчатого вала ГМК №45 (канал 1)
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.Fvkv_GMK_45_Ch_1.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.Fvkv_GMK_45_Ch_1.Settings, FromHMI := PAZ_GVL.DGI.Fvkv_GMK_45_Ch_1.FromHMI, ToHMI := PAZ_GVL.DGI.Fvkv_GMK_45_Ch_1.ToHMI, my := PAZ_GVL.DGI.Fvkv_GMK_45_Ch_1.Intern, out := PAZ_GVL.DGI.Fvkv_GMK_45_Ch_1.PV);
// [A1.6:3] Частота вращения коленчатого вала ГМК №46 (канал 1)
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.Fvkv_GMK_46_Ch_1.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.Fvkv_GMK_46_Ch_1.Settings, FromHMI := PAZ_GVL.DGI.Fvkv_GMK_46_Ch_1.FromHMI, ToHMI := PAZ_GVL.DGI.Fvkv_GMK_46_Ch_1.ToHMI, my := PAZ_GVL.DGI.Fvkv_GMK_46_Ch_1.Intern, out := PAZ_GVL.DGI.Fvkv_GMK_46_Ch_1.PV);
// [A1.6:4] Частота вращения коленчатого вала ГМК №47 (канал 1)
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.Fvkv_GMK_47_Ch_1.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.Fvkv_GMK_47_Ch_1.Settings, FromHMI := PAZ_GVL.DGI.Fvkv_GMK_47_Ch_1.FromHMI, ToHMI := PAZ_GVL.DGI.Fvkv_GMK_47_Ch_1.ToHMI, my := PAZ_GVL.DGI.Fvkv_GMK_47_Ch_1.Intern, out := PAZ_GVL.DGI.Fvkv_GMK_47_Ch_1.PV);
// [A1.6:5] Частота вращения коленчатого вала ГМК №48 (канал 1)
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.Fvkv_GMK_48_Ch_1.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.Fvkv_GMK_48_Ch_1.Settings, FromHMI := PAZ_GVL.DGI.Fvkv_GMK_48_Ch_1.FromHMI, ToHMI := PAZ_GVL.DGI.Fvkv_GMK_48_Ch_1.ToHMI, my := PAZ_GVL.DGI.Fvkv_GMK_48_Ch_1.Intern, out := PAZ_GVL.DGI.Fvkv_GMK_48_Ch_1.PV);
// [A1.6:6] Частота вращения коленчатого вала ГМК №51 (канал 1)
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.Fvkv_GMK_51_Ch_1.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.Fvkv_GMK_51_Ch_1.Settings, FromHMI := PAZ_GVL.DGI.Fvkv_GMK_51_Ch_1.FromHMI, ToHMI := PAZ_GVL.DGI.Fvkv_GMK_51_Ch_1.ToHMI, my := PAZ_GVL.DGI.Fvkv_GMK_51_Ch_1.Intern, out := PAZ_GVL.DGI.Fvkv_GMK_51_Ch_1.PV);
// [A1.6:7] Частота вращения коленчатого вала ГМК №52 (канал 1)
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.Fvkv_GMK_52_Ch_1.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.Fvkv_GMK_52_Ch_1.Settings, FromHMI := PAZ_GVL.DGI.Fvkv_GMK_52_Ch_1.FromHMI, ToHMI := PAZ_GVL.DGI.Fvkv_GMK_52_Ch_1.ToHMI, my := PAZ_GVL.DGI.Fvkv_GMK_52_Ch_1.Intern, out := PAZ_GVL.DGI.Fvkv_GMK_52_Ch_1.PV);
// [A1.6:8] Резерв
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.Reserv_0.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.Reserv_0.Settings, FromHMI := PAZ_GVL.DGI.Reserv_0.FromHMI, ToHMI := PAZ_GVL.DGI.Reserv_0.ToHMI, my := PAZ_GVL.DGI.Reserv_0.Intern, out := PAZ_GVL.DGI.Reserv_0.PV);
// [A1.6:9] Резерв
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.Reserv_1.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.Reserv_1.Settings, FromHMI := PAZ_GVL.DGI.Reserv_1.FromHMI, ToHMI := PAZ_GVL.DGI.Reserv_1.ToHMI, my := PAZ_GVL.DGI.Reserv_1.Intern, out := PAZ_GVL.DGI.Reserv_1.PV);
// [A1.6:10] Резерв
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.Reserv_2.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.Reserv_2.Settings, FromHMI := PAZ_GVL.DGI.Reserv_2.FromHMI, ToHMI := PAZ_GVL.DGI.Reserv_2.ToHMI, my := PAZ_GVL.DGI.Reserv_2.Intern, out := PAZ_GVL.DGI.Reserv_2.PV);
// [A1.6:11] Резерв
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.Reserv_3.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.Reserv_3.Settings, FromHMI := PAZ_GVL.DGI.Reserv_3.FromHMI, ToHMI := PAZ_GVL.DGI.Reserv_3.ToHMI, my := PAZ_GVL.DGI.Reserv_3.Intern, out := PAZ_GVL.DGI.Reserv_3.PV);
// [A1.6:12] Резерв
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.Reserv_4.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.Reserv_4.Settings, FromHMI := PAZ_GVL.DGI.Reserv_4.FromHMI, ToHMI := PAZ_GVL.DGI.Reserv_4.ToHMI, my := PAZ_GVL.DGI.Reserv_4.Intern, out := PAZ_GVL.DGI.Reserv_4.PV);
// [A1.6:13] Резерв
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.Reserv_5.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.Reserv_5.Settings, FromHMI := PAZ_GVL.DGI.Reserv_5.FromHMI, ToHMI := PAZ_GVL.DGI.Reserv_5.ToHMI, my := PAZ_GVL.DGI.Reserv_5.Intern, out := PAZ_GVL.DGI.Reserv_5.PV);
// [A1.6:14] Разрешение на внесение изменений
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.RazrVnesIzm.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.RazrVnesIzm.Settings, FromHMI := PAZ_GVL.DGI.RazrVnesIzm.FromHMI, ToHMI := PAZ_GVL.DGI.RazrVnesIzm.ToHMI, my := PAZ_GVL.DGI.RazrVnesIzm.Intern, out := PAZ_GVL.DGI.RazrVnesIzm.PV);
// [A1.6:15] Блокировка ПАЗ ГМК №44
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.Block_PAZ_GMK_44.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.Block_PAZ_GMK_44.Settings, FromHMI := PAZ_GVL.DGI.Block_PAZ_GMK_44.FromHMI, ToHMI := PAZ_GVL.DGI.Block_PAZ_GMK_44.ToHMI, my := PAZ_GVL.DGI.Block_PAZ_GMK_44.Intern, out := PAZ_GVL.DGI.Block_PAZ_GMK_44.PV);
// [A1.6:16] Блокировка ПАЗ ГМК №45
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.Block_PAZ_GMK_45.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.Block_PAZ_GMK_45.Settings, FromHMI := PAZ_GVL.DGI.Block_PAZ_GMK_45.FromHMI, ToHMI := PAZ_GVL.DGI.Block_PAZ_GMK_45.ToHMI, my := PAZ_GVL.DGI.Block_PAZ_GMK_45.Intern, out := PAZ_GVL.DGI.Block_PAZ_GMK_45.PV);
// [A1.6:17] Блокировка ПАЗ ГМК №46
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.Block_PAZ_GMK_46.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.Block_PAZ_GMK_46.Settings, FromHMI := PAZ_GVL.DGI.Block_PAZ_GMK_46.FromHMI, ToHMI := PAZ_GVL.DGI.Block_PAZ_GMK_46.ToHMI, my := PAZ_GVL.DGI.Block_PAZ_GMK_46.Intern, out := PAZ_GVL.DGI.Block_PAZ_GMK_46.PV);
// [A1.6:18] Блокировка ПАЗ ГМК №47
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.Block_PAZ_GMK_47.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.Block_PAZ_GMK_47.Settings, FromHMI := PAZ_GVL.DGI.Block_PAZ_GMK_47.FromHMI, ToHMI := PAZ_GVL.DGI.Block_PAZ_GMK_47.ToHMI, my := PAZ_GVL.DGI.Block_PAZ_GMK_47.Intern, out := PAZ_GVL.DGI.Block_PAZ_GMK_47.PV);
// [A1.6:19] Блокировка ПАЗ ГМК №48
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.Block_PAZ_GMK_48.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.Block_PAZ_GMK_48.Settings, FromHMI := PAZ_GVL.DGI.Block_PAZ_GMK_48.FromHMI, ToHMI := PAZ_GVL.DGI.Block_PAZ_GMK_48.ToHMI, my := PAZ_GVL.DGI.Block_PAZ_GMK_48.Intern, out := PAZ_GVL.DGI.Block_PAZ_GMK_48.PV);
// [A1.6:20] Блокировка ПАЗ ГМК №51
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.Block_PAZ_GMK_51.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.Block_PAZ_GMK_51.Settings, FromHMI := PAZ_GVL.DGI.Block_PAZ_GMK_51.FromHMI, ToHMI := PAZ_GVL.DGI.Block_PAZ_GMK_51.ToHMI, my := PAZ_GVL.DGI.Block_PAZ_GMK_51.Intern, out := PAZ_GVL.DGI.Block_PAZ_GMK_51.PV);
// [A1.6:21] Блокировка ПАЗ ГМК №52
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.Block_PAZ_GMK_52.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.Block_PAZ_GMK_52.Settings, FromHMI := PAZ_GVL.DGI.Block_PAZ_GMK_52.FromHMI, ToHMI := PAZ_GVL.DGI.Block_PAZ_GMK_52.ToHMI, my := PAZ_GVL.DGI.Block_PAZ_GMK_52.Intern, out := PAZ_GVL.DGI.Block_PAZ_GMK_52.PV);
// [A1.6:22] Ввод резервного  ПЛК
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.Vvod_Reserv_PLC.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.Vvod_Reserv_PLC.Settings, FromHMI := PAZ_GVL.DGI.Vvod_Reserv_PLC.FromHMI, ToHMI := PAZ_GVL.DGI.Vvod_Reserv_PLC.ToHMI, my := PAZ_GVL.DGI.Vvod_Reserv_PLC.Intern, out := PAZ_GVL.DGI.Vvod_Reserv_PLC.PV);
// [A1.6:23] Запуск ПАЗ ГМК №44
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.Pusk_PAZ_GMK_44.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.Pusk_PAZ_GMK_44.Settings, FromHMI := PAZ_GVL.DGI.Pusk_PAZ_GMK_44.FromHMI, ToHMI := PAZ_GVL.DGI.Pusk_PAZ_GMK_44.ToHMI, my := PAZ_GVL.DGI.Pusk_PAZ_GMK_44.Intern, out := PAZ_GVL.DGI.Pusk_PAZ_GMK_44.PV);
// [A1.6:24] Запуск ПАЗ ГМК №45
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.Pusk_PAZ_GMK_45.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.Pusk_PAZ_GMK_45.Settings, FromHMI := PAZ_GVL.DGI.Pusk_PAZ_GMK_45.FromHMI, ToHMI := PAZ_GVL.DGI.Pusk_PAZ_GMK_45.ToHMI, my := PAZ_GVL.DGI.Pusk_PAZ_GMK_45.Intern, out := PAZ_GVL.DGI.Pusk_PAZ_GMK_45.PV);
// [A1.6:25] Запуск ПАЗ ГМК №46
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.Pusk_PAZ_GMK_46.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.Pusk_PAZ_GMK_46.Settings, FromHMI := PAZ_GVL.DGI.Pusk_PAZ_GMK_46.FromHMI, ToHMI := PAZ_GVL.DGI.Pusk_PAZ_GMK_46.ToHMI, my := PAZ_GVL.DGI.Pusk_PAZ_GMK_46.Intern, out := PAZ_GVL.DGI.Pusk_PAZ_GMK_46.PV);
// [A1.6:26] Запуск ПАЗ ГМК №47
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.Pusk_PAZ_GMK_47.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.Pusk_PAZ_GMK_47.Settings, FromHMI := PAZ_GVL.DGI.Pusk_PAZ_GMK_47.FromHMI, ToHMI := PAZ_GVL.DGI.Pusk_PAZ_GMK_47.ToHMI, my := PAZ_GVL.DGI.Pusk_PAZ_GMK_47.Intern, out := PAZ_GVL.DGI.Pusk_PAZ_GMK_47.PV);
// [A1.6:27] Запуск ПАЗ ГМК №48
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.Pusk_PAZ_GMK_48.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.Pusk_PAZ_GMK_48.Settings, FromHMI := PAZ_GVL.DGI.Pusk_PAZ_GMK_48.FromHMI, ToHMI := PAZ_GVL.DGI.Pusk_PAZ_GMK_48.ToHMI, my := PAZ_GVL.DGI.Pusk_PAZ_GMK_48.Intern, out := PAZ_GVL.DGI.Pusk_PAZ_GMK_48.PV);
// [A1.6:28] Запуск ПАЗ ГМК №51
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.Pusk_PAZ_GMK_51.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.Pusk_PAZ_GMK_51.Settings, FromHMI := PAZ_GVL.DGI.Pusk_PAZ_GMK_51.FromHMI, ToHMI := PAZ_GVL.DGI.Pusk_PAZ_GMK_51.ToHMI, my := PAZ_GVL.DGI.Pusk_PAZ_GMK_51.Intern, out := PAZ_GVL.DGI.Pusk_PAZ_GMK_51.PV);
// [A1.7:1] Запуск ПАЗ ГМК №52
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.Pusk_PAZ_GMK_52.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.Pusk_PAZ_GMK_52.Settings, FromHMI := PAZ_GVL.DGI.Pusk_PAZ_GMK_52.FromHMI, ToHMI := PAZ_GVL.DGI.Pusk_PAZ_GMK_52.ToHMI, my := PAZ_GVL.DGI.Pusk_PAZ_GMK_52.Intern, out := PAZ_GVL.DGI.Pusk_PAZ_GMK_52.PV);
// [A1.7:2] Съем звука
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.Sound_OF.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.Sound_OF.Settings, FromHMI := PAZ_GVL.DGI.Sound_OF.FromHMI, ToHMI := PAZ_GVL.DGI.Sound_OF.ToHMI, my := PAZ_GVL.DGI.Sound_OF.Intern, out := PAZ_GVL.DGI.Sound_OF.PV);
// [A1.7:3] Сигналы внутренней диагностики 1
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.SignVnDiag_1.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.SignVnDiag_1.Settings, FromHMI := PAZ_GVL.DGI.SignVnDiag_1.FromHMI, ToHMI := PAZ_GVL.DGI.SignVnDiag_1.ToHMI, my := PAZ_GVL.DGI.SignVnDiag_1.Intern, out := PAZ_GVL.DGI.SignVnDiag_1.PV);
// [A1.7:4] Сигналы внутренней диагностики 2
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.SignVnDiag_2.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.SignVnDiag_2.Settings, FromHMI := PAZ_GVL.DGI.SignVnDiag_2.FromHMI, ToHMI := PAZ_GVL.DGI.SignVnDiag_2.ToHMI, my := PAZ_GVL.DGI.SignVnDiag_2.Intern, out := PAZ_GVL.DGI.SignVnDiag_2.PV);
// [A1.7:5] Сигналы внутренней диагностики 3
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.SignVnDiag_3.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.SignVnDiag_3.Settings, FromHMI := PAZ_GVL.DGI.SignVnDiag_3.FromHMI, ToHMI := PAZ_GVL.DGI.SignVnDiag_3.ToHMI, my := PAZ_GVL.DGI.SignVnDiag_3.Intern, out := PAZ_GVL.DGI.SignVnDiag_3.PV);
// [A1.7:6] Сигналы внутренней диагностики 4
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.SignVnDiag_4.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.SignVnDiag_4.Settings, FromHMI := PAZ_GVL.DGI.SignVnDiag_4.FromHMI, ToHMI := PAZ_GVL.DGI.SignVnDiag_4.ToHMI, my := PAZ_GVL.DGI.SignVnDiag_4.Intern, out := PAZ_GVL.DGI.SignVnDiag_4.PV);
// [A1.7:7] Частота вращения коленчатого вала ГМК №44 (канал 2)
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.Fvkv_GMK_44_Ch_2.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.Fvkv_GMK_44_Ch_2.Settings, FromHMI := PAZ_GVL.DGI.Fvkv_GMK_44_Ch_2.FromHMI, ToHMI := PAZ_GVL.DGI.Fvkv_GMK_44_Ch_2.ToHMI, my := PAZ_GVL.DGI.Fvkv_GMK_44_Ch_2.Intern, out := PAZ_GVL.DGI.Fvkv_GMK_44_Ch_2.PV);
// [A1.7:8] Частота вращения коленчатого вала ГМК №45 (канал 2)
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.Fvkv_GMK_45_Ch_2.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.Fvkv_GMK_45_Ch_2.Settings, FromHMI := PAZ_GVL.DGI.Fvkv_GMK_45_Ch_2.FromHMI, ToHMI := PAZ_GVL.DGI.Fvkv_GMK_45_Ch_2.ToHMI, my := PAZ_GVL.DGI.Fvkv_GMK_45_Ch_2.Intern, out := PAZ_GVL.DGI.Fvkv_GMK_45_Ch_2.PV);
// [A1.7:9] Частота вращения коленчатого вала ГМК №46 (канал 2)
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.Fvkv_GMK_46_Ch_2.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.Fvkv_GMK_46_Ch_2.Settings, FromHMI := PAZ_GVL.DGI.Fvkv_GMK_46_Ch_2.FromHMI, ToHMI := PAZ_GVL.DGI.Fvkv_GMK_46_Ch_2.ToHMI, my := PAZ_GVL.DGI.Fvkv_GMK_46_Ch_2.Intern, out := PAZ_GVL.DGI.Fvkv_GMK_46_Ch_2.PV);
// [A1.7:10] Частота вращения коленчатого вала ГМК №47 (канал 2)
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.Fvkv_GMK_47_Ch_2.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.Fvkv_GMK_47_Ch_2.Settings, FromHMI := PAZ_GVL.DGI.Fvkv_GMK_47_Ch_2.FromHMI, ToHMI := PAZ_GVL.DGI.Fvkv_GMK_47_Ch_2.ToHMI, my := PAZ_GVL.DGI.Fvkv_GMK_47_Ch_2.Intern, out := PAZ_GVL.DGI.Fvkv_GMK_47_Ch_2.PV);
// [A1.7:11] Частота вращения коленчатого вала ГМК №48 (канал 2)
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.Fvkv_GMK_48_Ch_2.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.Fvkv_GMK_48_Ch_2.Settings, FromHMI := PAZ_GVL.DGI.Fvkv_GMK_48_Ch_2.FromHMI, ToHMI := PAZ_GVL.DGI.Fvkv_GMK_48_Ch_2.ToHMI, my := PAZ_GVL.DGI.Fvkv_GMK_48_Ch_2.Intern, out := PAZ_GVL.DGI.Fvkv_GMK_48_Ch_2.PV);
// [A1.7:12] Частота вращения коленчатого вала ГМК №51 (канал 2)
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.Fvkv_GMK_51_Ch_2.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.Fvkv_GMK_51_Ch_2.Settings, FromHMI := PAZ_GVL.DGI.Fvkv_GMK_51_Ch_2.FromHMI, ToHMI := PAZ_GVL.DGI.Fvkv_GMK_51_Ch_2.ToHMI, my := PAZ_GVL.DGI.Fvkv_GMK_51_Ch_2.Intern, out := PAZ_GVL.DGI.Fvkv_GMK_51_Ch_2.PV);
// [A1.7:13] Частота вращения коленчатого вала ГМК №52 (канал 2)
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.Fvkv_GMK_52_Ch_2.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.Fvkv_GMK_52_Ch_2.Settings, FromHMI := PAZ_GVL.DGI.Fvkv_GMK_52_Ch_2.FromHMI, ToHMI := PAZ_GVL.DGI.Fvkv_GMK_52_Ch_2.ToHMI, my := PAZ_GVL.DGI.Fvkv_GMK_52_Ch_2.Intern, out := PAZ_GVL.DGI.Fvkv_GMK_52_Ch_2.PV);
// [A1.7:14] Резерв
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.Reserv_6.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.Reserv_6.Settings, FromHMI := PAZ_GVL.DGI.Reserv_6.FromHMI, ToHMI := PAZ_GVL.DGI.Reserv_6.ToHMI, my := PAZ_GVL.DGI.Reserv_6.Intern, out := PAZ_GVL.DGI.Reserv_6.PV);
// [A1.7:15] Клапан ESDV9601.1 на приёме ГМК открыт
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.Kl_ESDV9601_1_ON.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.Kl_ESDV9601_1_ON.Settings, FromHMI := PAZ_GVL.DGI.Kl_ESDV9601_1_ON.FromHMI, ToHMI := PAZ_GVL.DGI.Kl_ESDV9601_1_ON.ToHMI, my := PAZ_GVL.DGI.Kl_ESDV9601_1_ON.Intern, out := PAZ_GVL.DGI.Kl_ESDV9601_1_ON.PV);
// [A1.7:16] Клапан ESDV9601.1 на приёме ГМК закрыт
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.Kl_ESDV9601_1_OF.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.Kl_ESDV9601_1_OF.Settings, FromHMI := PAZ_GVL.DGI.Kl_ESDV9601_1_OF.FromHMI, ToHMI := PAZ_GVL.DGI.Kl_ESDV9601_1_OF.ToHMI, my := PAZ_GVL.DGI.Kl_ESDV9601_1_OF.Intern, out := PAZ_GVL.DGI.Kl_ESDV9601_1_OF.PV);
// [A1.7:17] Клапан ESDV9602.1 на выходе ГМК открыт
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.Kl_ESDV9602_1_ON.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.Kl_ESDV9602_1_ON.Settings, FromHMI := PAZ_GVL.DGI.Kl_ESDV9602_1_ON.FromHMI, ToHMI := PAZ_GVL.DGI.Kl_ESDV9602_1_ON.ToHMI, my := PAZ_GVL.DGI.Kl_ESDV9602_1_ON.Intern, out := PAZ_GVL.DGI.Kl_ESDV9602_1_ON.PV);
// [A1.7:18] Клапан ESDV9602.1 на выходе ГМК закрыт
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.Kl_ESDV9602_1_OF.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.Kl_ESDV9602_1_OF.Settings, FromHMI := PAZ_GVL.DGI.Kl_ESDV9602_1_OF.FromHMI, ToHMI := PAZ_GVL.DGI.Kl_ESDV9602_1_OF.ToHMI, my := PAZ_GVL.DGI.Kl_ESDV9602_1_OF.Intern, out := PAZ_GVL.DGI.Kl_ESDV9602_1_OF.PV);
// [A1.7:19] Клапан ESDV9611.1 на топливной линии открыт
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.Kl_ESDV9611_1_ON.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.Kl_ESDV9611_1_ON.Settings, FromHMI := PAZ_GVL.DGI.Kl_ESDV9611_1_ON.FromHMI, ToHMI := PAZ_GVL.DGI.Kl_ESDV9611_1_ON.ToHMI, my := PAZ_GVL.DGI.Kl_ESDV9611_1_ON.Intern, out := PAZ_GVL.DGI.Kl_ESDV9611_1_ON.PV);
// [A1.7:20] Клапан ESDV9611.1 на топливной линии закрыт
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.Kl_ESDV9611_1_OF.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.Kl_ESDV9611_1_OF.Settings, FromHMI := PAZ_GVL.DGI.Kl_ESDV9611_1_OF.FromHMI, ToHMI := PAZ_GVL.DGI.Kl_ESDV9611_1_OF.ToHMI, my := PAZ_GVL.DGI.Kl_ESDV9611_1_OF.Intern, out := PAZ_GVL.DGI.Kl_ESDV9611_1_OF.PV);
// [A1.7:21] Клапан ESDV9601.2 на приёме ГМК открыт
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.Kl_ESDV9601_2_ON.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.Kl_ESDV9601_2_ON.Settings, FromHMI := PAZ_GVL.DGI.Kl_ESDV9601_2_ON.FromHMI, ToHMI := PAZ_GVL.DGI.Kl_ESDV9601_2_ON.ToHMI, my := PAZ_GVL.DGI.Kl_ESDV9601_2_ON.Intern, out := PAZ_GVL.DGI.Kl_ESDV9601_2_ON.PV);
// [A1.7:22] Клапан ESDV9601.2 на приёме ГМК закрыт
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.Kl_ESDV9601_2_OF.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.Kl_ESDV9601_2_OF.Settings, FromHMI := PAZ_GVL.DGI.Kl_ESDV9601_2_OF.FromHMI, ToHMI := PAZ_GVL.DGI.Kl_ESDV9601_2_OF.ToHMI, my := PAZ_GVL.DGI.Kl_ESDV9601_2_OF.Intern, out := PAZ_GVL.DGI.Kl_ESDV9601_2_OF.PV);
// [A1.7:23] Клапан ESDV9602.2 на выходе ГМК открыт
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.Kl_ESDV9602_2_ON.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.Kl_ESDV9602_2_ON.Settings, FromHMI := PAZ_GVL.DGI.Kl_ESDV9602_2_ON.FromHMI, ToHMI := PAZ_GVL.DGI.Kl_ESDV9602_2_ON.ToHMI, my := PAZ_GVL.DGI.Kl_ESDV9602_2_ON.Intern, out := PAZ_GVL.DGI.Kl_ESDV9602_2_ON.PV);
// [A1.7:24] Клапан ESDV9602.2 на выходе ГМК закрыт
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.Kl_ESDV9602_2_OF.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.Kl_ESDV9602_2_OF.Settings, FromHMI := PAZ_GVL.DGI.Kl_ESDV9602_2_OF.FromHMI, ToHMI := PAZ_GVL.DGI.Kl_ESDV9602_2_OF.ToHMI, my := PAZ_GVL.DGI.Kl_ESDV9602_2_OF.Intern, out := PAZ_GVL.DGI.Kl_ESDV9602_2_OF.PV);
// [A1.7:25] Клапан ESDV9611.2 на топливной линии открыт
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.Kl_ESDV9611_2_ON.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.Kl_ESDV9611_2_ON.Settings, FromHMI := PAZ_GVL.DGI.Kl_ESDV9611_2_ON.FromHMI, ToHMI := PAZ_GVL.DGI.Kl_ESDV9611_2_ON.ToHMI, my := PAZ_GVL.DGI.Kl_ESDV9611_2_ON.Intern, out := PAZ_GVL.DGI.Kl_ESDV9611_2_ON.PV);
// [A1.7:26] Клапан ESDV9611.2 на топливной линии закрыт
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.Kl_ESDV9611_2_OF.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.Kl_ESDV9611_2_OF.Settings, FromHMI := PAZ_GVL.DGI.Kl_ESDV9611_2_OF.FromHMI, ToHMI := PAZ_GVL.DGI.Kl_ESDV9611_2_OF.ToHMI, my := PAZ_GVL.DGI.Kl_ESDV9611_2_OF.Intern, out := PAZ_GVL.DGI.Kl_ESDV9611_2_OF.PV);
// [A1.7:27] Клапан ESDV9601.3 на приёме ГМК открыт
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.Kl_ESDV9601_3_ON.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.Kl_ESDV9601_3_ON.Settings, FromHMI := PAZ_GVL.DGI.Kl_ESDV9601_3_ON.FromHMI, ToHMI := PAZ_GVL.DGI.Kl_ESDV9601_3_ON.ToHMI, my := PAZ_GVL.DGI.Kl_ESDV9601_3_ON.Intern, out := PAZ_GVL.DGI.Kl_ESDV9601_3_ON.PV);
// [A1.7:28] Клапан ESDV9601.3 на приёме ГМК закрыт
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.Kl_ESDV9601_3_OF.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.Kl_ESDV9601_3_OF.Settings, FromHMI := PAZ_GVL.DGI.Kl_ESDV9601_3_OF.FromHMI, ToHMI := PAZ_GVL.DGI.Kl_ESDV9601_3_OF.ToHMI, my := PAZ_GVL.DGI.Kl_ESDV9601_3_OF.Intern, out := PAZ_GVL.DGI.Kl_ESDV9601_3_OF.PV);
// [A1.8:1] Клапан ESDV9602.3 на выходе ГМК открыт
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.Kl_ESDV9602_3_ON.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.Kl_ESDV9602_3_ON.Settings, FromHMI := PAZ_GVL.DGI.Kl_ESDV9602_3_ON.FromHMI, ToHMI := PAZ_GVL.DGI.Kl_ESDV9602_3_ON.ToHMI, my := PAZ_GVL.DGI.Kl_ESDV9602_3_ON.Intern, out := PAZ_GVL.DGI.Kl_ESDV9602_3_ON.PV);
// [A1.8:2] Клапан ESDV9602.3 на выходе ГМК закрыт
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.Kl_ESDV9602_3_OF.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.Kl_ESDV9602_3_OF.Settings, FromHMI := PAZ_GVL.DGI.Kl_ESDV9602_3_OF.FromHMI, ToHMI := PAZ_GVL.DGI.Kl_ESDV9602_3_OF.ToHMI, my := PAZ_GVL.DGI.Kl_ESDV9602_3_OF.Intern, out := PAZ_GVL.DGI.Kl_ESDV9602_3_OF.PV);
// [A1.8:3] Клапан ESDV9611.3 на топливной линии открыт
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.Kl_ESDV9611_3_ON.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.Kl_ESDV9611_3_ON.Settings, FromHMI := PAZ_GVL.DGI.Kl_ESDV9611_3_ON.FromHMI, ToHMI := PAZ_GVL.DGI.Kl_ESDV9611_3_ON.ToHMI, my := PAZ_GVL.DGI.Kl_ESDV9611_3_ON.Intern, out := PAZ_GVL.DGI.Kl_ESDV9611_3_ON.PV);
// [A1.8:4] Клапан ESDV9611.3 на топливной линии закрыт
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.Kl_ESDV9611_3_OF.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.Kl_ESDV9611_3_OF.Settings, FromHMI := PAZ_GVL.DGI.Kl_ESDV9611_3_OF.FromHMI, ToHMI := PAZ_GVL.DGI.Kl_ESDV9611_3_OF.ToHMI, my := PAZ_GVL.DGI.Kl_ESDV9611_3_OF.Intern, out := PAZ_GVL.DGI.Kl_ESDV9611_3_OF.PV);
// [A1.8:5] Клапан ESDV9601.4 на приёме ГМК открыт
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.Kl_ESDV9601_4_ON.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.Kl_ESDV9601_4_ON.Settings, FromHMI := PAZ_GVL.DGI.Kl_ESDV9601_4_ON.FromHMI, ToHMI := PAZ_GVL.DGI.Kl_ESDV9601_4_ON.ToHMI, my := PAZ_GVL.DGI.Kl_ESDV9601_4_ON.Intern, out := PAZ_GVL.DGI.Kl_ESDV9601_4_ON.PV);
// [A1.8:6] Клапан ESDV9601.4 на приёме ГМК закрыт
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.Kl_ESDV9601_4_OF.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.Kl_ESDV9601_4_OF.Settings, FromHMI := PAZ_GVL.DGI.Kl_ESDV9601_4_OF.FromHMI, ToHMI := PAZ_GVL.DGI.Kl_ESDV9601_4_OF.ToHMI, my := PAZ_GVL.DGI.Kl_ESDV9601_4_OF.Intern, out := PAZ_GVL.DGI.Kl_ESDV9601_4_OF.PV);
// [A1.8:7] Клапан ESDV9602.4 на выходе ГМК открыт
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.Kl_ESDV9602_4_ON.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.Kl_ESDV9602_4_ON.Settings, FromHMI := PAZ_GVL.DGI.Kl_ESDV9602_4_ON.FromHMI, ToHMI := PAZ_GVL.DGI.Kl_ESDV9602_4_ON.ToHMI, my := PAZ_GVL.DGI.Kl_ESDV9602_4_ON.Intern, out := PAZ_GVL.DGI.Kl_ESDV9602_4_ON.PV);
// [A1.8:8] Клапан ESDV9602.4 на выходе ГМК закрыт
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.Kl_ESDV9602_4_OF.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.Kl_ESDV9602_4_OF.Settings, FromHMI := PAZ_GVL.DGI.Kl_ESDV9602_4_OF.FromHMI, ToHMI := PAZ_GVL.DGI.Kl_ESDV9602_4_OF.ToHMI, my := PAZ_GVL.DGI.Kl_ESDV9602_4_OF.Intern, out := PAZ_GVL.DGI.Kl_ESDV9602_4_OF.PV);
// [A1.8:9] Клапан ESDV9611.4 на топливной линии открыт
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.Kl_ESDV9611_4_ON.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.Kl_ESDV9611_4_ON.Settings, FromHMI := PAZ_GVL.DGI.Kl_ESDV9611_4_ON.FromHMI, ToHMI := PAZ_GVL.DGI.Kl_ESDV9611_4_ON.ToHMI, my := PAZ_GVL.DGI.Kl_ESDV9611_4_ON.Intern, out := PAZ_GVL.DGI.Kl_ESDV9611_4_ON.PV);
// [A1.8:10] Клапан ESDV9611.4 на топливной линии закрыт
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.Kl_ESDV9611_4_OF.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.Kl_ESDV9611_4_OF.Settings, FromHMI := PAZ_GVL.DGI.Kl_ESDV9611_4_OF.FromHMI, ToHMI := PAZ_GVL.DGI.Kl_ESDV9611_4_OF.ToHMI, my := PAZ_GVL.DGI.Kl_ESDV9611_4_OF.Intern, out := PAZ_GVL.DGI.Kl_ESDV9611_4_OF.PV);
// [A1.8:11] Клапан ESDV9601.5 на приёме ГМК открыт
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.Kl_ESDV9601_5_ON.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.Kl_ESDV9601_5_ON.Settings, FromHMI := PAZ_GVL.DGI.Kl_ESDV9601_5_ON.FromHMI, ToHMI := PAZ_GVL.DGI.Kl_ESDV9601_5_ON.ToHMI, my := PAZ_GVL.DGI.Kl_ESDV9601_5_ON.Intern, out := PAZ_GVL.DGI.Kl_ESDV9601_5_ON.PV);
// [A1.8:12] Клапан ESDV9601.5 на приёме ГМК закрыт
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.Kl_ESDV9601_5_OF.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.Kl_ESDV9601_5_OF.Settings, FromHMI := PAZ_GVL.DGI.Kl_ESDV9601_5_OF.FromHMI, ToHMI := PAZ_GVL.DGI.Kl_ESDV9601_5_OF.ToHMI, my := PAZ_GVL.DGI.Kl_ESDV9601_5_OF.Intern, out := PAZ_GVL.DGI.Kl_ESDV9601_5_OF.PV);
// [A1.8:13] Клапан ESDV9602.5 на выходе ГМК открыт
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.Kl_ESDV9602_5_ON.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.Kl_ESDV9602_5_ON.Settings, FromHMI := PAZ_GVL.DGI.Kl_ESDV9602_5_ON.FromHMI, ToHMI := PAZ_GVL.DGI.Kl_ESDV9602_5_ON.ToHMI, my := PAZ_GVL.DGI.Kl_ESDV9602_5_ON.Intern, out := PAZ_GVL.DGI.Kl_ESDV9602_5_ON.PV);
// [A1.8:14] Клапан ESDV9602.5 на выходе ГМК закрыт
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.Kl_ESDV9602_5_OF.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.Kl_ESDV9602_5_OF.Settings, FromHMI := PAZ_GVL.DGI.Kl_ESDV9602_5_OF.FromHMI, ToHMI := PAZ_GVL.DGI.Kl_ESDV9602_5_OF.ToHMI, my := PAZ_GVL.DGI.Kl_ESDV9602_5_OF.Intern, out := PAZ_GVL.DGI.Kl_ESDV9602_5_OF.PV);
// [A1.8:15] Клапан ESDV9611.5 на топливной линии открыт
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.Kl_ESDV9611_5_ON.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.Kl_ESDV9611_5_ON.Settings, FromHMI := PAZ_GVL.DGI.Kl_ESDV9611_5_ON.FromHMI, ToHMI := PAZ_GVL.DGI.Kl_ESDV9611_5_ON.ToHMI, my := PAZ_GVL.DGI.Kl_ESDV9611_5_ON.Intern, out := PAZ_GVL.DGI.Kl_ESDV9611_5_ON.PV);
// [A1.8:16] Клапан ESDV9611.5 на топливной линии закрыт
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.Kl_ESDV9611_5_OF.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.Kl_ESDV9611_5_OF.Settings, FromHMI := PAZ_GVL.DGI.Kl_ESDV9611_5_OF.FromHMI, ToHMI := PAZ_GVL.DGI.Kl_ESDV9611_5_OF.ToHMI, my := PAZ_GVL.DGI.Kl_ESDV9611_5_OF.Intern, out := PAZ_GVL.DGI.Kl_ESDV9611_5_OF.PV);
// [A1.8:17] Клапан ESDV9601.6 на приёме ГМК открыт
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.Kl_ESDV9601_6_ON.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.Kl_ESDV9601_6_ON.Settings, FromHMI := PAZ_GVL.DGI.Kl_ESDV9601_6_ON.FromHMI, ToHMI := PAZ_GVL.DGI.Kl_ESDV9601_6_ON.ToHMI, my := PAZ_GVL.DGI.Kl_ESDV9601_6_ON.Intern, out := PAZ_GVL.DGI.Kl_ESDV9601_6_ON.PV);
// [A1.8:18] Клапан ESDV9601.6 на приёме ГМК закрыт
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.Kl_ESDV9601_6_OF.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.Kl_ESDV9601_6_OF.Settings, FromHMI := PAZ_GVL.DGI.Kl_ESDV9601_6_OF.FromHMI, ToHMI := PAZ_GVL.DGI.Kl_ESDV9601_6_OF.ToHMI, my := PAZ_GVL.DGI.Kl_ESDV9601_6_OF.Intern, out := PAZ_GVL.DGI.Kl_ESDV9601_6_OF.PV);
// [A1.8:19] Клапан ESDV9602.6 на выходе ГМК открыт
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.Kl_ESDV9602_6_ON.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.Kl_ESDV9602_6_ON.Settings, FromHMI := PAZ_GVL.DGI.Kl_ESDV9602_6_ON.FromHMI, ToHMI := PAZ_GVL.DGI.Kl_ESDV9602_6_ON.ToHMI, my := PAZ_GVL.DGI.Kl_ESDV9602_6_ON.Intern, out := PAZ_GVL.DGI.Kl_ESDV9602_6_ON.PV);
// [A1.8:20] Клапан ESDV9602.6 на выходе ГМК закрыт
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.Kl_ESDV9602_6_OF.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.Kl_ESDV9602_6_OF.Settings, FromHMI := PAZ_GVL.DGI.Kl_ESDV9602_6_OF.FromHMI, ToHMI := PAZ_GVL.DGI.Kl_ESDV9602_6_OF.ToHMI, my := PAZ_GVL.DGI.Kl_ESDV9602_6_OF.Intern, out := PAZ_GVL.DGI.Kl_ESDV9602_6_OF.PV);
// [A1.8:21] Клапан ESDV9611.6 на топливной линии открыт
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.Kl_ESDV9611_6_ON.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.Kl_ESDV9611_6_ON.Settings, FromHMI := PAZ_GVL.DGI.Kl_ESDV9611_6_ON.FromHMI, ToHMI := PAZ_GVL.DGI.Kl_ESDV9611_6_ON.ToHMI, my := PAZ_GVL.DGI.Kl_ESDV9611_6_ON.Intern, out := PAZ_GVL.DGI.Kl_ESDV9611_6_ON.PV);
// [A1.8:22] Клапан ESDV9611.6 на топливной линии закрыт
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.Kl_ESDV9611_6_OF.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.Kl_ESDV9611_6_OF.Settings, FromHMI := PAZ_GVL.DGI.Kl_ESDV9611_6_OF.FromHMI, ToHMI := PAZ_GVL.DGI.Kl_ESDV9611_6_OF.ToHMI, my := PAZ_GVL.DGI.Kl_ESDV9611_6_OF.Intern, out := PAZ_GVL.DGI.Kl_ESDV9611_6_OF.PV);
// [A1.8:23] Клапан ESDV9601.7 на приёме ГМК открыт
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.Kl_ESDV9601_7_ON.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.Kl_ESDV9601_7_ON.Settings, FromHMI := PAZ_GVL.DGI.Kl_ESDV9601_7_ON.FromHMI, ToHMI := PAZ_GVL.DGI.Kl_ESDV9601_7_ON.ToHMI, my := PAZ_GVL.DGI.Kl_ESDV9601_7_ON.Intern, out := PAZ_GVL.DGI.Kl_ESDV9601_7_ON.PV);
// [A1.8:24] Клапан ESDV9601.7 на приёме ГМК закрыт
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.Kl_ESDV9601_7_OF.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.Kl_ESDV9601_7_OF.Settings, FromHMI := PAZ_GVL.DGI.Kl_ESDV9601_7_OF.FromHMI, ToHMI := PAZ_GVL.DGI.Kl_ESDV9601_7_OF.ToHMI, my := PAZ_GVL.DGI.Kl_ESDV9601_7_OF.Intern, out := PAZ_GVL.DGI.Kl_ESDV9601_7_OF.PV);
// [A1.8:25] Клапан ESDV9602.7 на выходе ГМК открыт
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.Kl_ESDV9602_7_ON.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.Kl_ESDV9602_7_ON.Settings, FromHMI := PAZ_GVL.DGI.Kl_ESDV9602_7_ON.FromHMI, ToHMI := PAZ_GVL.DGI.Kl_ESDV9602_7_ON.ToHMI, my := PAZ_GVL.DGI.Kl_ESDV9602_7_ON.Intern, out := PAZ_GVL.DGI.Kl_ESDV9602_7_ON.PV);
// [A1.8:26] Клапан ESDV9602.7 на выходе ГМК закрыт
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.Kl_ESDV9602_7_OF.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.Kl_ESDV9602_7_OF.Settings, FromHMI := PAZ_GVL.DGI.Kl_ESDV9602_7_OF.FromHMI, ToHMI := PAZ_GVL.DGI.Kl_ESDV9602_7_OF.ToHMI, my := PAZ_GVL.DGI.Kl_ESDV9602_7_OF.Intern, out := PAZ_GVL.DGI.Kl_ESDV9602_7_OF.PV);
// [A1.8:27] Клапан ESDV9611.7 на топливной линии открыт
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.Kl_ESDV9611_7_ON.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.Kl_ESDV9611_7_ON.Settings, FromHMI := PAZ_GVL.DGI.Kl_ESDV9611_7_ON.FromHMI, ToHMI := PAZ_GVL.DGI.Kl_ESDV9611_7_ON.ToHMI, my := PAZ_GVL.DGI.Kl_ESDV9611_7_ON.Intern, out := PAZ_GVL.DGI.Kl_ESDV9611_7_ON.PV);
// [A1.8:28] Клапан ESDV9611.7 на топливной линии закрыт
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.Kl_ESDV9611_7_OF.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.Kl_ESDV9611_7_OF.Settings, FromHMI := PAZ_GVL.DGI.Kl_ESDV9611_7_OF.FromHMI, ToHMI := PAZ_GVL.DGI.Kl_ESDV9611_7_OF.ToHMI, my := PAZ_GVL.DGI.Kl_ESDV9611_7_OF.Intern, out := PAZ_GVL.DGI.Kl_ESDV9611_7_OF.PV);
// [A1.9:1] Аварийный останов ГМК №44 (от АСУ ТП КУОГ)
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.AO_GMK_44_ot_ASUTP_KUOG.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.AO_GMK_44_ot_ASUTP_KUOG.Settings, FromHMI := PAZ_GVL.DGI.AO_GMK_44_ot_ASUTP_KUOG.FromHMI, ToHMI := PAZ_GVL.DGI.AO_GMK_44_ot_ASUTP_KUOG.ToHMI, my := PAZ_GVL.DGI.AO_GMK_44_ot_ASUTP_KUOG.Intern, out := PAZ_GVL.DGI.AO_GMK_44_ot_ASUTP_KUOG.PV);
// [A1.9:2] Кнопка АО на агрегате №44
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.Btn_AO_na_Agr_44.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.Btn_AO_na_Agr_44.Settings, FromHMI := PAZ_GVL.DGI.Btn_AO_na_Agr_44.FromHMI, ToHMI := PAZ_GVL.DGI.Btn_AO_na_Agr_44.ToHMI, my := PAZ_GVL.DGI.Btn_AO_na_Agr_44.Intern, out := PAZ_GVL.DGI.Btn_AO_na_Agr_44.PV);
// [A1.9:3] Кнопка АО на агрегате №44 (2)
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.Btn_AO_na_Agr_44_2.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.Btn_AO_na_Agr_44_2.Settings, FromHMI := PAZ_GVL.DGI.Btn_AO_na_Agr_44_2.FromHMI, ToHMI := PAZ_GVL.DGI.Btn_AO_na_Agr_44_2.ToHMI, my := PAZ_GVL.DGI.Btn_AO_na_Agr_44_2.Intern, out := PAZ_GVL.DGI.Btn_AO_na_Agr_44_2.PV);
// [A1.9:4] Аварийный останов ГМК №45 (от АСУ ТП КУОГ)
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.AO_GMK_45_ot_ASUTP_KUOG.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.AO_GMK_45_ot_ASUTP_KUOG.Settings, FromHMI := PAZ_GVL.DGI.AO_GMK_45_ot_ASUTP_KUOG.FromHMI, ToHMI := PAZ_GVL.DGI.AO_GMK_45_ot_ASUTP_KUOG.ToHMI, my := PAZ_GVL.DGI.AO_GMK_45_ot_ASUTP_KUOG.Intern, out := PAZ_GVL.DGI.AO_GMK_45_ot_ASUTP_KUOG.PV);
// [A1.9:5] Кнопка АО на агрегате №45
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.Btn_AO_na_Agr_45.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.Btn_AO_na_Agr_45.Settings, FromHMI := PAZ_GVL.DGI.Btn_AO_na_Agr_45.FromHMI, ToHMI := PAZ_GVL.DGI.Btn_AO_na_Agr_45.ToHMI, my := PAZ_GVL.DGI.Btn_AO_na_Agr_45.Intern, out := PAZ_GVL.DGI.Btn_AO_na_Agr_45.PV);
// [A1.9:6] Кнопка АО на агрегате №45 (2)
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.Btn_AO_na_Agr_45_2.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.Btn_AO_na_Agr_45_2.Settings, FromHMI := PAZ_GVL.DGI.Btn_AO_na_Agr_45_2.FromHMI, ToHMI := PAZ_GVL.DGI.Btn_AO_na_Agr_45_2.ToHMI, my := PAZ_GVL.DGI.Btn_AO_na_Agr_45_2.Intern, out := PAZ_GVL.DGI.Btn_AO_na_Agr_45_2.PV);
// [A1.9:7] Аварийный останов ГМК №46 (от АСУ ТП КУОГ)
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.AO_GMK_46_ot_ASUTP_KUOG.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.AO_GMK_46_ot_ASUTP_KUOG.Settings, FromHMI := PAZ_GVL.DGI.AO_GMK_46_ot_ASUTP_KUOG.FromHMI, ToHMI := PAZ_GVL.DGI.AO_GMK_46_ot_ASUTP_KUOG.ToHMI, my := PAZ_GVL.DGI.AO_GMK_46_ot_ASUTP_KUOG.Intern, out := PAZ_GVL.DGI.AO_GMK_46_ot_ASUTP_KUOG.PV);
// [A1.9:8] Кнопка АО на агрегате №46
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.Btn_AO_na_Agr_46.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.Btn_AO_na_Agr_46.Settings, FromHMI := PAZ_GVL.DGI.Btn_AO_na_Agr_46.FromHMI, ToHMI := PAZ_GVL.DGI.Btn_AO_na_Agr_46.ToHMI, my := PAZ_GVL.DGI.Btn_AO_na_Agr_46.Intern, out := PAZ_GVL.DGI.Btn_AO_na_Agr_46.PV);
// [A1.9:9] Кнопка АО на агрегате №46 (2)
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.Btn_AO_na_Agr_46_2.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.Btn_AO_na_Agr_46_2.Settings, FromHMI := PAZ_GVL.DGI.Btn_AO_na_Agr_46_2.FromHMI, ToHMI := PAZ_GVL.DGI.Btn_AO_na_Agr_46_2.ToHMI, my := PAZ_GVL.DGI.Btn_AO_na_Agr_46_2.Intern, out := PAZ_GVL.DGI.Btn_AO_na_Agr_46_2.PV);
// [A1.9:10] Аварийный останов ГМК №47 (от АСУ ТП КУОГ)
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.AO_GMK_47_ot_ASUTP_KUOG.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.AO_GMK_47_ot_ASUTP_KUOG.Settings, FromHMI := PAZ_GVL.DGI.AO_GMK_47_ot_ASUTP_KUOG.FromHMI, ToHMI := PAZ_GVL.DGI.AO_GMK_47_ot_ASUTP_KUOG.ToHMI, my := PAZ_GVL.DGI.AO_GMK_47_ot_ASUTP_KUOG.Intern, out := PAZ_GVL.DGI.AO_GMK_47_ot_ASUTP_KUOG.PV);
// [A1.9:11] Кнопка АО на агрегате №47
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.Btn_AO_na_Agr_47.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.Btn_AO_na_Agr_47.Settings, FromHMI := PAZ_GVL.DGI.Btn_AO_na_Agr_47.FromHMI, ToHMI := PAZ_GVL.DGI.Btn_AO_na_Agr_47.ToHMI, my := PAZ_GVL.DGI.Btn_AO_na_Agr_47.Intern, out := PAZ_GVL.DGI.Btn_AO_na_Agr_47.PV);
// [A1.9:12] Кнопка АО на агрегате №47 (2)
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.Btn_AO_na_Agr_47_2.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.Btn_AO_na_Agr_47_2.Settings, FromHMI := PAZ_GVL.DGI.Btn_AO_na_Agr_47_2.FromHMI, ToHMI := PAZ_GVL.DGI.Btn_AO_na_Agr_47_2.ToHMI, my := PAZ_GVL.DGI.Btn_AO_na_Agr_47_2.Intern, out := PAZ_GVL.DGI.Btn_AO_na_Agr_47_2.PV);
// [A1.9:13] Аварийный останов ГМК №48 (от АСУ ТП КУОГ)
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.AO_GMK_48_ot_ASUTP_KUOG.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.AO_GMK_48_ot_ASUTP_KUOG.Settings, FromHMI := PAZ_GVL.DGI.AO_GMK_48_ot_ASUTP_KUOG.FromHMI, ToHMI := PAZ_GVL.DGI.AO_GMK_48_ot_ASUTP_KUOG.ToHMI, my := PAZ_GVL.DGI.AO_GMK_48_ot_ASUTP_KUOG.Intern, out := PAZ_GVL.DGI.AO_GMK_48_ot_ASUTP_KUOG.PV);
// [A1.9:14] Кнопка АО на агрегате №48
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.Btn_AO_na_Agr_48.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.Btn_AO_na_Agr_48.Settings, FromHMI := PAZ_GVL.DGI.Btn_AO_na_Agr_48.FromHMI, ToHMI := PAZ_GVL.DGI.Btn_AO_na_Agr_48.ToHMI, my := PAZ_GVL.DGI.Btn_AO_na_Agr_48.Intern, out := PAZ_GVL.DGI.Btn_AO_na_Agr_48.PV);
// [A1.9:15] Кнопка АО на агрегате №48 (2)
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.Btn_AO_na_Agr_48_2.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.Btn_AO_na_Agr_48_2.Settings, FromHMI := PAZ_GVL.DGI.Btn_AO_na_Agr_48_2.FromHMI, ToHMI := PAZ_GVL.DGI.Btn_AO_na_Agr_48_2.ToHMI, my := PAZ_GVL.DGI.Btn_AO_na_Agr_48_2.Intern, out := PAZ_GVL.DGI.Btn_AO_na_Agr_48_2.PV);
// [A1.9:16] Аварийный останов ГМК №51 (от АСУ ТП КУОГ)
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.AO_GMK_51_ot_ASUTP_KUOG.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.AO_GMK_51_ot_ASUTP_KUOG.Settings, FromHMI := PAZ_GVL.DGI.AO_GMK_51_ot_ASUTP_KUOG.FromHMI, ToHMI := PAZ_GVL.DGI.AO_GMK_51_ot_ASUTP_KUOG.ToHMI, my := PAZ_GVL.DGI.AO_GMK_51_ot_ASUTP_KUOG.Intern, out := PAZ_GVL.DGI.AO_GMK_51_ot_ASUTP_KUOG.PV);
// [A1.9:17] Кнопка АО на агрегате №51
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.Btn_AO_na_Agr_51.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.Btn_AO_na_Agr_51.Settings, FromHMI := PAZ_GVL.DGI.Btn_AO_na_Agr_51.FromHMI, ToHMI := PAZ_GVL.DGI.Btn_AO_na_Agr_51.ToHMI, my := PAZ_GVL.DGI.Btn_AO_na_Agr_51.Intern, out := PAZ_GVL.DGI.Btn_AO_na_Agr_51.PV);
// [A1.9:18] Кнопка АО на агрегате №51 (2)
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.Btn_AO_na_Agr_51_2.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.Btn_AO_na_Agr_51_2.Settings, FromHMI := PAZ_GVL.DGI.Btn_AO_na_Agr_51_2.FromHMI, ToHMI := PAZ_GVL.DGI.Btn_AO_na_Agr_51_2.ToHMI, my := PAZ_GVL.DGI.Btn_AO_na_Agr_51_2.Intern, out := PAZ_GVL.DGI.Btn_AO_na_Agr_51_2.PV);
// [A1.9:19] Аварийный останов ГМК №52 (от АСУ ТП КУОГ)
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.AO_GMK_52_ot_ASUTP_KUOG.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.AO_GMK_52_ot_ASUTP_KUOG.Settings, FromHMI := PAZ_GVL.DGI.AO_GMK_52_ot_ASUTP_KUOG.FromHMI, ToHMI := PAZ_GVL.DGI.AO_GMK_52_ot_ASUTP_KUOG.ToHMI, my := PAZ_GVL.DGI.AO_GMK_52_ot_ASUTP_KUOG.Intern, out := PAZ_GVL.DGI.AO_GMK_52_ot_ASUTP_KUOG.PV);
// [A1.9:20] Кнопка АО на агрегате №52
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.Btn_AO_na_Agr_52.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.Btn_AO_na_Agr_52.Settings, FromHMI := PAZ_GVL.DGI.Btn_AO_na_Agr_52.FromHMI, ToHMI := PAZ_GVL.DGI.Btn_AO_na_Agr_52.ToHMI, my := PAZ_GVL.DGI.Btn_AO_na_Agr_52.Intern, out := PAZ_GVL.DGI.Btn_AO_na_Agr_52.PV);
// [A1.9:21] Кнопка АО на агрегате №52 (2)
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.Btn_AO_na_Agr_52_2.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.Btn_AO_na_Agr_52_2.Settings, FromHMI := PAZ_GVL.DGI.Btn_AO_na_Agr_52_2.FromHMI, ToHMI := PAZ_GVL.DGI.Btn_AO_na_Agr_52_2.ToHMI, my := PAZ_GVL.DGI.Btn_AO_na_Agr_52_2.Intern, out := PAZ_GVL.DGI.Btn_AO_na_Agr_52_2.PV);
// [A1.9:22] Резерв
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.Reserv_7.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.Reserv_7.Settings, FromHMI := PAZ_GVL.DGI.Reserv_7.FromHMI, ToHMI := PAZ_GVL.DGI.Reserv_7.ToHMI, my := PAZ_GVL.DGI.Reserv_7.Intern, out := PAZ_GVL.DGI.Reserv_7.PV);
// [A1.9:23] Резерв
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.Reserv_8.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.Reserv_8.Settings, FromHMI := PAZ_GVL.DGI.Reserv_8.FromHMI, ToHMI := PAZ_GVL.DGI.Reserv_8.ToHMI, my := PAZ_GVL.DGI.Reserv_8.Intern, out := PAZ_GVL.DGI.Reserv_8.PV);
// [A1.9:24] Резерв
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.Reserv_9.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.Reserv_9.Settings, FromHMI := PAZ_GVL.DGI.Reserv_9.FromHMI, ToHMI := PAZ_GVL.DGI.Reserv_9.ToHMI, my := PAZ_GVL.DGI.Reserv_9.Intern, out := PAZ_GVL.DGI.Reserv_9.PV);
// [A1.9:25] Резерв
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.Reserv_10.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.Reserv_10.Settings, FromHMI := PAZ_GVL.DGI.Reserv_10.FromHMI, ToHMI := PAZ_GVL.DGI.Reserv_10.ToHMI, my := PAZ_GVL.DGI.Reserv_10.Intern, out := PAZ_GVL.DGI.Reserv_10.PV);
// [A1.9:26] Резерв
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.Reserv_11.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.Reserv_11.Settings, FromHMI := PAZ_GVL.DGI.Reserv_11.FromHMI, ToHMI := PAZ_GVL.DGI.Reserv_11.ToHMI, my := PAZ_GVL.DGI.Reserv_11.Intern, out := PAZ_GVL.DGI.Reserv_11.PV);
// [A1.9:27] Резерв
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.Reserv_12.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.Reserv_12.Settings, FromHMI := PAZ_GVL.DGI.Reserv_12.FromHMI, ToHMI := PAZ_GVL.DGI.Reserv_12.ToHMI, my := PAZ_GVL.DGI.Reserv_12.Intern, out := PAZ_GVL.DGI.Reserv_12.PV);
// [A1.9:28] Резерв
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.Reserv_13.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.Reserv_13.Settings, FromHMI := PAZ_GVL.DGI.Reserv_13.FromHMI, ToHMI := PAZ_GVL.DGI.Reserv_13.ToHMI, my := PAZ_GVL.DGI.Reserv_13.Intern, out := PAZ_GVL.DGI.Reserv_13.PV);
// [A1.10:1] Разрешение на внесение изменений (2)
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.RazrVnesIzm_2.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.RazrVnesIzm_2.Settings, FromHMI := PAZ_GVL.DGI.RazrVnesIzm_2.FromHMI, ToHMI := PAZ_GVL.DGI.RazrVnesIzm_2.ToHMI, my := PAZ_GVL.DGI.RazrVnesIzm_2.Intern, out := PAZ_GVL.DGI.RazrVnesIzm_2.PV);
// [A1.10:2] Блокировка ПАЗ ГМК №44 (2)
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.Block_PAZ_GMK_44_2.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.Block_PAZ_GMK_44_2.Settings, FromHMI := PAZ_GVL.DGI.Block_PAZ_GMK_44_2.FromHMI, ToHMI := PAZ_GVL.DGI.Block_PAZ_GMK_44_2.ToHMI, my := PAZ_GVL.DGI.Block_PAZ_GMK_44_2.Intern, out := PAZ_GVL.DGI.Block_PAZ_GMK_44_2.PV);
// [A1.10:3] Блокировка ПАЗ ГМК №45 (2)
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.Block_PAZ_GMK_45_2.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.Block_PAZ_GMK_45_2.Settings, FromHMI := PAZ_GVL.DGI.Block_PAZ_GMK_45_2.FromHMI, ToHMI := PAZ_GVL.DGI.Block_PAZ_GMK_45_2.ToHMI, my := PAZ_GVL.DGI.Block_PAZ_GMK_45_2.Intern, out := PAZ_GVL.DGI.Block_PAZ_GMK_45_2.PV);
// [A1.10:4] Блокировка ПАЗ ГМК №46 (2)
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.Block_PAZ_GMK_46_2.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.Block_PAZ_GMK_46_2.Settings, FromHMI := PAZ_GVL.DGI.Block_PAZ_GMK_46_2.FromHMI, ToHMI := PAZ_GVL.DGI.Block_PAZ_GMK_46_2.ToHMI, my := PAZ_GVL.DGI.Block_PAZ_GMK_46_2.Intern, out := PAZ_GVL.DGI.Block_PAZ_GMK_46_2.PV);
// [A1.10:5] Блокировка ПАЗ ГМК №47 (2)
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.Block_PAZ_GMK_47_2.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.Block_PAZ_GMK_47_2.Settings, FromHMI := PAZ_GVL.DGI.Block_PAZ_GMK_47_2.FromHMI, ToHMI := PAZ_GVL.DGI.Block_PAZ_GMK_47_2.ToHMI, my := PAZ_GVL.DGI.Block_PAZ_GMK_47_2.Intern, out := PAZ_GVL.DGI.Block_PAZ_GMK_47_2.PV);
// [A1.10:6] Блокировка ПАЗ ГМК №48 (2)
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.Block_PAZ_GMK_48_2.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.Block_PAZ_GMK_48_2.Settings, FromHMI := PAZ_GVL.DGI.Block_PAZ_GMK_48_2.FromHMI, ToHMI := PAZ_GVL.DGI.Block_PAZ_GMK_48_2.ToHMI, my := PAZ_GVL.DGI.Block_PAZ_GMK_48_2.Intern, out := PAZ_GVL.DGI.Block_PAZ_GMK_48_2.PV);
// [A1.10:7] Блокировка ПАЗ ГМК №51 (2)
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.Block_PAZ_GMK_51_2.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.Block_PAZ_GMK_51_2.Settings, FromHMI := PAZ_GVL.DGI.Block_PAZ_GMK_51_2.FromHMI, ToHMI := PAZ_GVL.DGI.Block_PAZ_GMK_51_2.ToHMI, my := PAZ_GVL.DGI.Block_PAZ_GMK_51_2.Intern, out := PAZ_GVL.DGI.Block_PAZ_GMK_51_2.PV);
// [A1.10:8] Блокировка ПАЗ ГМК №52 (2)
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.Block_PAZ_GMK_52_2.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.Block_PAZ_GMK_52_2.Settings, FromHMI := PAZ_GVL.DGI.Block_PAZ_GMK_52_2.FromHMI, ToHMI := PAZ_GVL.DGI.Block_PAZ_GMK_52_2.ToHMI, my := PAZ_GVL.DGI.Block_PAZ_GMK_52_2.Intern, out := PAZ_GVL.DGI.Block_PAZ_GMK_52_2.PV);
// [A1.10:9] Ввод резервного  ПЛК (2)
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.Vvod_Reserv_PLC_2.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.Vvod_Reserv_PLC_2.Settings, FromHMI := PAZ_GVL.DGI.Vvod_Reserv_PLC_2.FromHMI, ToHMI := PAZ_GVL.DGI.Vvod_Reserv_PLC_2.ToHMI, my := PAZ_GVL.DGI.Vvod_Reserv_PLC_2.Intern, out := PAZ_GVL.DGI.Vvod_Reserv_PLC_2.PV);
// [A1.10:10] Запуск ПАЗ ГМК №44 (2)
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.Pusk_PAZ_GMK_44_2.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.Pusk_PAZ_GMK_44_2.Settings, FromHMI := PAZ_GVL.DGI.Pusk_PAZ_GMK_44_2.FromHMI, ToHMI := PAZ_GVL.DGI.Pusk_PAZ_GMK_44_2.ToHMI, my := PAZ_GVL.DGI.Pusk_PAZ_GMK_44_2.Intern, out := PAZ_GVL.DGI.Pusk_PAZ_GMK_44_2.PV);
// [A1.10:11] Запуск ПАЗ ГМК №45 (2)
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.Pusk_PAZ_GMK_45_2.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.Pusk_PAZ_GMK_45_2.Settings, FromHMI := PAZ_GVL.DGI.Pusk_PAZ_GMK_45_2.FromHMI, ToHMI := PAZ_GVL.DGI.Pusk_PAZ_GMK_45_2.ToHMI, my := PAZ_GVL.DGI.Pusk_PAZ_GMK_45_2.Intern, out := PAZ_GVL.DGI.Pusk_PAZ_GMK_45_2.PV);
// [A1.10:12] Запуск ПАЗ ГМК №46 (2)
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.Pusk_PAZ_GMK_46_2.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.Pusk_PAZ_GMK_46_2.Settings, FromHMI := PAZ_GVL.DGI.Pusk_PAZ_GMK_46_2.FromHMI, ToHMI := PAZ_GVL.DGI.Pusk_PAZ_GMK_46_2.ToHMI, my := PAZ_GVL.DGI.Pusk_PAZ_GMK_46_2.Intern, out := PAZ_GVL.DGI.Pusk_PAZ_GMK_46_2.PV);
// [A1.10:13] Запуск ПАЗ ГМК №47 (2)
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.Pusk_PAZ_GMK_47_2.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.Pusk_PAZ_GMK_47_2.Settings, FromHMI := PAZ_GVL.DGI.Pusk_PAZ_GMK_47_2.FromHMI, ToHMI := PAZ_GVL.DGI.Pusk_PAZ_GMK_47_2.ToHMI, my := PAZ_GVL.DGI.Pusk_PAZ_GMK_47_2.Intern, out := PAZ_GVL.DGI.Pusk_PAZ_GMK_47_2.PV);
// [A1.10:14] Запуск ПАЗ ГМК №48 (2)
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.Pusk_PAZ_GMK_48_2.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.Pusk_PAZ_GMK_48_2.Settings, FromHMI := PAZ_GVL.DGI.Pusk_PAZ_GMK_48_2.FromHMI, ToHMI := PAZ_GVL.DGI.Pusk_PAZ_GMK_48_2.ToHMI, my := PAZ_GVL.DGI.Pusk_PAZ_GMK_48_2.Intern, out := PAZ_GVL.DGI.Pusk_PAZ_GMK_48_2.PV);
// [A1.10:15] Запуск ПАЗ ГМК №51 (2)
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.Pusk_PAZ_GMK_51_2.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.Pusk_PAZ_GMK_51_2.Settings, FromHMI := PAZ_GVL.DGI.Pusk_PAZ_GMK_51_2.FromHMI, ToHMI := PAZ_GVL.DGI.Pusk_PAZ_GMK_51_2.ToHMI, my := PAZ_GVL.DGI.Pusk_PAZ_GMK_51_2.Intern, out := PAZ_GVL.DGI.Pusk_PAZ_GMK_51_2.PV);
// [A1.10:16] Запуск ПАЗ ГМК №52 (2)
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.Pusk_PAZ_GMK_52_2.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.Pusk_PAZ_GMK_52_2.Settings, FromHMI := PAZ_GVL.DGI.Pusk_PAZ_GMK_52_2.FromHMI, ToHMI := PAZ_GVL.DGI.Pusk_PAZ_GMK_52_2.ToHMI, my := PAZ_GVL.DGI.Pusk_PAZ_GMK_52_2.Intern, out := PAZ_GVL.DGI.Pusk_PAZ_GMK_52_2.PV);
// [A1.10:17] Съем звука (2)
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.Sound_OF_2.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.Sound_OF_2.Settings, FromHMI := PAZ_GVL.DGI.Sound_OF_2.FromHMI, ToHMI := PAZ_GVL.DGI.Sound_OF_2.ToHMI, my := PAZ_GVL.DGI.Sound_OF_2.Intern, out := PAZ_GVL.DGI.Sound_OF_2.PV);
// [A1.10:18] Сигналы внутренней диагностики 5
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.SignVnDiag_5.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.SignVnDiag_5.Settings, FromHMI := PAZ_GVL.DGI.SignVnDiag_5.FromHMI, ToHMI := PAZ_GVL.DGI.SignVnDiag_5.ToHMI, my := PAZ_GVL.DGI.SignVnDiag_5.Intern, out := PAZ_GVL.DGI.SignVnDiag_5.PV);
// [A1.10:19] Сигналы внутренней диагностики 6
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.SignVnDiag_6.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.SignVnDiag_6.Settings, FromHMI := PAZ_GVL.DGI.SignVnDiag_6.FromHMI, ToHMI := PAZ_GVL.DGI.SignVnDiag_6.ToHMI, my := PAZ_GVL.DGI.SignVnDiag_6.Intern, out := PAZ_GVL.DGI.SignVnDiag_6.PV);
// [A1.10:20] Сигналы внутренней диагностики 7
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.SignVnDiag_7.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.SignVnDiag_7.Settings, FromHMI := PAZ_GVL.DGI.SignVnDiag_7.FromHMI, ToHMI := PAZ_GVL.DGI.SignVnDiag_7.ToHMI, my := PAZ_GVL.DGI.SignVnDiag_7.Intern, out := PAZ_GVL.DGI.SignVnDiag_7.PV);
// [A1.10:21] Сигналы внутренней диагностики 8
VGSig.fnDI_Processing(IN := PAZ_GVL.DGI.SignVnDiag_8.DRV, externalFault := FALSE, set := PAZ_GVL.DGI.SignVnDiag_8.Settings, FromHMI := PAZ_GVL.DGI.SignVnDiag_8.FromHMI, ToHMI := PAZ_GVL.DGI.SignVnDiag_8.ToHMI, my := PAZ_GVL.DGI.SignVnDiag_8.Intern, out := PAZ_GVL.DGI.SignVnDiag_8.PV);
"""
proj = projects.primary
folder = proj.find('DI PAZ', recursive=True)[0]
struktur = folder.create_pou('PAZ_DI_Call', type = PouType.Function,language=None, return_type='BOOL', base_type=None, interfaces=None)
struktur.textual_declaration.insert(4, 0, CONTENT_var)
struktur.textual_implementation.insert(0, 0, CONTENT_body)
