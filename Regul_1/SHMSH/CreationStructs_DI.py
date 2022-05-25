#encoding:utf-8
from __future__ import print_function
STRUCT_CONTENT_DI = """\
	Check_U_SHMSH_AC_V:str_DI; //[A1.3:1] Контроль питания ШМШ ~220 В
	Ispr_BP_SHMSH:str_DI; //[A1.3:2] Исправность БП ШМШ
	Ispr_BP_BUZ:str_DI; //[A1.3:3] Исправность БП БУЗ
	Ispr_BP_N:str_DI; //[A1.3:4] Исправность БП БКД
	Ispr_BP_BS_SKV:str_DI; //[A1.3:5] Исправность БП блока согласующего системы контроля вибрации
	AvtPwr_ON:str_DI; //[A1.3:6] Автоматы питания включены
	Btn_PrevScr:str_DI; //[A1.3:7] Кнопка "Предыдущий экран"
	Btn_NextScr:str_DI; //[A1.3:8] Кнопка "Следующий экран"
	Btn_Vybor_Cyl:str_DI; //[A1.4:1] Кнопка "Выбор цилиндра"
	Btn_UOZ_Down:str_DI; //[A1.4:2] Кнопка "УОЗ меньше"
	Btn_UOZ_Up:str_DI; //[A1.4:3] Кнопка "УОЗ больше"
	Btn_AO:str_DI; //[A1.4:4] Кнопка "Принудительный останов"
	Btn_NO:str_DI; //[A1.4:5] Кнопка "Нормальный останов"
	Btn_Pusk_GPA:str_DI; //[A1.4:6] Кнопка "Пуск ГПА"
	Btn_Deblock:str_DI; //[A1.4:7] Кнопка "Деблокировка"
"""
proj = projects.primary
folder = proj.find('Parameter lists SHMSH', recursive=True)[0]
struktur = folder.create_dut('SHMSH_list_DI')  # DutType.Structure is the default
struktur.textual_declaration.insert(2, 0, STRUCT_CONTENT_DI)
