#encoding:utf-8
from __future__ import print_function
CONTENT_var = """\
"""
CONTENT_body = """\
//================ Привязка вЫходов к HW ================
SHMSH_GVL.A1_5.out_ch.0 := SHMSH_GVL.DGO.SvetInd_PS.DRV; //Световой индикатор "ПС"
SHMSH_GVL.A1_5.out_ch.1 := SHMSH_GVL.DGO.SvetInd_AS.DRV; //Световой индикатор "АС"
SHMSH_GVL.A1_5.out_ch.2 := SHMSH_GVL.DGO.SvetInd_AO.DRV; //Световой индикатор "Принудительный останов"
SHMSH_GVL.A1_5.out_ch.3 := SHMSH_GVL.DGO.SvetInd_NO.DRV; //Световой индикатор "Нормальный останов"
SHMSH_GVL.A1_5.out_ch.4 := SHMSH_GVL.DGO.SvetInd_Pusk_GPA.DRV; //Световой индикатор "Пуск ГПА"
SHMSH_GVL.A1_5.out_ch.5 := SHMSH_GVL.DGO.SvetInd_Deblock.DRV; //Световой индикатор "Деблокировка"
"""
proj = projects.primary
folder = proj.find('DO SHMSH', recursive=True)[0]
struktur = folder.create_pou('SHMSH_DO_binding_Lg_to_Hw', type = PouType.Function,language=None, return_type='BOOL', base_type=None, interfaces=None)
struktur.textual_declaration.insert(4, 0, CONTENT_var)
struktur.textual_implementation.insert(0, 0, CONTENT_body)
