#encoding:utf-8
from __future__ import print_function
CONTENT_var = """\
"""
CONTENT_body = """\
//================ Привязка входов к HW ================
SHMSH_GVL.DGI.Check_U_SHMSH_AC_V.DRV := SHMSH_GVL.A1_3.in_ch.0; //Контроль питания ШМШ ~220 В
SHMSH_GVL.DGI.Ispr_BP_SHMSH.DRV := SHMSH_GVL.A1_3.in_ch.1; //Исправность БП ШМШ
SHMSH_GVL.DGI.Ispr_BP_BUZ.DRV := SHMSH_GVL.A1_3.in_ch.2; //Исправность БП БУЗ
SHMSH_GVL.DGI.Ispr_BP_N.DRV := SHMSH_GVL.A1_3.in_ch.3; //Исправность БП БКД
SHMSH_GVL.DGI.Ispr_BP_BS_SKV.DRV := SHMSH_GVL.A1_3.in_ch.4; //Исправность БП блока согласующего системы контроля вибрации
SHMSH_GVL.DGI.AvtPwr_ON.DRV := SHMSH_GVL.A1_3.in_ch.5; //Автоматы питания включены
SHMSH_GVL.DGI.Btn_PrevScr.DRV := SHMSH_GVL.A1_3.in_ch.6; //Кнопка "Предыдущий экран"
SHMSH_GVL.DGI.Btn_NextScr.DRV := SHMSH_GVL.A1_3.in_ch.7; //Кнопка "Следующий экран"
SHMSH_GVL.DGI.Btn_Vybor_Cyl.DRV := SHMSH_GVL.A1_4.in_ch.0; //Кнопка "Выбор цилиндра"
SHMSH_GVL.DGI.Btn_UOZ_Down.DRV := SHMSH_GVL.A1_4.in_ch.1; //Кнопка "УОЗ меньше"
SHMSH_GVL.DGI.Btn_UOZ_Up.DRV := SHMSH_GVL.A1_4.in_ch.2; //Кнопка "УОЗ больше"
SHMSH_GVL.DGI.Btn_AO.DRV := SHMSH_GVL.A1_4.in_ch.3; //Кнопка "Принудительный останов"
SHMSH_GVL.DGI.Btn_NO.DRV := SHMSH_GVL.A1_4.in_ch.4; //Кнопка "Нормальный останов"
SHMSH_GVL.DGI.Btn_Pusk_GPA.DRV := SHMSH_GVL.A1_4.in_ch.5; //Кнопка "Пуск ГПА"
SHMSH_GVL.DGI.Btn_Deblock.DRV := SHMSH_GVL.A1_4.in_ch.6; //Кнопка "Деблокировка"
"""
proj = projects.primary
folder = proj.find('DI SHMSH', recursive=True)[0]
struktur = folder.create_pou('SHMSH_DI_binding_Hw_to_Lg', type = PouType.Function,language=None, return_type='BOOL', base_type=None, interfaces=None)
struktur.textual_declaration.insert(4, 0, CONTENT_var)
struktur.textual_implementation.insert(0, 0, CONTENT_body)
