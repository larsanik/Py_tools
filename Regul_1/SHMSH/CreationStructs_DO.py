#encoding:utf-8
from __future__ import print_function
STRUCT_CONTENT_DO = """\
	SvetInd_PS:str_DO; //[A1.5:1] Световой индикатор "ПС"
	SvetInd_AS:str_DO; //[A1.5:2] Световой индикатор "АС"
	SvetInd_AO:str_DO; //[A1.5:3] Световой индикатор "Принудительный останов"
	SvetInd_NO:str_DO; //[A1.5:4] Световой индикатор "Нормальный останов"
	SvetInd_Pusk_GPA:str_DO; //[A1.5:5] Световой индикатор "Пуск ГПА"
	SvetInd_Deblock:str_DO; //[A1.5:6] Световой индикатор "Деблокировка"
"""
proj = projects.primary
folder = proj.find('Parameter lists SHMSH', recursive=True)[0]
struktur = folder.create_dut('SHMSH_list_DO')  # DutType.Structure is the default
struktur.textual_declaration.insert(2, 0, STRUCT_CONTENT_DO)
