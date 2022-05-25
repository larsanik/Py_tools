#encoding:utf-8
from __future__ import print_function
CONTENT_var = """\
"""
CONTENT_body = """\
//================ Привязка входов к HW ================
SHU_GVL.AI.Tsc_1.DRV := SHU_GVL.A1_4.in_ch1; //Температура силового цилиндра 1
SHU_GVL.AI.Tsc_2.DRV := SHU_GVL.A1_4.in_ch2; //Температура силового цилиндра 2
SHU_GVL.AI.Tsc_3.DRV := SHU_GVL.A1_4.in_ch3; //Температура силового цилиндра 3
SHU_GVL.AI.Tsc_4.DRV := SHU_GVL.A1_4.in_ch4; //Температура силового цилиндра 4
SHU_GVL.AI.Tsc_5.DRV := SHU_GVL.A1_4.in_ch5; //Температура силового цилиндра 5
SHU_GVL.AI.Tsc_6.DRV := SHU_GVL.A1_4.in_ch6; //Температура силового цилиндра 6
SHU_GVL.AI.Tsc_7.DRV := SHU_GVL.A1_4.in_ch7; //Температура силового цилиндра 7
SHU_GVL.AI.Tsc_8.DRV := SHU_GVL.A1_4.in_ch8; //Температура силового цилиндра 8
SHU_GVL.AI.Tsc_9.DRV := SHU_GVL.A1_4.in_ch9; //Температура силового цилиндра 9
SHU_GVL.AI.Tsc_10.DRV := SHU_GVL.A1_4.in_ch10; //Температура силового цилиндра 10
SHU_GVL.AI.Tvg_lk.DRV := SHU_GVL.A1_4.in_ch11; //Температура выхлопных газов в левом коллекторе
SHU_GVL.AI.Tvg_pk.DRV := SHU_GVL.A1_4.in_ch12; //Температура выхлопных газов в правом коллекторе
SHU_GVL.AI.Reserv_0.DRV := SHU_GVL.A1_4.in_ch13; //Резерв
SHU_GVL.AI.Reserv_1.DRV := SHU_GVL.A1_4.in_ch14; //Резерв
SHU_GVL.AI.Reserv_2.DRV := SHU_GVL.A1_4.in_ch15; //Резерв
SHU_GVL.AI.Reserv_3.DRV := SHU_GVL.A1_4.in_ch16; //Резерв
SHU_GVL.AI.Tkp_1.DRV := SHU_GVL.A1_5.in_ch1; //Температура коренного подшипника № 1
SHU_GVL.AI.Tkp_2.DRV := SHU_GVL.A1_5.in_ch2; //Температура коренного подшипника № 2
SHU_GVL.AI.Tkp_3.DRV := SHU_GVL.A1_5.in_ch3; //Температура коренного подшипника № 3
SHU_GVL.AI.Tkp_4.DRV := SHU_GVL.A1_5.in_ch4; //Температура коренного подшипника № 4
SHU_GVL.AI.Tkp_5.DRV := SHU_GVL.A1_5.in_ch5; //Температура коренного подшипника № 5
SHU_GVL.AI.Tkp_6.DRV := SHU_GVL.A1_5.in_ch6; //Температура коренного подшипника № 6
SHU_GVL.AI.Tkp_7.DRV := SHU_GVL.A1_5.in_ch7; //Температура коренного подшипника № 7
SHU_GVL.AI.Tkp_8.DRV := SHU_GVL.A1_5.in_ch8; //Температура коренного подшипника № 8
SHU_GVL.AI.Tkp_9.DRV := SHU_GVL.A1_5.in_ch9; //Температура коренного подшипника № 9
SHU_GVL.AI.Tkp_10.DRV := SHU_GVL.A1_5.in_ch10; //Температура коренного подшипника № 10
SHU_GVL.AI.Tv_inD.DRV := SHU_GVL.A1_5.in_ch11; //Температура воды на входе в двигатель
SHU_GVL.AI.Tv_outD.DRV := SHU_GVL.A1_5.in_ch12; //Температура воды на выходе из двигателя
SHU_GVL.AI.Tvn.DRV := SHU_GVL.A1_5.in_ch13; //Температура воздуха наддува
SHU_GVL.AI.Tm_inGMK.DRV := SHU_GVL.A1_5.in_ch14; //Температура масла на входе в ГМК
SHU_GVL.AI.Tm_outGMK.DRV := SHU_GVL.A1_5.in_ch15; //Температура масла на выходе из ГМК
SHU_GVL.AI.Reserv_4.DRV := SHU_GVL.A1_5.in_ch16; //Резерв
SHU_GVL.AI.Tg_outKC_1.DRV := SHU_GVL.A1_6.in_ch1; //Температура газа на выходе компрессорного цилиндра 1
SHU_GVL.AI.Tg_outKC_2.DRV := SHU_GVL.A1_6.in_ch2; //Температура газа на выходе компрессорного цилиндра 2
SHU_GVL.AI.Tg_outKC_3.DRV := SHU_GVL.A1_6.in_ch3; //Температура газа на выходе компрессорного цилиндра 3
SHU_GVL.AI.Tg_outKC_4.DRV := SHU_GVL.A1_6.in_ch4; //Температура газа на выходе компрессорного цилиндра 4
SHU_GVL.AI.Tg_outKC_5.DRV := SHU_GVL.A1_6.in_ch5; //Температура газа на выходе компрессорного цилиндра 5
SHU_GVL.AI.Reserv_5.DRV := SHU_GVL.A1_6.in_ch6; //Резерв
SHU_GVL.AI.Reserv_6.DRV := SHU_GVL.A1_6.in_ch7; //Резерв
SHU_GVL.AI.Reserv_7.DRV := SHU_GVL.A1_6.in_ch8; //Резерв
SHU_GVL.AI.Reserv_8.DRV := SHU_GVL.A1_6.in_ch9; //Резерв
SHU_GVL.AI.Reserv_9.DRV := SHU_GVL.A1_6.in_ch10; //Резерв
SHU_GVL.AI.RegKr1_KCU.DRV := SHU_GVL.A1_6.in_ch14; //Управление запорно-регулирующим клапаном на приёме ГМК PV4601.1. КЦУ
SHU_GVL.AI.U_Osn_AC.DRV := SHU_GVL.A1_6.in_ch15; //Напряжение основного питания ~220 В
SHU_GVL.AI.U_Res_AC.DRV := SHU_GVL.A1_6.in_ch16; //Напряжение резервного питания ~220 В
SHU_GVL.AI.Pg_inGMK.DRV := SHU_GVL.A1_7.in_ch1; //Давление газа на входе в ГМК
SHU_GVL.AI.Pg_outGMK.DRV := SHU_GVL.A1_7.in_ch2; //Давление газа на выходе из ГМК
SHU_GVL.AI.Ppv.DRV := SHU_GVL.A1_7.in_ch3; //Давление пускового воздуха
SHU_GVL.AI.Ptg_inTRK.DRV := SHU_GVL.A1_7.in_ch4; //Давление топливного газа до ТРК
SHU_GVL.AI.Ptg_outTRK.DRV := SHU_GVL.A1_7.in_ch5; //Давление топливного газа после ТРК
SHU_GVL.AI.Pvn.DRV := SHU_GVL.A1_7.in_ch6; //Давление воздуха наддува
SHU_GVL.AI.Pm_inTK.DRV := SHU_GVL.A1_7.in_ch7; //Давление масла на входе в турбокомпрессоры
SHU_GVL.AI.Pm_inD.DRV := SHU_GVL.A1_7.in_ch8; //Давление масла на входе в двигатель
SHU_GVL.AI.dPmf.DRV := SHU_GVL.A1_7.in_ch9; //Перепад давления масла на фильтре
SHU_GVL.AI.Pv_outD.DRV := SHU_GVL.A1_7.in_ch10; //Давление воды на выходе из двигателя
SHU_GVL.AI.Pos_TRK.DRV := SHU_GVL.A1_7.in_ch11; //Положение ТРК PV9604.1
SHU_GVL.AI.Pos_RegKr1.DRV := SHU_GVL.A1_7.in_ch12; //Положение запорно-регулирующего клапана на приёме ГМК PV4601.1
SHU_GVL.AI.Vb_Ch_1.DRV := SHU_GVL.A1_7.in_ch13; //Уровень вибрации ГМК (виброскорость), канал 1
SHU_GVL.AI.Vb_Ch_2.DRV := SHU_GVL.A1_7.in_ch14; //Уровень вибрации ГМК (виброскорость), канал 2
SHU_GVL.AI.Reserv_10.DRV := SHU_GVL.A1_7.in_ch15; //Резерв
SHU_GVL.AI.Reserv_11.DRV := SHU_GVL.A1_7.in_ch16; //Резерв
"""
proj = projects.primary
folder = proj.find('AI SHU', recursive=True)[0]
struktur = folder.create_pou('SHU_AI_binding_Hw_to_Lg', type = PouType.Function,language=None, return_type='BOOL', base_type=None, interfaces=None)
struktur.textual_declaration.insert(4, 0, CONTENT_var)
struktur.textual_implementation.insert(0, 0, CONTENT_body)
