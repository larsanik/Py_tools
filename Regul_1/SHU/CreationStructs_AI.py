#encoding:utf-8
from __future__ import print_function
STRUCT_CONTENT_AI = """\
	Tsc_1:str_AI; //[A1.4:1] Температура силового цилиндра 1
	Tsc_2:str_AI; //[A1.4:2] Температура силового цилиндра 2
	Tsc_3:str_AI; //[A1.4:3] Температура силового цилиндра 3
	Tsc_4:str_AI; //[A1.4:4] Температура силового цилиндра 4
	Tsc_5:str_AI; //[A1.4:5] Температура силового цилиндра 5
	Tsc_6:str_AI; //[A1.4:6] Температура силового цилиндра 6
	Tsc_7:str_AI; //[A1.4:7] Температура силового цилиндра 7
	Tsc_8:str_AI; //[A1.4:8] Температура силового цилиндра 8
	Tsc_9:str_AI; //[A1.4:9] Температура силового цилиндра 9
	Tsc_10:str_AI; //[A1.4:10] Температура силового цилиндра 10
	Tvg_lk:str_AI; //[A1.4:11] Температура выхлопных газов в левом коллекторе
	Tvg_pk:str_AI; //[A1.4:12] Температура выхлопных газов в правом коллекторе
	Reserv_0:str_AI; //[A1.4:13] Резерв
	Reserv_1:str_AI; //[A1.4:14] Резерв
	Reserv_2:str_AI; //[A1.4:15] Резерв
	Reserv_3:str_AI; //[A1.4:16] Резерв
	Tkp_1:str_AI; //[A1.5:1] Температура коренного подшипника № 1
	Tkp_2:str_AI; //[A1.5:2] Температура коренного подшипника № 2
	Tkp_3:str_AI; //[A1.5:3] Температура коренного подшипника № 3
	Tkp_4:str_AI; //[A1.5:4] Температура коренного подшипника № 4
	Tkp_5:str_AI; //[A1.5:5] Температура коренного подшипника № 5
	Tkp_6:str_AI; //[A1.5:6] Температура коренного подшипника № 6
	Tkp_7:str_AI; //[A1.5:7] Температура коренного подшипника № 7
	Tkp_8:str_AI; //[A1.5:8] Температура коренного подшипника № 8
	Tkp_9:str_AI; //[A1.5:9] Температура коренного подшипника № 9
	Tkp_10:str_AI; //[A1.5:10] Температура коренного подшипника № 10
	Tv_inD:str_AI; //[A1.5:11] Температура воды на входе в двигатель
	Tv_outD:str_AI; //[A1.5:12] Температура воды на выходе из двигателя
	Tvn:str_AI; //[A1.5:13] Температура воздуха наддува
	Tm_inGMK:str_AI; //[A1.5:14] Температура масла на входе в ГМК
	Tm_outGMK:str_AI; //[A1.5:15] Температура масла на выходе из ГМК
	Reserv_4:str_AI; //[A1.5:16] Резерв
	Tg_outKC_1:str_AI; //[A1.6:1] Температура газа на выходе компрессорного цилиндра 1
	Tg_outKC_2:str_AI; //[A1.6:2] Температура газа на выходе компрессорного цилиндра 2
	Tg_outKC_3:str_AI; //[A1.6:3] Температура газа на выходе компрессорного цилиндра 3
	Tg_outKC_4:str_AI; //[A1.6:4] Температура газа на выходе компрессорного цилиндра 4
	Tg_outKC_5:str_AI; //[A1.6:5] Температура газа на выходе компрессорного цилиндра 5
	Reserv_5:str_AI; //[A1.6:6] Резерв
	Reserv_6:str_AI; //[A1.6:7] Резерв
	Reserv_7:str_AI; //[A1.6:8] Резерв
	Reserv_8:str_AI; //[A1.6:9] Резерв
	Reserv_9:str_AI; //[A1.6:10] Резерв
	RegKr1_KCU:str_AI; //[A1.6:14] Управление запорно-регулирующим клапаном на приёме ГМК PV4601.1. КЦУ
	U_Osn_AC:str_AI; //[A1.6:15] Напряжение основного питания ~220 В
	U_Res_AC:str_AI; //[A1.6:16] Напряжение резервного питания ~220 В
	Pg_inGMK:str_AI; //[A1.7:1] Давление газа на входе в ГМК
	Pg_outGMK:str_AI; //[A1.7:2] Давление газа на выходе из ГМК
	Ppv:str_AI; //[A1.7:3] Давление пускового воздуха
	Ptg_inTRK:str_AI; //[A1.7:4] Давление топливного газа до ТРК
	Ptg_outTRK:str_AI; //[A1.7:5] Давление топливного газа после ТРК
	Pvn:str_AI; //[A1.7:6] Давление воздуха наддува
	Pm_inTK:str_AI; //[A1.7:7] Давление масла на входе в турбокомпрессоры
	Pm_inD:str_AI; //[A1.7:8] Давление масла на входе в двигатель
	dPmf:str_AI; //[A1.7:9] Перепад давления масла на фильтре
	Pv_outD:str_AI; //[A1.7:10] Давление воды на выходе из двигателя
	Pos_TRK:str_AI; //[A1.7:11] Положение ТРК PV9604.1
	Pos_RegKr1:str_AI; //[A1.7:12] Положение запорно-регулирующего клапана на приёме ГМК PV4601.1
	Vb_Ch_1:str_AI; //[A1.7:13] Уровень вибрации ГМК (виброскорость), канал 1
	Vb_Ch_2:str_AI; //[A1.7:14] Уровень вибрации ГМК (виброскорость), канал 2
	Reserv_10:str_AI; //[A1.7:15] Резерв
	Reserv_11:str_AI; //[A1.7:16] Резерв
"""
proj = projects.primary
folder = proj.find('Parameter lists SHU', recursive=True)[0]
struktur = folder.create_dut('SHU_list_AI')  # DutType.Structure is the default
struktur.textual_declaration.insert(2, 0, STRUCT_CONTENT_AI)
