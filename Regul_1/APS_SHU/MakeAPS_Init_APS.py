#encoding:utf-8
from __future__ import print_function
CONTENT_var = """\
"""
CONTENT_body = """\
IF NOT SHU_GVL.init THEN
    SHU_GVL.Alarms.Fire := 1; // Пожар
    SHU_GVL.Alarms.AOs := 2; // Аварийный останов со стравливанием
    SHU_GVL.Alarms.AOb := 3; // Аварийный останов без стравливания
    SHU_GVL.Alarms.VOs := 4; // Вынужденный останов со стравливанием
    SHU_GVL.Alarms.VOb := 5; // Вынужденный останов без стравливания
    SHU_GVL.Alarms.AS := 6; // Авариная сигнализация без останова
    SHU_GVL.Alarms.PS := 7; // Предупредительная сигнализация
    SHU_GVL.Alarms.OS := 8; // Ограничительная сигнализация

    SHU_GVL.APS.Ps_Tsc_1_n.Intern.target := SHU_GVL.Alarms.PS; //[ШУ ГМК] Температура силового цилиндра 1
    SHU_GVL.APS.Ps_Tsc_1_v.Intern.target := SHU_GVL.Alarms.PS; //[ШУ ГМК] Температура силового цилиндра 1
    SHU_GVL.APS.As_Tsc_1_v.Intern.target := SHU_GVL.Alarms.AOs; //[ШУ ГМК] Температура силового цилиндра 1
    SHU_GVL.APS.Ps_Tsc_2_n.Intern.target := SHU_GVL.Alarms.PS; //[ШУ ГМК] Температура силового цилиндра 2
    SHU_GVL.APS.Ps_Tsc_2_v.Intern.target := SHU_GVL.Alarms.PS; //[ШУ ГМК] Температура силового цилиндра 2
    SHU_GVL.APS.As_Tsc_2_v.Intern.target := SHU_GVL.Alarms.AOs; //[ШУ ГМК] Температура силового цилиндра 2
    SHU_GVL.APS.Ps_Tsc_3_n.Intern.target := SHU_GVL.Alarms.PS; //[ШУ ГМК] Температура силового цилиндра 3
    SHU_GVL.APS.Ps_Tsc_3_v.Intern.target := SHU_GVL.Alarms.PS; //[ШУ ГМК] Температура силового цилиндра 3
    SHU_GVL.APS.As_Tsc_3_v.Intern.target := SHU_GVL.Alarms.AOs; //[ШУ ГМК] Температура силового цилиндра 3
    SHU_GVL.APS.Ps_Tsc_4_n.Intern.target := SHU_GVL.Alarms.PS; //[ШУ ГМК] Температура силового цилиндра 4
    SHU_GVL.APS.Ps_Tsc_4_v.Intern.target := SHU_GVL.Alarms.PS; //[ШУ ГМК] Температура силового цилиндра 4
    SHU_GVL.APS.As_Tsc_4_v.Intern.target := SHU_GVL.Alarms.AOs; //[ШУ ГМК] Температура силового цилиндра 4
    SHU_GVL.APS.Ps_Tsc_5_n.Intern.target := SHU_GVL.Alarms.PS; //[ШУ ГМК] Температура силового цилиндра 5
    SHU_GVL.APS.Ps_Tsc_5_v.Intern.target := SHU_GVL.Alarms.PS; //[ШУ ГМК] Температура силового цилиндра 5
    SHU_GVL.APS.As_Tsc_5_v.Intern.target := SHU_GVL.Alarms.AOs; //[ШУ ГМК] Температура силового цилиндра 5
    SHU_GVL.APS.Ps_Tsc_6_n.Intern.target := SHU_GVL.Alarms.PS; //[ШУ ГМК] Температура силового цилиндра 6
    SHU_GVL.APS.Ps_Tsc_6_v.Intern.target := SHU_GVL.Alarms.PS; //[ШУ ГМК] Температура силового цилиндра 6
    SHU_GVL.APS.As_Tsc_6_v.Intern.target := SHU_GVL.Alarms.AOs; //[ШУ ГМК] Температура силового цилиндра 6
    SHU_GVL.APS.Ps_Tsc_7_n.Intern.target := SHU_GVL.Alarms.PS; //[ШУ ГМК] Температура силового цилиндра 7
    SHU_GVL.APS.Ps_Tsc_7_v.Intern.target := SHU_GVL.Alarms.PS; //[ШУ ГМК] Температура силового цилиндра 7
    SHU_GVL.APS.As_Tsc_7_v.Intern.target := SHU_GVL.Alarms.AOs; //[ШУ ГМК] Температура силового цилиндра 7
    SHU_GVL.APS.Ps_Tsc_8_n.Intern.target := SHU_GVL.Alarms.PS; //[ШУ ГМК] Температура силового цилиндра 8
    SHU_GVL.APS.Ps_Tsc_8_v.Intern.target := SHU_GVL.Alarms.PS; //[ШУ ГМК] Температура силового цилиндра 8
    SHU_GVL.APS.As_Tsc_8_v.Intern.target := SHU_GVL.Alarms.AOs; //[ШУ ГМК] Температура силового цилиндра 8
    SHU_GVL.APS.Ps_Tsc_9_n.Intern.target := SHU_GVL.Alarms.PS; //[ШУ ГМК] Температура силового цилиндра 9
    SHU_GVL.APS.Ps_Tsc_9_v.Intern.target := SHU_GVL.Alarms.PS; //[ШУ ГМК] Температура силового цилиндра 9
    SHU_GVL.APS.As_Tsc_9_v.Intern.target := SHU_GVL.Alarms.AOs; //[ШУ ГМК] Температура силового цилиндра 9
    SHU_GVL.APS.Ps_Tsc_10_n.Intern.target := SHU_GVL.Alarms.PS; //[ШУ ГМК] Температура силового цилиндра 10
    SHU_GVL.APS.Ps_Tsc_10_v.Intern.target := SHU_GVL.Alarms.PS; //[ШУ ГМК] Температура силового цилиндра 10
    SHU_GVL.APS.As_Tsc_10_v.Intern.target := SHU_GVL.Alarms.AOs; //[ШУ ГМК] Температура силового цилиндра 10
    SHU_GVL.APS.Ps_Tvg_lk_n.Intern.target := SHU_GVL.Alarms.PS; //[ШУ ГМК] Температура выхлопных газов в левом коллекторе
    SHU_GVL.APS.Ps_Tvg_lk_v.Intern.target := SHU_GVL.Alarms.PS; //[ШУ ГМК] Температура выхлопных газов в левом коллекторе
    SHU_GVL.APS.As_Tvg_lk_v.Intern.target := SHU_GVL.Alarms.AOs; //[ШУ ГМК] Температура выхлопных газов в левом коллекторе
    SHU_GVL.APS.Ps_Tvg_pk_n.Intern.target := SHU_GVL.Alarms.PS; //[ШУ ГМК] Температура выхлопных газов в правом коллекторе
    SHU_GVL.APS.Ps_Tvg_pk_v.Intern.target := SHU_GVL.Alarms.PS; //[ШУ ГМК] Температура выхлопных газов в правом коллекторе
    SHU_GVL.APS.As_Tvg_pk_v.Intern.target := SHU_GVL.Alarms.AOs; //[ШУ ГМК] Температура выхлопных газов в правом коллекторе
    SHU_GVL.APS.Ps_Tkp_1_v.Intern.target := SHU_GVL.Alarms.PS; //[ШУ ГМК] Температура коренного подшипника № 1
    SHU_GVL.APS.As_Tkp_1_v.Intern.target := SHU_GVL.Alarms.AOs; //[ШУ ГМК] Температура коренного подшипника № 1
    SHU_GVL.APS.Ps_Tkp_2_v.Intern.target := SHU_GVL.Alarms.PS; //[ШУ ГМК] Температура коренного подшипника № 2
    SHU_GVL.APS.As_Tkp_2_v.Intern.target := SHU_GVL.Alarms.AOs; //[ШУ ГМК] Температура коренного подшипника № 2
    SHU_GVL.APS.Ps_Tkp_3_v.Intern.target := SHU_GVL.Alarms.PS; //[ШУ ГМК] Температура коренного подшипника № 3
    SHU_GVL.APS.As_Tkp_3_v.Intern.target := SHU_GVL.Alarms.AOs; //[ШУ ГМК] Температура коренного подшипника № 3
    SHU_GVL.APS.Ps_Tkp_4_v.Intern.target := SHU_GVL.Alarms.PS; //[ШУ ГМК] Температура коренного подшипника № 4
    SHU_GVL.APS.As_Tkp_4_v.Intern.target := SHU_GVL.Alarms.AOs; //[ШУ ГМК] Температура коренного подшипника № 4
    SHU_GVL.APS.Ps_Tkp_5_v.Intern.target := SHU_GVL.Alarms.PS; //[ШУ ГМК] Температура коренного подшипника № 5
    SHU_GVL.APS.As_Tkp_5_v.Intern.target := SHU_GVL.Alarms.AOs; //[ШУ ГМК] Температура коренного подшипника № 5
    SHU_GVL.APS.Ps_Tkp_6_v.Intern.target := SHU_GVL.Alarms.PS; //[ШУ ГМК] Температура коренного подшипника № 6
    SHU_GVL.APS.As_Tkp_6_v.Intern.target := SHU_GVL.Alarms.AOs; //[ШУ ГМК] Температура коренного подшипника № 6
    SHU_GVL.APS.Ps_Tkp_7_v.Intern.target := SHU_GVL.Alarms.PS; //[ШУ ГМК] Температура коренного подшипника № 7
    SHU_GVL.APS.As_Tkp_7_v.Intern.target := SHU_GVL.Alarms.AOs; //[ШУ ГМК] Температура коренного подшипника № 7
    SHU_GVL.APS.Ps_Tkp_8_v.Intern.target := SHU_GVL.Alarms.PS; //[ШУ ГМК] Температура коренного подшипника № 8
    SHU_GVL.APS.As_Tkp_8_v.Intern.target := SHU_GVL.Alarms.AOs; //[ШУ ГМК] Температура коренного подшипника № 8
    SHU_GVL.APS.Ps_Tkp_9_v.Intern.target := SHU_GVL.Alarms.PS; //[ШУ ГМК] Температура коренного подшипника № 9
    SHU_GVL.APS.As_Tkp_9_v.Intern.target := SHU_GVL.Alarms.AOs; //[ШУ ГМК] Температура коренного подшипника № 9
    SHU_GVL.APS.Ps_Tkp_10_v.Intern.target := SHU_GVL.Alarms.PS; //[ШУ ГМК] Температура коренного подшипника № 10
    SHU_GVL.APS.As_Tkp_10_v.Intern.target := SHU_GVL.Alarms.AOs; //[ШУ ГМК] Температура коренного подшипника № 10
    SHU_GVL.APS.Ps_Tv_outD_v.Intern.target := SHU_GVL.Alarms.PS; //[ШУ ГМК] Температура воды на выходе из двигателя
    SHU_GVL.APS.As_Tv_outD_v.Intern.target := SHU_GVL.Alarms.AOs; //[ШУ ГМК] Температура воды на выходе из двигателя
    SHU_GVL.APS.Ps_Tm_inGMK_n.Intern.target := SHU_GVL.Alarms.PS; //[ШУ ГМК] Температура масла на входе в ГМК
    SHU_GVL.APS.Ps_Tm_outGMK_v.Intern.target := SHU_GVL.Alarms.PS; //[ШУ ГМК] Температура масла на выходе из ГМК
    SHU_GVL.APS.As_Tm_outGMK_v.Intern.target := SHU_GVL.Alarms.AOs; //[ШУ ГМК] Температура масла на выходе из ГМК
    SHU_GVL.APS.Ps_Tg_outKC_1_v.Intern.target := SHU_GVL.Alarms.PS; //[ШУ ГМК] Температура газа на выходе компрессорного цилиндра 1
    SHU_GVL.APS.As_Tg_outKC_1_v.Intern.target := SHU_GVL.Alarms.AOs; //[ШУ ГМК] Температура газа на выходе компрессорного цилиндра 1
    SHU_GVL.APS.Ps_Tg_outKC_2_v.Intern.target := SHU_GVL.Alarms.PS; //[ШУ ГМК] Температура газа на выходе компрессорного цилиндра 2
    SHU_GVL.APS.As_Tg_outKC_2_v.Intern.target := SHU_GVL.Alarms.AOs; //[ШУ ГМК] Температура газа на выходе компрессорного цилиндра 2
    SHU_GVL.APS.Ps_Tg_outKC_3_v.Intern.target := SHU_GVL.Alarms.PS; //[ШУ ГМК] Температура газа на выходе компрессорного цилиндра 3
    SHU_GVL.APS.As_Tg_outKC_3_v.Intern.target := SHU_GVL.Alarms.AOs; //[ШУ ГМК] Температура газа на выходе компрессорного цилиндра 3
    SHU_GVL.APS.Ps_Tg_outKC_4_v.Intern.target := SHU_GVL.Alarms.PS; //[ШУ ГМК] Температура газа на выходе компрессорного цилиндра 4
    SHU_GVL.APS.As_Tg_outKC_4_v.Intern.target := SHU_GVL.Alarms.AOs; //[ШУ ГМК] Температура газа на выходе компрессорного цилиндра 4
    SHU_GVL.APS.Ps_Tg_outKC_5_v.Intern.target := SHU_GVL.Alarms.PS; //[ШУ ГМК] Температура газа на выходе компрессорного цилиндра 5
    SHU_GVL.APS.As_Tg_outKC_5_v.Intern.target := SHU_GVL.Alarms.AOs; //[ШУ ГМК] Температура газа на выходе компрессорного цилиндра 5
    SHU_GVL.APS.Ps_Pg_inGMK_n.Intern.target := SHU_GVL.Alarms.PS; //[ШУ ГМК] Давление газа на входе в ГМК
    SHU_GVL.APS.Ps_Pg_inGMK_v.Intern.target := SHU_GVL.Alarms.PS; //[ШУ ГМК] Давление газа на входе в ГМК
    SHU_GVL.APS.Ps_Pg_outGMK_SHU_GMK_v.Intern.target := SHU_GVL.Alarms.PS; //[ШУ ГМК] Давление газа на выходе из ГМК
    SHU_GVL.APS.As_Pg_outGMK_SHU_GMK_v.Intern.target := SHU_GVL.Alarms.AOs; //[ШУ ГМК] Давление газа на выходе из ГМК
    SHU_GVL.APS.Ps_Ppv_n.Intern.target := SHU_GVL.Alarms.PS; //[ШУ ГМК] Давление пускового воздуха
    SHU_GVL.APS.Ps_Ptg_inTRK_n.Intern.target := SHU_GVL.Alarms.PS; //[ШУ ГМК] Давление топливного газа до ТРК
    SHU_GVL.APS.Ps_Ptg_inTRK_v.Intern.target := SHU_GVL.Alarms.PS; //[ШУ ГМК] Давление топливного газа до ТРК
    SHU_GVL.APS.As_Ptg_inTRK_n.Intern.target := SHU_GVL.Alarms.AOs; //[ШУ ГМК] Давление топливного газа до ТРК
    SHU_GVL.APS.As_Ptg_inTRK_v.Intern.target := SHU_GVL.Alarms.AOs; //[ШУ ГМК] Давление топливного газа до ТРК
    SHU_GVL.APS.Ps_Pm_inTK_n.Intern.target := SHU_GVL.Alarms.PS; //[ШУ ГМК] Давление масла на входе в турбокомпрессоры
    SHU_GVL.APS.As_Pm_inTK_n.Intern.target := SHU_GVL.Alarms.AOs; //[ШУ ГМК] Давление масла на входе в турбокомпрессоры
    SHU_GVL.APS.Ps_Pm_inD_SHU_GMK_n.Intern.target := SHU_GVL.Alarms.PS; //[ШУ ГМК] Давление масла на входе в двигатель
    SHU_GVL.APS.As_Pm_inD_SHU_GMK_n.Intern.target := SHU_GVL.Alarms.AOs; //[ШУ ГМК] Давление масла на входе в двигатель
    SHU_GVL.APS.Ps_dPmf_v.Intern.target := SHU_GVL.Alarms.PS; //[ШУ ГМК] Перепад давления масла на фильтре
    SHU_GVL.APS.As_Pv_outD_n.Intern.target := SHU_GVL.Alarms.AOs; //[ШУ ГМК] Давление воды на выходе из двигателя
    SHU_GVL.APS.Ps_Vb_Ch_1_v.Intern.target := SHU_GVL.Alarms.PS; //[ШУ ГМК] Уровень вибрации ГМК (виброскорость), канал 1
    SHU_GVL.APS.As_Vb_Ch_1_v.Intern.target := SHU_GVL.Alarms.AOs; //[ШУ ГМК] Уровень вибрации ГМК (виброскорость), канал 1
    SHU_GVL.APS.Ps_Vb_Ch_2_v.Intern.target := SHU_GVL.Alarms.PS; //[ШУ ГМК] Уровень вибрации ГМК (виброскорость), канал 2
    SHU_GVL.APS.As_Vb_Ch_2_v.Intern.target := SHU_GVL.Alarms.AOs; //[ШУ ГМК] Уровень вибрации ГМК (виброскорость), канал 2
    SHU_GVL.APS.Ps_A_Pmp_ppm.Intern.target := SHU_GVL.Alarms.PS; //[ШУ ГМК] Авария насоса прокачки масла
    SHU_GVL.APS.Ps_Det_SC_1_v.Intern.target := SHU_GVL.Alarms.PS; //[БКД] Детонация в цилиндре № 1
    SHU_GVL.APS.As_Det_SC_1_v.Intern.target := SHU_GVL.Alarms.AOs; //[БКД] Детонация в цилиндре № 1
    SHU_GVL.APS.Ps_Det_SC_2_v.Intern.target := SHU_GVL.Alarms.PS; //[БКД] Детонация в цилиндре № 2
    SHU_GVL.APS.As_Det_SC_2_v.Intern.target := SHU_GVL.Alarms.AOs; //[БКД] Детонация в цилиндре № 2
    SHU_GVL.APS.Ps_Det_SC_3_v.Intern.target := SHU_GVL.Alarms.PS; //[БКД] Детонация в цилиндре № 3
    SHU_GVL.APS.As_Det_SC_3_v.Intern.target := SHU_GVL.Alarms.AOs; //[БКД] Детонация в цилиндре № 3
    SHU_GVL.APS.Ps_Det_SC_4_v.Intern.target := SHU_GVL.Alarms.PS; //[БКД] Детонация в цилиндре № 4
    SHU_GVL.APS.As_Det_SC_4_v.Intern.target := SHU_GVL.Alarms.AOs; //[БКД] Детонация в цилиндре № 4
    SHU_GVL.APS.Ps_Det_SC_5_v.Intern.target := SHU_GVL.Alarms.PS; //[БКД] Детонация в цилиндре № 5
    SHU_GVL.APS.As_Det_SC_5_v.Intern.target := SHU_GVL.Alarms.AOs; //[БКД] Детонация в цилиндре № 5
    SHU_GVL.APS.Ps_Det_SC_6_v.Intern.target := SHU_GVL.Alarms.PS; //[БКД] Детонация в цилиндре № 6
    SHU_GVL.APS.As_Det_SC_6_v.Intern.target := SHU_GVL.Alarms.AOs; //[БКД] Детонация в цилиндре № 6
    SHU_GVL.APS.Ps_Det_SC_7_v.Intern.target := SHU_GVL.Alarms.PS; //[БКД] Детонация в цилиндре № 7
    SHU_GVL.APS.As_Det_SC_7_v.Intern.target := SHU_GVL.Alarms.AOs; //[БКД] Детонация в цилиндре № 7
    SHU_GVL.APS.Ps_Det_SC_8_v.Intern.target := SHU_GVL.Alarms.PS; //[БКД] Детонация в цилиндре № 8
    SHU_GVL.APS.As_Det_SC_8_v.Intern.target := SHU_GVL.Alarms.AOs; //[БКД] Детонация в цилиндре № 8
    SHU_GVL.APS.Ps_Det_SC_9_v.Intern.target := SHU_GVL.Alarms.PS; //[БКД] Детонация в цилиндре № 9
    SHU_GVL.APS.As_Det_SC_9_v.Intern.target := SHU_GVL.Alarms.AOs; //[БКД] Детонация в цилиндре № 9
    SHU_GVL.APS.Ps_Det_SC_10_v.Intern.target := SHU_GVL.Alarms.PS; //[БКД] Детонация в цилиндре № 10
    SHU_GVL.APS.As_Det_SC_10_v.Intern.target := SHU_GVL.Alarms.AOs; //[БКД] Детонация в цилиндре № 10
    SHU_GVL.APS.Ps_F_1_vkv_v.Intern.target := SHU_GVL.Alarms.PS; //[БУЗ] Частота 1 вращения коленчатого вала
    SHU_GVL.APS.As_F_1_vkv_v.Intern.target := SHU_GVL.Alarms.AOs; //[БУЗ] Частота 1 вращения коленчатого вала
END_IF
"""
proj = projects.primary
folder = proj.find('APS SHU', recursive=True)[0]
struktur = folder.create_pou('SHU_APS_Init', type = PouType.Function,language=None, return_type='BOOL', base_type=None, interfaces=None)
struktur.textual_declaration.insert(4, 0, CONTENT_var)
struktur.textual_implementation.insert(0, 0, CONTENT_body)