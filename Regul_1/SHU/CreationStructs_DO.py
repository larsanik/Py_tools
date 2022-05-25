#encoding:utf-8
from __future__ import print_function
STRUCT_CONTENT_DO = """\
	Reserv_0:str_DO; //[A1.11:1] Резерв
	Reserv_1:str_DO; //[A1.11:2] Резерв
	Kr5_ON:str_DO; //[A1.11:3] Клапан XV9605.1 на перемычке открыть/закрыть
	Kr13_ON:str_DO; //[A1.11:4] Клапан XV9613.1 на сбросе приёмной линии открыть/закрыть
	Reserv_2:str_DO; //[A1.11:5] Резерв
	Reserv_3:str_DO; //[A1.11:6] Резерв
	Kr10_ON:str_DO; //[A1.11:7] Трехходовой клапан XV9610.1 на топливной линии открыть/закрыть
	Kr8_ON:str_DO; //[A1.11:8] Клапан пускового воздуха XV9608.1 открыть/закрыть
	Reserv_4:str_DO; //[A1.11:9] Резерв
	Reserv_5:str_DO; //[A1.11:10] Резерв
	Pmp_ppm_ON:str_DO; //[A1.11:11] Предпусковой насос прокачки масла включить
	Pmp_ppm_OF:str_DO; //[A1.11:12] Предпусковой насос прокачки масла отключить
	Reserv_6:str_DO; //[A1.11:13] Резерв
	Reserv_7:str_DO; //[A1.11:14] Резерв
	Zazh_ON:str_DO; //[A1.11:17] Включить зажигание
	Reserv_8:str_DO; //[A1.11:18] Резерв
	Reserv_9:str_DO; //[A1.11:19] Резерв
	Reserv_10:str_DO; //[A1.11:20] Резерв
	Reserv_11:str_DO; //[A1.11:21] Резерв
	Reserv_12:str_DO; //[A1.11:22] Резерв
	Reserv_13:str_DO; //[A1.11:23] Резерв
	Reserv_14:str_DO; //[A1.11:24] Резерв
	Snd_PS:str_DO; //[A1.11:25] Сирена на двери "ПС"
	Snd_AS:str_DO; //[A1.11:26] Сирена на двери "АС"
	SvetInd_PS:str_DO; //[A1.11:27] Световая индикатор на двери "ПС"
	SvetInd_AS:str_DO; //[A1.11:28] Световая индикатор на двери "АС"
	SvetInd_Btn_AO:str_DO; //[A1.11:29] Световая индикация кнопки на двери "АО"
	SvetInd_Btn_NO:str_DO; //[A1.11:30] Световая индикация кнопки на двери "НО"
	Meandr:str_DO; //[A1.11:31] Исправность контроллера ЛСУ
"""
proj = projects.primary
folder = proj.find('Parameter lists SHU', recursive=True)[0]
struktur = folder.create_dut('SHU_list_DO')  # DutType.Structure is the default
struktur.textual_declaration.insert(2, 0, STRUCT_CONTENT_DO)
