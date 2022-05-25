#encoding:utf-8
from __future__ import print_function
STRUCT_CONTENT_DI = """\
	Kr1_ON:str_DI; //[A1.8:1] Клапан ESDV9601.1 на приёме ГМК открыт
	Kr1_OF:str_DI; //[A1.8:2] Клапан ESDV9601.1 на приёме ГМК закрыт
	Kr2_ON:str_DI; //[A1.8:3] Клапан ESDV9602.1 на выходе ГМК открыт
	Kr2_OF:str_DI; //[A1.8:4] Клапан ESDV9602.1 на выходе ГМК закрыт
	Kr5_ON:str_DI; //[A1.8:5] Клапан XV9605.1 на перемычке открыт
	Kr5_OF:str_DI; //[A1.8:6] Клапан XV9605.1 на перемычке закрыт
	Kr13_ON:str_DI; //[A1.8:7] Клапан XV9613.1 на сбросе приёмной линии открыт
	Kr13_OF:str_DI; //[A1.8:8] Клапан XV9613.1 на сбросе приёмной линии закрыт
	Reserv_0:str_DI; //[A1.8:9] Резерв
	Reserv_1:str_DI; //[A1.8:10] Резерв
	Reserv_2:str_DI; //[A1.8:11] Резерв
	Reserv_3:str_DI; //[A1.8:12] Резерв
	Kr10_ON:str_DI; //[A1.8:13] Трехходовой клапан XV9610.1 на топливной линии открыт
	Kr10_OF:str_DI; //[A1.8:14] Трехходовой клапан XV9610.1 на топливной линии закрыт
	Kr8_ON:str_DI; //[A1.8:15] Клапан пускового воздуха XV9608.1 открыт
	Kr8_OF:str_DI; //[A1.8:16] Клапан пускового воздуха XV9608.1 закрыт
	Pmp_ppm_ON:str_DI; //[A1.8:17] Насос прокачки масла включен
	Pmp_ppm_AU:str_DI; //[A1.8:18] Насос прокачки масла в автоматическом управлении
	A_Pmp_ppm:str_DI; //[A1.8:19] Авария насоса прокачки масла
	Reserv_4:str_DI; //[A1.8:20] Резерв
	Reserv_5:str_DI; //[A1.8:21] Резерв
	Reserv_6:str_DI; //[A1.8:22] Резерв
	Reserv_7:str_DI; //[A1.8:23] Резерв
	Reserv_8:str_DI; //[A1.8:24] Резерв
	Zazh_ON:str_DI; //[A1.8:25] Зажигание в работе
	Kr11_ON:str_DI; //[A1.8:26] Клапан ESDV9611.1 на топливной линии открыт
	Kr11_OF:str_DI; //[A1.8:27] Клапан ESDV9611.1 на топливной линии закрыт
	Reserv_9:str_DI; //[A1.8:28] Резерв
	U_Osn_AC_ON:str_DI; //[A1.9:9] Контроль основного пит. ШУ ГМК ~220 В
	U_Res_AC_ON:str_DI; //[A1.9:10] Контроль резервного пит. ШУ ГМК ~220 В
	RazrGood:str_DI; //[A1.9:11] Контроль исправности разрядников
	AvtPwr_ON:str_DI; //[A1.9:12] Автоматы питания включены
	DoorOpen:str_DI; //[A1.9:13] Двери ШУ ГМК открыты
	Ispr_Osn_DC_inC:str_DI; //[A1.9:14] Исправность осн. ИП =24 В внутр. цепей
	Ispr_Res_DC_inC:str_DI; //[A1.9:15] Исправность рез. ИП =24 В внутр. цепей
	Ispr_Osn_DC_AI:str_DI; //[A1.9:16] Исправность осн. ИП =24 В AI
	Ispr_Res_DC_AI:str_DI; //[A1.9:17] Исправность рез. ИП =24 В AI
	Ispr_Osn_DC_DI:str_DI; //[A1.9:18] Исправность осн. ИП =24 В DI (внеш.)
	Ispr_Res_DC_DI:str_DI; //[A1.9:19] Исправность рез. ИП =24 В DI (внеш.)
	Ispr_Osn_DC_DO:str_DI; //[A1.9:20] Исправность осн. ИП =24 В DO (внеш.)
	Ispr_Res_DC_DO:str_DI; //[A1.9:21] Исправность рез. ИП =24 В DO (внеш.)
	Btn_AO:str_DI; //[A1.9:22] Кнопка на двери "Аварийный останов"
	Btn_NO:str_DI; //[A1.9:23] Кнопка на двери "Нормальный останов"
	Btn_Deblock:str_DI; //[A1.9:24] Кнопка на двери "Деблокировка"
	U_AC_outC_ON:str_DI; //[A1.9:25] Контроль внешнего питания ~220 В от ШУ ГМК
"""
proj = projects.primary
folder = proj.find('Parameter lists SHU', recursive=True)[0]
struktur = folder.create_dut('SHU_list_DI')  # DutType.Structure is the default
struktur.textual_declaration.insert(2, 0, STRUCT_CONTENT_DI)
