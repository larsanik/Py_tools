#encoding:utf-8
from __future__ import print_function
CONTENT_var = """\
"""
CONTENT_body = """\
IF NOT SHU_GVL.init THEN
// -----------------------------------------
// ----------Инициализация уставок ----------
// -----------------------------------------
    SHU_GVL.ANB.Ps_Tsc_1_n.Ust := 200.0; //Температура силового цилиндра 1
    SHU_GVL.ANB.Ps_Tsc_1_v.Ust := 430.0; //Температура силового цилиндра 1
    SHU_GVL.ANB.As_Tsc_1_v.Ust := 450.0; //Температура силового цилиндра 1
    SHU_GVL.ANB.Ps_Tsc_2_n.Ust := 200.0; //Температура силового цилиндра 2
    SHU_GVL.ANB.Ps_Tsc_2_v.Ust := 430.0; //Температура силового цилиндра 2
    SHU_GVL.ANB.As_Tsc_2_v.Ust := 450.0; //Температура силового цилиндра 2
    SHU_GVL.ANB.Ps_Tsc_3_n.Ust := 200.0; //Температура силового цилиндра 3
    SHU_GVL.ANB.Ps_Tsc_3_v.Ust := 430.0; //Температура силового цилиндра 3
    SHU_GVL.ANB.As_Tsc_3_v.Ust := 450.0; //Температура силового цилиндра 3
    SHU_GVL.ANB.Ps_Tsc_4_n.Ust := 200.0; //Температура силового цилиндра 4
    SHU_GVL.ANB.Ps_Tsc_4_v.Ust := 430.0; //Температура силового цилиндра 4
    SHU_GVL.ANB.As_Tsc_4_v.Ust := 450.0; //Температура силового цилиндра 4
    SHU_GVL.ANB.Ps_Tsc_5_n.Ust := 200.0; //Температура силового цилиндра 5
    SHU_GVL.ANB.Ps_Tsc_5_v.Ust := 430.0; //Температура силового цилиндра 5
    SHU_GVL.ANB.As_Tsc_5_v.Ust := 450.0; //Температура силового цилиндра 5
    SHU_GVL.ANB.Ps_Tsc_6_n.Ust := 200.0; //Температура силового цилиндра 6
    SHU_GVL.ANB.Ps_Tsc_6_v.Ust := 430.0; //Температура силового цилиндра 6
    SHU_GVL.ANB.As_Tsc_6_v.Ust := 450.0; //Температура силового цилиндра 6
    SHU_GVL.ANB.Ps_Tsc_7_n.Ust := 200.0; //Температура силового цилиндра 7
    SHU_GVL.ANB.Ps_Tsc_7_v.Ust := 430.0; //Температура силового цилиндра 7
    SHU_GVL.ANB.As_Tsc_7_v.Ust := 450.0; //Температура силового цилиндра 7
    SHU_GVL.ANB.Ps_Tsc_8_n.Ust := 200.0; //Температура силового цилиндра 8
    SHU_GVL.ANB.Ps_Tsc_8_v.Ust := 430.0; //Температура силового цилиндра 8
    SHU_GVL.ANB.As_Tsc_8_v.Ust := 450.0; //Температура силового цилиндра 8
    SHU_GVL.ANB.Ps_Tsc_9_n.Ust := 200.0; //Температура силового цилиндра 9
    SHU_GVL.ANB.Ps_Tsc_9_v.Ust := 430.0; //Температура силового цилиндра 9
    SHU_GVL.ANB.As_Tsc_9_v.Ust := 450.0; //Температура силового цилиндра 9
    SHU_GVL.ANB.Ps_Tsc_10_n.Ust := 200.0; //Температура силового цилиндра 10
    SHU_GVL.ANB.Ps_Tsc_10_v.Ust := 430.0; //Температура силового цилиндра 10
    SHU_GVL.ANB.As_Tsc_10_v.Ust := 450.0; //Температура силового цилиндра 10
    SHU_GVL.ANB.Ps_Tvg_lk_n.Ust := 200.0; //Температура выхлопных газов в левом коллекторе
    SHU_GVL.ANB.Ps_Tvg_lk_v.Ust := 430.0; //Температура выхлопных газов в левом коллекторе
    SHU_GVL.ANB.As_Tvg_lk_v.Ust := 450.0; //Температура выхлопных газов в левом коллекторе
    SHU_GVL.ANB.Ps_Tvg_pk_n.Ust := 200.0; //Температура выхлопных газов в правом коллекторе
    SHU_GVL.ANB.Ps_Tvg_pk_v.Ust := 430.0; //Температура выхлопных газов в правом коллекторе
    SHU_GVL.ANB.As_Tvg_pk_v.Ust := 450.0; //Температура выхлопных газов в правом коллекторе
    SHU_GVL.ANB.Ps_Tkp_1_v.Ust := 90.0; //Температура коренного подшипника № 1
    SHU_GVL.ANB.As_Tkp_1_v.Ust := 100.0; //Температура коренного подшипника № 1
    SHU_GVL.ANB.Ps_Tkp_2_v.Ust := 90.0; //Температура коренного подшипника № 2
    SHU_GVL.ANB.As_Tkp_2_v.Ust := 100.0; //Температура коренного подшипника № 2
    SHU_GVL.ANB.Ps_Tkp_3_v.Ust := 90.0; //Температура коренного подшипника № 3
    SHU_GVL.ANB.As_Tkp_3_v.Ust := 100.0; //Температура коренного подшипника № 3
    SHU_GVL.ANB.Ps_Tkp_4_v.Ust := 90.0; //Температура коренного подшипника № 4
    SHU_GVL.ANB.As_Tkp_4_v.Ust := 100.0; //Температура коренного подшипника № 4
    SHU_GVL.ANB.Ps_Tkp_5_v.Ust := 90.0; //Температура коренного подшипника № 5
    SHU_GVL.ANB.As_Tkp_5_v.Ust := 100.0; //Температура коренного подшипника № 5
    SHU_GVL.ANB.Ps_Tkp_6_v.Ust := 90.0; //Температура коренного подшипника № 6
    SHU_GVL.ANB.As_Tkp_6_v.Ust := 100.0; //Температура коренного подшипника № 6
    SHU_GVL.ANB.Ps_Tkp_7_v.Ust := 90.0; //Температура коренного подшипника № 7
    SHU_GVL.ANB.As_Tkp_7_v.Ust := 100.0; //Температура коренного подшипника № 7
    SHU_GVL.ANB.Ps_Tkp_8_v.Ust := 90.0; //Температура коренного подшипника № 8
    SHU_GVL.ANB.As_Tkp_8_v.Ust := 100.0; //Температура коренного подшипника № 8
    SHU_GVL.ANB.Ps_Tkp_9_v.Ust := 90.0; //Температура коренного подшипника № 9
    SHU_GVL.ANB.As_Tkp_9_v.Ust := 100.0; //Температура коренного подшипника № 9
    SHU_GVL.ANB.Ps_Tkp_10_v.Ust := 90.0; //Температура коренного подшипника № 10
    SHU_GVL.ANB.As_Tkp_10_v.Ust := 100.0; //Температура коренного подшипника № 10
    SHU_GVL.ANB.Ps_Tv_outD_v.Ust := 79.0; //Температура воды на выходе из двигателя
    SHU_GVL.ANB.As_Tv_outD_v.Ust := 85.0; //Температура воды на выходе из двигателя
    SHU_GVL.ANB.Ps_Tm_inGMK_n.Ust := 25.0; //Температура масла на входе в ГМК
    SHU_GVL.ANB.Ps_Tm_outGMK_v.Ust := 75.0; //Температура масла на выходе из ГМК
    SHU_GVL.ANB.As_Tm_outGMK_v.Ust := 80.0; //Температура масла на выходе из ГМК
    SHU_GVL.ANB.Ps_Tg_outKC_1_v.Ust := 110.0; //Температура газа на выходе компрессорного цилиндра 1
    SHU_GVL.ANB.As_Tg_outKC_1_v.Ust := 125.0; //Температура газа на выходе компрессорного цилиндра 1
    SHU_GVL.ANB.Ps_Tg_outKC_2_v.Ust := 110.0; //Температура газа на выходе компрессорного цилиндра 2
    SHU_GVL.ANB.As_Tg_outKC_2_v.Ust := 125.0; //Температура газа на выходе компрессорного цилиндра 2
    SHU_GVL.ANB.Ps_Tg_outKC_3_v.Ust := 110.0; //Температура газа на выходе компрессорного цилиндра 3
    SHU_GVL.ANB.As_Tg_outKC_3_v.Ust := 125.0; //Температура газа на выходе компрессорного цилиндра 3
    SHU_GVL.ANB.Ps_Tg_outKC_4_v.Ust := 110.0; //Температура газа на выходе компрессорного цилиндра 4
    SHU_GVL.ANB.As_Tg_outKC_4_v.Ust := 125.0; //Температура газа на выходе компрессорного цилиндра 4
    SHU_GVL.ANB.Ps_Tg_outKC_5_v.Ust := 110.0; //Температура газа на выходе компрессорного цилиндра 5
    SHU_GVL.ANB.As_Tg_outKC_5_v.Ust := 125.0; //Температура газа на выходе компрессорного цилиндра 5
    SHU_GVL.ANB.Ps_Pg_inGMK_n.Ust := 1.0; //Давление газа на входе в ГМК
    SHU_GVL.ANB.Ps_Pg_inGMK_v.Ust := 1.5; //Давление газа на входе в ГМК
    SHU_GVL.ANB.Ps_Pg_outGMK_SHU_GMK_v.Ust := 4.1; //Давление газа на выходе из ГМК
    SHU_GVL.ANB.As_Pg_outGMK_SHU_GMK_v.Ust := 4.3; //Давление газа на выходе из ГМК
    SHU_GVL.ANB.Ps_Ppv_n.Ust := 1.2; //Давление пускового воздуха
    SHU_GVL.ANB.Ps_Ptg_inTRK_n.Ust := 0.3; //Давление топливного газа до ТРК
    SHU_GVL.ANB.Ps_Ptg_inTRK_v.Ust := 0.45; //Давление топливного газа до ТРК
    SHU_GVL.ANB.As_Ptg_inTRK_n.Ust := 0.2; //Давление топливного газа до ТРК
    SHU_GVL.ANB.As_Ptg_inTRK_v.Ust := 0.49; //Давление топливного газа до ТРК
    SHU_GVL.ANB.Ps_Pm_inTK_n.Ust := 0.18; //Давление масла на входе в турбокомпрессоры
    SHU_GVL.ANB.As_Pm_inTK_n.Ust := 0.15; //Давление масла на входе в турбокомпрессоры
    SHU_GVL.ANB.Ps_Pm_inD_SHU_GMK_n.Ust := 0.18; //Давление масла на входе в двигатель
    SHU_GVL.ANB.As_Pm_inD_SHU_GMK_n.Ust := 0.13; //Давление масла на входе в двигатель
    SHU_GVL.ANB.Ps_dPmf_v.Ust := 0.1; //Перепад давления масла на фильтре
    SHU_GVL.ANB.As_Pv_outD_n.Ust := 0.05; //Давление воды на выходе из двигателя
    SHU_GVL.ANB.Ps_Vb_Ch_1_v.Ust := 12.0; //Уровень вибрации ГМК (виброскорость), канал 1
    SHU_GVL.ANB.As_Vb_Ch_1_v.Ust := 18.0; //Уровень вибрации ГМК (виброскорость), канал 1
    SHU_GVL.ANB.Ps_Vb_Ch_2_v.Ust := 12.0; //Уровень вибрации ГМК (виброскорость), канал 2
    SHU_GVL.ANB.As_Vb_Ch_2_v.Ust := 18.0; //Уровень вибрации ГМК (виброскорость), канал 2
    // ------------------------------- функция инициализации --------------------------------
    // 1.                     уставка(BOOL)
    // 2.                     |                          направление срабатывания.TRUE - верхняя, FALSE - нижняя(BOOL)
    // 3.                     |                          |    значение, записываемое в ANB при неисправности канала: 0 - FALSE, 1 - TRUE, 2 - оставить то что было(INT)
    // 4.                     |                          |    |    задержка на срабатывание(REAL)
    //                        |                          |    |    |
    // algGVL.ANB.As_Nst_v.Settings := VGALG.fnANB_init(TRUE, 0, 10.5);
    SHU_GVL.ANB.Ps_Tsc_1_n.ANB_Settings := VGALG.fnANB_init(FALSE, 0, 0); // Температура силового цилиндра 1
    SHU_GVL.ANB.Ps_Tsc_1_v.ANB_Settings := VGALG.fnANB_init(TRUE, 0, 0); // Температура силового цилиндра 1
    SHU_GVL.ANB.As_Tsc_1_v.ANB_Settings := VGALG.fnANB_init(TRUE, 0, 0); // Температура силового цилиндра 1
    SHU_GVL.ANB.Ps_Tsc_2_n.ANB_Settings := VGALG.fnANB_init(FALSE, 0, 0); // Температура силового цилиндра 2
    SHU_GVL.ANB.Ps_Tsc_2_v.ANB_Settings := VGALG.fnANB_init(TRUE, 0, 0); // Температура силового цилиндра 2
    SHU_GVL.ANB.As_Tsc_2_v.ANB_Settings := VGALG.fnANB_init(TRUE, 0, 0); // Температура силового цилиндра 2
    SHU_GVL.ANB.Ps_Tsc_3_n.ANB_Settings := VGALG.fnANB_init(FALSE, 0, 0); // Температура силового цилиндра 3
    SHU_GVL.ANB.Ps_Tsc_3_v.ANB_Settings := VGALG.fnANB_init(TRUE, 0, 0); // Температура силового цилиндра 3
    SHU_GVL.ANB.As_Tsc_3_v.ANB_Settings := VGALG.fnANB_init(TRUE, 0, 0); // Температура силового цилиндра 3
    SHU_GVL.ANB.Ps_Tsc_4_n.ANB_Settings := VGALG.fnANB_init(FALSE, 0, 0); // Температура силового цилиндра 4
    SHU_GVL.ANB.Ps_Tsc_4_v.ANB_Settings := VGALG.fnANB_init(TRUE, 0, 0); // Температура силового цилиндра 4
    SHU_GVL.ANB.As_Tsc_4_v.ANB_Settings := VGALG.fnANB_init(TRUE, 0, 0); // Температура силового цилиндра 4
    SHU_GVL.ANB.Ps_Tsc_5_n.ANB_Settings := VGALG.fnANB_init(FALSE, 0, 0); // Температура силового цилиндра 5
    SHU_GVL.ANB.Ps_Tsc_5_v.ANB_Settings := VGALG.fnANB_init(TRUE, 0, 0); // Температура силового цилиндра 5
    SHU_GVL.ANB.As_Tsc_5_v.ANB_Settings := VGALG.fnANB_init(TRUE, 0, 0); // Температура силового цилиндра 5
    SHU_GVL.ANB.Ps_Tsc_6_n.ANB_Settings := VGALG.fnANB_init(FALSE, 0, 0); // Температура силового цилиндра 6
    SHU_GVL.ANB.Ps_Tsc_6_v.ANB_Settings := VGALG.fnANB_init(TRUE, 0, 0); // Температура силового цилиндра 6
    SHU_GVL.ANB.As_Tsc_6_v.ANB_Settings := VGALG.fnANB_init(TRUE, 0, 0); // Температура силового цилиндра 6
    SHU_GVL.ANB.Ps_Tsc_7_n.ANB_Settings := VGALG.fnANB_init(FALSE, 0, 0); // Температура силового цилиндра 7
    SHU_GVL.ANB.Ps_Tsc_7_v.ANB_Settings := VGALG.fnANB_init(TRUE, 0, 0); // Температура силового цилиндра 7
    SHU_GVL.ANB.As_Tsc_7_v.ANB_Settings := VGALG.fnANB_init(TRUE, 0, 0); // Температура силового цилиндра 7
    SHU_GVL.ANB.Ps_Tsc_8_n.ANB_Settings := VGALG.fnANB_init(FALSE, 0, 0); // Температура силового цилиндра 8
    SHU_GVL.ANB.Ps_Tsc_8_v.ANB_Settings := VGALG.fnANB_init(TRUE, 0, 0); // Температура силового цилиндра 8
    SHU_GVL.ANB.As_Tsc_8_v.ANB_Settings := VGALG.fnANB_init(TRUE, 0, 0); // Температура силового цилиндра 8
    SHU_GVL.ANB.Ps_Tsc_9_n.ANB_Settings := VGALG.fnANB_init(FALSE, 0, 0); // Температура силового цилиндра 9
    SHU_GVL.ANB.Ps_Tsc_9_v.ANB_Settings := VGALG.fnANB_init(TRUE, 0, 0); // Температура силового цилиндра 9
    SHU_GVL.ANB.As_Tsc_9_v.ANB_Settings := VGALG.fnANB_init(TRUE, 0, 0); // Температура силового цилиндра 9
    SHU_GVL.ANB.Ps_Tsc_10_n.ANB_Settings := VGALG.fnANB_init(FALSE, 0, 0); // Температура силового цилиндра 10
    SHU_GVL.ANB.Ps_Tsc_10_v.ANB_Settings := VGALG.fnANB_init(TRUE, 0, 0); // Температура силового цилиндра 10
    SHU_GVL.ANB.As_Tsc_10_v.ANB_Settings := VGALG.fnANB_init(TRUE, 0, 0); // Температура силового цилиндра 10
    SHU_GVL.ANB.Ps_Tvg_lk_n.ANB_Settings := VGALG.fnANB_init(FALSE, 0, 0); // Температура выхлопных газов в левом коллекторе
    SHU_GVL.ANB.Ps_Tvg_lk_v.ANB_Settings := VGALG.fnANB_init(TRUE, 0, 0); // Температура выхлопных газов в левом коллекторе
    SHU_GVL.ANB.As_Tvg_lk_v.ANB_Settings := VGALG.fnANB_init(TRUE, 0, 0); // Температура выхлопных газов в левом коллекторе
    SHU_GVL.ANB.Ps_Tvg_pk_n.ANB_Settings := VGALG.fnANB_init(FALSE, 0, 0); // Температура выхлопных газов в правом коллекторе
    SHU_GVL.ANB.Ps_Tvg_pk_v.ANB_Settings := VGALG.fnANB_init(TRUE, 0, 0); // Температура выхлопных газов в правом коллекторе
    SHU_GVL.ANB.As_Tvg_pk_v.ANB_Settings := VGALG.fnANB_init(TRUE, 0, 0); // Температура выхлопных газов в правом коллекторе
    SHU_GVL.ANB.Ps_Tkp_1_v.ANB_Settings := VGALG.fnANB_init(TRUE, 0, 0); // Температура коренного подшипника № 1
    SHU_GVL.ANB.As_Tkp_1_v.ANB_Settings := VGALG.fnANB_init(TRUE, 0, 0); // Температура коренного подшипника № 1
    SHU_GVL.ANB.Ps_Tkp_2_v.ANB_Settings := VGALG.fnANB_init(TRUE, 0, 0); // Температура коренного подшипника № 2
    SHU_GVL.ANB.As_Tkp_2_v.ANB_Settings := VGALG.fnANB_init(TRUE, 0, 0); // Температура коренного подшипника № 2
    SHU_GVL.ANB.Ps_Tkp_3_v.ANB_Settings := VGALG.fnANB_init(TRUE, 0, 0); // Температура коренного подшипника № 3
    SHU_GVL.ANB.As_Tkp_3_v.ANB_Settings := VGALG.fnANB_init(TRUE, 0, 0); // Температура коренного подшипника № 3
    SHU_GVL.ANB.Ps_Tkp_4_v.ANB_Settings := VGALG.fnANB_init(TRUE, 0, 0); // Температура коренного подшипника № 4
    SHU_GVL.ANB.As_Tkp_4_v.ANB_Settings := VGALG.fnANB_init(TRUE, 0, 0); // Температура коренного подшипника № 4
    SHU_GVL.ANB.Ps_Tkp_5_v.ANB_Settings := VGALG.fnANB_init(TRUE, 0, 0); // Температура коренного подшипника № 5
    SHU_GVL.ANB.As_Tkp_5_v.ANB_Settings := VGALG.fnANB_init(TRUE, 0, 0); // Температура коренного подшипника № 5
    SHU_GVL.ANB.Ps_Tkp_6_v.ANB_Settings := VGALG.fnANB_init(TRUE, 0, 0); // Температура коренного подшипника № 6
    SHU_GVL.ANB.As_Tkp_6_v.ANB_Settings := VGALG.fnANB_init(TRUE, 0, 0); // Температура коренного подшипника № 6
    SHU_GVL.ANB.Ps_Tkp_7_v.ANB_Settings := VGALG.fnANB_init(TRUE, 0, 0); // Температура коренного подшипника № 7
    SHU_GVL.ANB.As_Tkp_7_v.ANB_Settings := VGALG.fnANB_init(TRUE, 0, 0); // Температура коренного подшипника № 7
    SHU_GVL.ANB.Ps_Tkp_8_v.ANB_Settings := VGALG.fnANB_init(TRUE, 0, 0); // Температура коренного подшипника № 8
    SHU_GVL.ANB.As_Tkp_8_v.ANB_Settings := VGALG.fnANB_init(TRUE, 0, 0); // Температура коренного подшипника № 8
    SHU_GVL.ANB.Ps_Tkp_9_v.ANB_Settings := VGALG.fnANB_init(TRUE, 0, 0); // Температура коренного подшипника № 9
    SHU_GVL.ANB.As_Tkp_9_v.ANB_Settings := VGALG.fnANB_init(TRUE, 0, 0); // Температура коренного подшипника № 9
    SHU_GVL.ANB.Ps_Tkp_10_v.ANB_Settings := VGALG.fnANB_init(TRUE, 0, 0); // Температура коренного подшипника № 10
    SHU_GVL.ANB.As_Tkp_10_v.ANB_Settings := VGALG.fnANB_init(TRUE, 0, 0); // Температура коренного подшипника № 10
    SHU_GVL.ANB.Ps_Tv_outD_v.ANB_Settings := VGALG.fnANB_init(TRUE, 0, 0); // Температура воды на выходе из двигателя
    SHU_GVL.ANB.As_Tv_outD_v.ANB_Settings := VGALG.fnANB_init(TRUE, 0, 0); // Температура воды на выходе из двигателя
    SHU_GVL.ANB.Ps_Tm_inGMK_n.ANB_Settings := VGALG.fnANB_init(FALSE, 0, 0); // Температура масла на входе в ГМК
    SHU_GVL.ANB.Ps_Tm_outGMK_v.ANB_Settings := VGALG.fnANB_init(TRUE, 0, 0); // Температура масла на выходе из ГМК
    SHU_GVL.ANB.As_Tm_outGMK_v.ANB_Settings := VGALG.fnANB_init(TRUE, 0, 0); // Температура масла на выходе из ГМК
    SHU_GVL.ANB.Ps_Tg_outKC_1_v.ANB_Settings := VGALG.fnANB_init(TRUE, 0, 0); // Температура газа на выходе компрессорного цилиндра 1
    SHU_GVL.ANB.As_Tg_outKC_1_v.ANB_Settings := VGALG.fnANB_init(TRUE, 0, 0); // Температура газа на выходе компрессорного цилиндра 1
    SHU_GVL.ANB.Ps_Tg_outKC_2_v.ANB_Settings := VGALG.fnANB_init(TRUE, 0, 0); // Температура газа на выходе компрессорного цилиндра 2
    SHU_GVL.ANB.As_Tg_outKC_2_v.ANB_Settings := VGALG.fnANB_init(TRUE, 0, 0); // Температура газа на выходе компрессорного цилиндра 2
    SHU_GVL.ANB.Ps_Tg_outKC_3_v.ANB_Settings := VGALG.fnANB_init(TRUE, 0, 0); // Температура газа на выходе компрессорного цилиндра 3
    SHU_GVL.ANB.As_Tg_outKC_3_v.ANB_Settings := VGALG.fnANB_init(TRUE, 0, 0); // Температура газа на выходе компрессорного цилиндра 3
    SHU_GVL.ANB.Ps_Tg_outKC_4_v.ANB_Settings := VGALG.fnANB_init(TRUE, 0, 0); // Температура газа на выходе компрессорного цилиндра 4
    SHU_GVL.ANB.As_Tg_outKC_4_v.ANB_Settings := VGALG.fnANB_init(TRUE, 0, 0); // Температура газа на выходе компрессорного цилиндра 4
    SHU_GVL.ANB.Ps_Tg_outKC_5_v.ANB_Settings := VGALG.fnANB_init(TRUE, 0, 0); // Температура газа на выходе компрессорного цилиндра 5
    SHU_GVL.ANB.As_Tg_outKC_5_v.ANB_Settings := VGALG.fnANB_init(TRUE, 0, 0); // Температура газа на выходе компрессорного цилиндра 5
    SHU_GVL.ANB.Ps_Pg_inGMK_n.ANB_Settings := VGALG.fnANB_init(FALSE, 0, 0); // Давление газа на входе в ГМК
    SHU_GVL.ANB.Ps_Pg_inGMK_v.ANB_Settings := VGALG.fnANB_init(TRUE, 0, 0); // Давление газа на входе в ГМК
    SHU_GVL.ANB.Ps_Pg_outGMK_SHU_GMK_v.ANB_Settings := VGALG.fnANB_init(TRUE, 0, 0); // Давление газа на выходе из ГМК
    SHU_GVL.ANB.As_Pg_outGMK_SHU_GMK_v.ANB_Settings := VGALG.fnANB_init(TRUE, 0, 0); // Давление газа на выходе из ГМК
    SHU_GVL.ANB.Ps_Ppv_n.ANB_Settings := VGALG.fnANB_init(FALSE, 0, 0); // Давление пускового воздуха
    SHU_GVL.ANB.Ps_Ptg_inTRK_n.ANB_Settings := VGALG.fnANB_init(FALSE, 0, 0); // Давление топливного газа до ТРК
    SHU_GVL.ANB.Ps_Ptg_inTRK_v.ANB_Settings := VGALG.fnANB_init(TRUE, 0, 0); // Давление топливного газа до ТРК
    SHU_GVL.ANB.As_Ptg_inTRK_n.ANB_Settings := VGALG.fnANB_init(FALSE, 0, 0); // Давление топливного газа до ТРК
    SHU_GVL.ANB.As_Ptg_inTRK_v.ANB_Settings := VGALG.fnANB_init(TRUE, 0, 0); // Давление топливного газа до ТРК
    SHU_GVL.ANB.Ps_Pm_inTK_n.ANB_Settings := VGALG.fnANB_init(FALSE, 0, 0); // Давление масла на входе в турбокомпрессоры
    SHU_GVL.ANB.As_Pm_inTK_n.ANB_Settings := VGALG.fnANB_init(FALSE, 0, 0); // Давление масла на входе в турбокомпрессоры
    SHU_GVL.ANB.Ps_Pm_inD_SHU_GMK_n.ANB_Settings := VGALG.fnANB_init(FALSE, 0, 0); // Давление масла на входе в двигатель
    SHU_GVL.ANB.As_Pm_inD_SHU_GMK_n.ANB_Settings := VGALG.fnANB_init(FALSE, 0, 0); // Давление масла на входе в двигатель
    SHU_GVL.ANB.Ps_dPmf_v.ANB_Settings := VGALG.fnANB_init(TRUE, 0, 0); // Перепад давления масла на фильтре
    SHU_GVL.ANB.As_Pv_outD_n.ANB_Settings := VGALG.fnANB_init(FALSE, 0, 0); // Давление воды на выходе из двигателя
    SHU_GVL.ANB.Ps_Vb_Ch_1_v.ANB_Settings := VGALG.fnANB_init(TRUE, 0, 0); // Уровень вибрации ГМК (виброскорость), канал 1
    SHU_GVL.ANB.As_Vb_Ch_1_v.ANB_Settings := VGALG.fnANB_init(TRUE, 0, 0); // Уровень вибрации ГМК (виброскорость), канал 1
    SHU_GVL.ANB.Ps_Vb_Ch_2_v.ANB_Settings := VGALG.fnANB_init(TRUE, 0, 0); // Уровень вибрации ГМК (виброскорость), канал 2
    SHU_GVL.ANB.As_Vb_Ch_2_v.ANB_Settings := VGALG.fnANB_init(TRUE, 0, 0); // Уровень вибрации ГМК (виброскорость), канал 2
END_IF;
// -------------------------------------------
// -------------Формирование уставок----------
// -------------------------------------------
// Температура силового цилиндра 1
SHU_GVL.ANB.Ps_Tsc_1_n.ANB := VGALG.fnANB_Processing(SHU_GVL.ANB.Ps_Tsc_1_n.ANB_Settings, SHU_GVL.AI.Tsc_1.ToHMI.PV, SHU_GVL.AI.Tsc_1.ToHMI.fault_common, SHU_GVL.ANB.Ps_Tsc_1_n.Ust, SHU_GVL.ANB.Ps_Tsc_1_n.ANB_Internal);
SHU_GVL.AI.Tsc_1.ToHMI.ps := SHU_GVL.ANB.Ps_Tsc_1_n.ANB;
// Температура силового цилиндра 1
SHU_GVL.ANB.Ps_Tsc_1_v.ANB := VGALG.fnANB_Processing(SHU_GVL.ANB.Ps_Tsc_1_v.ANB_Settings, SHU_GVL.AI.Tsc_1.ToHMI.PV, SHU_GVL.AI.Tsc_1.ToHMI.fault_common, SHU_GVL.ANB.Ps_Tsc_1_v.Ust, SHU_GVL.ANB.Ps_Tsc_1_v.ANB_Internal);
SHU_GVL.AI.Tsc_1.ToHMI.ps := SHU_GVL.ANB.Ps_Tsc_1_v.ANB;
// Температура силового цилиндра 1
SHU_GVL.ANB.As_Tsc_1_v.ANB := VGALG.fnANB_Processing(SHU_GVL.ANB.As_Tsc_1_v.ANB_Settings, SHU_GVL.AI.Tsc_1.ToHMI.PV, SHU_GVL.AI.Tsc_1.ToHMI.fault_common, SHU_GVL.ANB.As_Tsc_1_v.Ust, SHU_GVL.ANB.As_Tsc_1_v.ANB_Internal);
SHU_GVL.AI.Tsc_1.ToHMI.as := SHU_GVL.ANB.As_Tsc_1_v.ANB;
// Температура силового цилиндра 2
SHU_GVL.ANB.Ps_Tsc_2_n.ANB := VGALG.fnANB_Processing(SHU_GVL.ANB.Ps_Tsc_2_n.ANB_Settings, SHU_GVL.AI.Tsc_2.ToHMI.PV, SHU_GVL.AI.Tsc_2.ToHMI.fault_common, SHU_GVL.ANB.Ps_Tsc_2_n.Ust, SHU_GVL.ANB.Ps_Tsc_2_n.ANB_Internal);
SHU_GVL.AI.Tsc_2.ToHMI.ps := SHU_GVL.ANB.Ps_Tsc_2_n.ANB;
// Температура силового цилиндра 2
SHU_GVL.ANB.Ps_Tsc_2_v.ANB := VGALG.fnANB_Processing(SHU_GVL.ANB.Ps_Tsc_2_v.ANB_Settings, SHU_GVL.AI.Tsc_2.ToHMI.PV, SHU_GVL.AI.Tsc_2.ToHMI.fault_common, SHU_GVL.ANB.Ps_Tsc_2_v.Ust, SHU_GVL.ANB.Ps_Tsc_2_v.ANB_Internal);
SHU_GVL.AI.Tsc_2.ToHMI.ps := SHU_GVL.ANB.Ps_Tsc_2_v.ANB;
// Температура силового цилиндра 2
SHU_GVL.ANB.As_Tsc_2_v.ANB := VGALG.fnANB_Processing(SHU_GVL.ANB.As_Tsc_2_v.ANB_Settings, SHU_GVL.AI.Tsc_2.ToHMI.PV, SHU_GVL.AI.Tsc_2.ToHMI.fault_common, SHU_GVL.ANB.As_Tsc_2_v.Ust, SHU_GVL.ANB.As_Tsc_2_v.ANB_Internal);
SHU_GVL.AI.Tsc_2.ToHMI.as := SHU_GVL.ANB.As_Tsc_2_v.ANB;
// Температура силового цилиндра 3
SHU_GVL.ANB.Ps_Tsc_3_n.ANB := VGALG.fnANB_Processing(SHU_GVL.ANB.Ps_Tsc_3_n.ANB_Settings, SHU_GVL.AI.Tsc_3.ToHMI.PV, SHU_GVL.AI.Tsc_3.ToHMI.fault_common, SHU_GVL.ANB.Ps_Tsc_3_n.Ust, SHU_GVL.ANB.Ps_Tsc_3_n.ANB_Internal);
SHU_GVL.AI.Tsc_3.ToHMI.ps := SHU_GVL.ANB.Ps_Tsc_3_n.ANB;
// Температура силового цилиндра 3
SHU_GVL.ANB.Ps_Tsc_3_v.ANB := VGALG.fnANB_Processing(SHU_GVL.ANB.Ps_Tsc_3_v.ANB_Settings, SHU_GVL.AI.Tsc_3.ToHMI.PV, SHU_GVL.AI.Tsc_3.ToHMI.fault_common, SHU_GVL.ANB.Ps_Tsc_3_v.Ust, SHU_GVL.ANB.Ps_Tsc_3_v.ANB_Internal);
SHU_GVL.AI.Tsc_3.ToHMI.ps := SHU_GVL.ANB.Ps_Tsc_3_v.ANB;
// Температура силового цилиндра 3
SHU_GVL.ANB.As_Tsc_3_v.ANB := VGALG.fnANB_Processing(SHU_GVL.ANB.As_Tsc_3_v.ANB_Settings, SHU_GVL.AI.Tsc_3.ToHMI.PV, SHU_GVL.AI.Tsc_3.ToHMI.fault_common, SHU_GVL.ANB.As_Tsc_3_v.Ust, SHU_GVL.ANB.As_Tsc_3_v.ANB_Internal);
SHU_GVL.AI.Tsc_3.ToHMI.as := SHU_GVL.ANB.As_Tsc_3_v.ANB;
// Температура силового цилиндра 4
SHU_GVL.ANB.Ps_Tsc_4_n.ANB := VGALG.fnANB_Processing(SHU_GVL.ANB.Ps_Tsc_4_n.ANB_Settings, SHU_GVL.AI.Tsc_4.ToHMI.PV, SHU_GVL.AI.Tsc_4.ToHMI.fault_common, SHU_GVL.ANB.Ps_Tsc_4_n.Ust, SHU_GVL.ANB.Ps_Tsc_4_n.ANB_Internal);
SHU_GVL.AI.Tsc_4.ToHMI.ps := SHU_GVL.ANB.Ps_Tsc_4_n.ANB;
// Температура силового цилиндра 4
SHU_GVL.ANB.Ps_Tsc_4_v.ANB := VGALG.fnANB_Processing(SHU_GVL.ANB.Ps_Tsc_4_v.ANB_Settings, SHU_GVL.AI.Tsc_4.ToHMI.PV, SHU_GVL.AI.Tsc_4.ToHMI.fault_common, SHU_GVL.ANB.Ps_Tsc_4_v.Ust, SHU_GVL.ANB.Ps_Tsc_4_v.ANB_Internal);
SHU_GVL.AI.Tsc_4.ToHMI.ps := SHU_GVL.ANB.Ps_Tsc_4_v.ANB;
// Температура силового цилиндра 4
SHU_GVL.ANB.As_Tsc_4_v.ANB := VGALG.fnANB_Processing(SHU_GVL.ANB.As_Tsc_4_v.ANB_Settings, SHU_GVL.AI.Tsc_4.ToHMI.PV, SHU_GVL.AI.Tsc_4.ToHMI.fault_common, SHU_GVL.ANB.As_Tsc_4_v.Ust, SHU_GVL.ANB.As_Tsc_4_v.ANB_Internal);
SHU_GVL.AI.Tsc_4.ToHMI.as := SHU_GVL.ANB.As_Tsc_4_v.ANB;
// Температура силового цилиндра 5
SHU_GVL.ANB.Ps_Tsc_5_n.ANB := VGALG.fnANB_Processing(SHU_GVL.ANB.Ps_Tsc_5_n.ANB_Settings, SHU_GVL.AI.Tsc_5.ToHMI.PV, SHU_GVL.AI.Tsc_5.ToHMI.fault_common, SHU_GVL.ANB.Ps_Tsc_5_n.Ust, SHU_GVL.ANB.Ps_Tsc_5_n.ANB_Internal);
SHU_GVL.AI.Tsc_5.ToHMI.ps := SHU_GVL.ANB.Ps_Tsc_5_n.ANB;
// Температура силового цилиндра 5
SHU_GVL.ANB.Ps_Tsc_5_v.ANB := VGALG.fnANB_Processing(SHU_GVL.ANB.Ps_Tsc_5_v.ANB_Settings, SHU_GVL.AI.Tsc_5.ToHMI.PV, SHU_GVL.AI.Tsc_5.ToHMI.fault_common, SHU_GVL.ANB.Ps_Tsc_5_v.Ust, SHU_GVL.ANB.Ps_Tsc_5_v.ANB_Internal);
SHU_GVL.AI.Tsc_5.ToHMI.ps := SHU_GVL.ANB.Ps_Tsc_5_v.ANB;
// Температура силового цилиндра 5
SHU_GVL.ANB.As_Tsc_5_v.ANB := VGALG.fnANB_Processing(SHU_GVL.ANB.As_Tsc_5_v.ANB_Settings, SHU_GVL.AI.Tsc_5.ToHMI.PV, SHU_GVL.AI.Tsc_5.ToHMI.fault_common, SHU_GVL.ANB.As_Tsc_5_v.Ust, SHU_GVL.ANB.As_Tsc_5_v.ANB_Internal);
SHU_GVL.AI.Tsc_5.ToHMI.as := SHU_GVL.ANB.As_Tsc_5_v.ANB;
// Температура силового цилиндра 6
SHU_GVL.ANB.Ps_Tsc_6_n.ANB := VGALG.fnANB_Processing(SHU_GVL.ANB.Ps_Tsc_6_n.ANB_Settings, SHU_GVL.AI.Tsc_6.ToHMI.PV, SHU_GVL.AI.Tsc_6.ToHMI.fault_common, SHU_GVL.ANB.Ps_Tsc_6_n.Ust, SHU_GVL.ANB.Ps_Tsc_6_n.ANB_Internal);
SHU_GVL.AI.Tsc_6.ToHMI.ps := SHU_GVL.ANB.Ps_Tsc_6_n.ANB;
// Температура силового цилиндра 6
SHU_GVL.ANB.Ps_Tsc_6_v.ANB := VGALG.fnANB_Processing(SHU_GVL.ANB.Ps_Tsc_6_v.ANB_Settings, SHU_GVL.AI.Tsc_6.ToHMI.PV, SHU_GVL.AI.Tsc_6.ToHMI.fault_common, SHU_GVL.ANB.Ps_Tsc_6_v.Ust, SHU_GVL.ANB.Ps_Tsc_6_v.ANB_Internal);
SHU_GVL.AI.Tsc_6.ToHMI.ps := SHU_GVL.ANB.Ps_Tsc_6_v.ANB;
// Температура силового цилиндра 6
SHU_GVL.ANB.As_Tsc_6_v.ANB := VGALG.fnANB_Processing(SHU_GVL.ANB.As_Tsc_6_v.ANB_Settings, SHU_GVL.AI.Tsc_6.ToHMI.PV, SHU_GVL.AI.Tsc_6.ToHMI.fault_common, SHU_GVL.ANB.As_Tsc_6_v.Ust, SHU_GVL.ANB.As_Tsc_6_v.ANB_Internal);
SHU_GVL.AI.Tsc_6.ToHMI.as := SHU_GVL.ANB.As_Tsc_6_v.ANB;
// Температура силового цилиндра 7
SHU_GVL.ANB.Ps_Tsc_7_n.ANB := VGALG.fnANB_Processing(SHU_GVL.ANB.Ps_Tsc_7_n.ANB_Settings, SHU_GVL.AI.Tsc_7.ToHMI.PV, SHU_GVL.AI.Tsc_7.ToHMI.fault_common, SHU_GVL.ANB.Ps_Tsc_7_n.Ust, SHU_GVL.ANB.Ps_Tsc_7_n.ANB_Internal);
SHU_GVL.AI.Tsc_7.ToHMI.ps := SHU_GVL.ANB.Ps_Tsc_7_n.ANB;
// Температура силового цилиндра 7
SHU_GVL.ANB.Ps_Tsc_7_v.ANB := VGALG.fnANB_Processing(SHU_GVL.ANB.Ps_Tsc_7_v.ANB_Settings, SHU_GVL.AI.Tsc_7.ToHMI.PV, SHU_GVL.AI.Tsc_7.ToHMI.fault_common, SHU_GVL.ANB.Ps_Tsc_7_v.Ust, SHU_GVL.ANB.Ps_Tsc_7_v.ANB_Internal);
SHU_GVL.AI.Tsc_7.ToHMI.ps := SHU_GVL.ANB.Ps_Tsc_7_v.ANB;
// Температура силового цилиндра 7
SHU_GVL.ANB.As_Tsc_7_v.ANB := VGALG.fnANB_Processing(SHU_GVL.ANB.As_Tsc_7_v.ANB_Settings, SHU_GVL.AI.Tsc_7.ToHMI.PV, SHU_GVL.AI.Tsc_7.ToHMI.fault_common, SHU_GVL.ANB.As_Tsc_7_v.Ust, SHU_GVL.ANB.As_Tsc_7_v.ANB_Internal);
SHU_GVL.AI.Tsc_7.ToHMI.as := SHU_GVL.ANB.As_Tsc_7_v.ANB;
// Температура силового цилиндра 8
SHU_GVL.ANB.Ps_Tsc_8_n.ANB := VGALG.fnANB_Processing(SHU_GVL.ANB.Ps_Tsc_8_n.ANB_Settings, SHU_GVL.AI.Tsc_8.ToHMI.PV, SHU_GVL.AI.Tsc_8.ToHMI.fault_common, SHU_GVL.ANB.Ps_Tsc_8_n.Ust, SHU_GVL.ANB.Ps_Tsc_8_n.ANB_Internal);
SHU_GVL.AI.Tsc_8.ToHMI.ps := SHU_GVL.ANB.Ps_Tsc_8_n.ANB;
// Температура силового цилиндра 8
SHU_GVL.ANB.Ps_Tsc_8_v.ANB := VGALG.fnANB_Processing(SHU_GVL.ANB.Ps_Tsc_8_v.ANB_Settings, SHU_GVL.AI.Tsc_8.ToHMI.PV, SHU_GVL.AI.Tsc_8.ToHMI.fault_common, SHU_GVL.ANB.Ps_Tsc_8_v.Ust, SHU_GVL.ANB.Ps_Tsc_8_v.ANB_Internal);
SHU_GVL.AI.Tsc_8.ToHMI.ps := SHU_GVL.ANB.Ps_Tsc_8_v.ANB;
// Температура силового цилиндра 8
SHU_GVL.ANB.As_Tsc_8_v.ANB := VGALG.fnANB_Processing(SHU_GVL.ANB.As_Tsc_8_v.ANB_Settings, SHU_GVL.AI.Tsc_8.ToHMI.PV, SHU_GVL.AI.Tsc_8.ToHMI.fault_common, SHU_GVL.ANB.As_Tsc_8_v.Ust, SHU_GVL.ANB.As_Tsc_8_v.ANB_Internal);
SHU_GVL.AI.Tsc_8.ToHMI.as := SHU_GVL.ANB.As_Tsc_8_v.ANB;
// Температура силового цилиндра 9
SHU_GVL.ANB.Ps_Tsc_9_n.ANB := VGALG.fnANB_Processing(SHU_GVL.ANB.Ps_Tsc_9_n.ANB_Settings, SHU_GVL.AI.Tsc_9.ToHMI.PV, SHU_GVL.AI.Tsc_9.ToHMI.fault_common, SHU_GVL.ANB.Ps_Tsc_9_n.Ust, SHU_GVL.ANB.Ps_Tsc_9_n.ANB_Internal);
SHU_GVL.AI.Tsc_9.ToHMI.ps := SHU_GVL.ANB.Ps_Tsc_9_n.ANB;
// Температура силового цилиндра 9
SHU_GVL.ANB.Ps_Tsc_9_v.ANB := VGALG.fnANB_Processing(SHU_GVL.ANB.Ps_Tsc_9_v.ANB_Settings, SHU_GVL.AI.Tsc_9.ToHMI.PV, SHU_GVL.AI.Tsc_9.ToHMI.fault_common, SHU_GVL.ANB.Ps_Tsc_9_v.Ust, SHU_GVL.ANB.Ps_Tsc_9_v.ANB_Internal);
SHU_GVL.AI.Tsc_9.ToHMI.ps := SHU_GVL.ANB.Ps_Tsc_9_v.ANB;
// Температура силового цилиндра 9
SHU_GVL.ANB.As_Tsc_9_v.ANB := VGALG.fnANB_Processing(SHU_GVL.ANB.As_Tsc_9_v.ANB_Settings, SHU_GVL.AI.Tsc_9.ToHMI.PV, SHU_GVL.AI.Tsc_9.ToHMI.fault_common, SHU_GVL.ANB.As_Tsc_9_v.Ust, SHU_GVL.ANB.As_Tsc_9_v.ANB_Internal);
SHU_GVL.AI.Tsc_9.ToHMI.as := SHU_GVL.ANB.As_Tsc_9_v.ANB;
// Температура силового цилиндра 10
SHU_GVL.ANB.Ps_Tsc_10_n.ANB := VGALG.fnANB_Processing(SHU_GVL.ANB.Ps_Tsc_10_n.ANB_Settings, SHU_GVL.AI.Tsc_10.ToHMI.PV, SHU_GVL.AI.Tsc_10.ToHMI.fault_common, SHU_GVL.ANB.Ps_Tsc_10_n.Ust, SHU_GVL.ANB.Ps_Tsc_10_n.ANB_Internal);
SHU_GVL.AI.Tsc_10.ToHMI.ps := SHU_GVL.ANB.Ps_Tsc_10_n.ANB;
// Температура силового цилиндра 10
SHU_GVL.ANB.Ps_Tsc_10_v.ANB := VGALG.fnANB_Processing(SHU_GVL.ANB.Ps_Tsc_10_v.ANB_Settings, SHU_GVL.AI.Tsc_10.ToHMI.PV, SHU_GVL.AI.Tsc_10.ToHMI.fault_common, SHU_GVL.ANB.Ps_Tsc_10_v.Ust, SHU_GVL.ANB.Ps_Tsc_10_v.ANB_Internal);
SHU_GVL.AI.Tsc_10.ToHMI.ps := SHU_GVL.ANB.Ps_Tsc_10_v.ANB;
// Температура силового цилиндра 10
SHU_GVL.ANB.As_Tsc_10_v.ANB := VGALG.fnANB_Processing(SHU_GVL.ANB.As_Tsc_10_v.ANB_Settings, SHU_GVL.AI.Tsc_10.ToHMI.PV, SHU_GVL.AI.Tsc_10.ToHMI.fault_common, SHU_GVL.ANB.As_Tsc_10_v.Ust, SHU_GVL.ANB.As_Tsc_10_v.ANB_Internal);
SHU_GVL.AI.Tsc_10.ToHMI.as := SHU_GVL.ANB.As_Tsc_10_v.ANB;
// Температура выхлопных газов в левом коллекторе
SHU_GVL.ANB.Ps_Tvg_lk_n.ANB := VGALG.fnANB_Processing(SHU_GVL.ANB.Ps_Tvg_lk_n.ANB_Settings, SHU_GVL.AI.Tvg_lk.ToHMI.PV, SHU_GVL.AI.Tvg_lk.ToHMI.fault_common, SHU_GVL.ANB.Ps_Tvg_lk_n.Ust, SHU_GVL.ANB.Ps_Tvg_lk_n.ANB_Internal);
SHU_GVL.AI.Tvg_lk.ToHMI.ps := SHU_GVL.ANB.Ps_Tvg_lk_n.ANB;
// Температура выхлопных газов в левом коллекторе
SHU_GVL.ANB.Ps_Tvg_lk_v.ANB := VGALG.fnANB_Processing(SHU_GVL.ANB.Ps_Tvg_lk_v.ANB_Settings, SHU_GVL.AI.Tvg_lk.ToHMI.PV, SHU_GVL.AI.Tvg_lk.ToHMI.fault_common, SHU_GVL.ANB.Ps_Tvg_lk_v.Ust, SHU_GVL.ANB.Ps_Tvg_lk_v.ANB_Internal);
SHU_GVL.AI.Tvg_lk.ToHMI.ps := SHU_GVL.ANB.Ps_Tvg_lk_v.ANB;
// Температура выхлопных газов в левом коллекторе
SHU_GVL.ANB.As_Tvg_lk_v.ANB := VGALG.fnANB_Processing(SHU_GVL.ANB.As_Tvg_lk_v.ANB_Settings, SHU_GVL.AI.Tvg_lk.ToHMI.PV, SHU_GVL.AI.Tvg_lk.ToHMI.fault_common, SHU_GVL.ANB.As_Tvg_lk_v.Ust, SHU_GVL.ANB.As_Tvg_lk_v.ANB_Internal);
SHU_GVL.AI.Tvg_lk.ToHMI.as := SHU_GVL.ANB.As_Tvg_lk_v.ANB;
// Температура выхлопных газов в правом коллекторе
SHU_GVL.ANB.Ps_Tvg_pk_n.ANB := VGALG.fnANB_Processing(SHU_GVL.ANB.Ps_Tvg_pk_n.ANB_Settings, SHU_GVL.AI.Tvg_pk.ToHMI.PV, SHU_GVL.AI.Tvg_pk.ToHMI.fault_common, SHU_GVL.ANB.Ps_Tvg_pk_n.Ust, SHU_GVL.ANB.Ps_Tvg_pk_n.ANB_Internal);
SHU_GVL.AI.Tvg_pk.ToHMI.ps := SHU_GVL.ANB.Ps_Tvg_pk_n.ANB;
// Температура выхлопных газов в правом коллекторе
SHU_GVL.ANB.Ps_Tvg_pk_v.ANB := VGALG.fnANB_Processing(SHU_GVL.ANB.Ps_Tvg_pk_v.ANB_Settings, SHU_GVL.AI.Tvg_pk.ToHMI.PV, SHU_GVL.AI.Tvg_pk.ToHMI.fault_common, SHU_GVL.ANB.Ps_Tvg_pk_v.Ust, SHU_GVL.ANB.Ps_Tvg_pk_v.ANB_Internal);
SHU_GVL.AI.Tvg_pk.ToHMI.ps := SHU_GVL.ANB.Ps_Tvg_pk_v.ANB;
// Температура выхлопных газов в правом коллекторе
SHU_GVL.ANB.As_Tvg_pk_v.ANB := VGALG.fnANB_Processing(SHU_GVL.ANB.As_Tvg_pk_v.ANB_Settings, SHU_GVL.AI.Tvg_pk.ToHMI.PV, SHU_GVL.AI.Tvg_pk.ToHMI.fault_common, SHU_GVL.ANB.As_Tvg_pk_v.Ust, SHU_GVL.ANB.As_Tvg_pk_v.ANB_Internal);
SHU_GVL.AI.Tvg_pk.ToHMI.as := SHU_GVL.ANB.As_Tvg_pk_v.ANB;
// Температура коренного подшипника № 1
SHU_GVL.ANB.Ps_Tkp_1_v.ANB := VGALG.fnANB_Processing(SHU_GVL.ANB.Ps_Tkp_1_v.ANB_Settings, SHU_GVL.AI.Tkp_1.ToHMI.PV, SHU_GVL.AI.Tkp_1.ToHMI.fault_common, SHU_GVL.ANB.Ps_Tkp_1_v.Ust, SHU_GVL.ANB.Ps_Tkp_1_v.ANB_Internal);
SHU_GVL.AI.Tkp_1.ToHMI.ps := SHU_GVL.ANB.Ps_Tkp_1_v.ANB;
// Температура коренного подшипника № 1
SHU_GVL.ANB.As_Tkp_1_v.ANB := VGALG.fnANB_Processing(SHU_GVL.ANB.As_Tkp_1_v.ANB_Settings, SHU_GVL.AI.Tkp_1.ToHMI.PV, SHU_GVL.AI.Tkp_1.ToHMI.fault_common, SHU_GVL.ANB.As_Tkp_1_v.Ust, SHU_GVL.ANB.As_Tkp_1_v.ANB_Internal);
SHU_GVL.AI.Tkp_1.ToHMI.as := SHU_GVL.ANB.As_Tkp_1_v.ANB;
// Температура коренного подшипника № 2
SHU_GVL.ANB.Ps_Tkp_2_v.ANB := VGALG.fnANB_Processing(SHU_GVL.ANB.Ps_Tkp_2_v.ANB_Settings, SHU_GVL.AI.Tkp_2.ToHMI.PV, SHU_GVL.AI.Tkp_2.ToHMI.fault_common, SHU_GVL.ANB.Ps_Tkp_2_v.Ust, SHU_GVL.ANB.Ps_Tkp_2_v.ANB_Internal);
SHU_GVL.AI.Tkp_2.ToHMI.ps := SHU_GVL.ANB.Ps_Tkp_2_v.ANB;
// Температура коренного подшипника № 2
SHU_GVL.ANB.As_Tkp_2_v.ANB := VGALG.fnANB_Processing(SHU_GVL.ANB.As_Tkp_2_v.ANB_Settings, SHU_GVL.AI.Tkp_2.ToHMI.PV, SHU_GVL.AI.Tkp_2.ToHMI.fault_common, SHU_GVL.ANB.As_Tkp_2_v.Ust, SHU_GVL.ANB.As_Tkp_2_v.ANB_Internal);
SHU_GVL.AI.Tkp_2.ToHMI.as := SHU_GVL.ANB.As_Tkp_2_v.ANB;
// Температура коренного подшипника № 3
SHU_GVL.ANB.Ps_Tkp_3_v.ANB := VGALG.fnANB_Processing(SHU_GVL.ANB.Ps_Tkp_3_v.ANB_Settings, SHU_GVL.AI.Tkp_3.ToHMI.PV, SHU_GVL.AI.Tkp_3.ToHMI.fault_common, SHU_GVL.ANB.Ps_Tkp_3_v.Ust, SHU_GVL.ANB.Ps_Tkp_3_v.ANB_Internal);
SHU_GVL.AI.Tkp_3.ToHMI.ps := SHU_GVL.ANB.Ps_Tkp_3_v.ANB;
// Температура коренного подшипника № 3
SHU_GVL.ANB.As_Tkp_3_v.ANB := VGALG.fnANB_Processing(SHU_GVL.ANB.As_Tkp_3_v.ANB_Settings, SHU_GVL.AI.Tkp_3.ToHMI.PV, SHU_GVL.AI.Tkp_3.ToHMI.fault_common, SHU_GVL.ANB.As_Tkp_3_v.Ust, SHU_GVL.ANB.As_Tkp_3_v.ANB_Internal);
SHU_GVL.AI.Tkp_3.ToHMI.as := SHU_GVL.ANB.As_Tkp_3_v.ANB;
// Температура коренного подшипника № 4
SHU_GVL.ANB.Ps_Tkp_4_v.ANB := VGALG.fnANB_Processing(SHU_GVL.ANB.Ps_Tkp_4_v.ANB_Settings, SHU_GVL.AI.Tkp_4.ToHMI.PV, SHU_GVL.AI.Tkp_4.ToHMI.fault_common, SHU_GVL.ANB.Ps_Tkp_4_v.Ust, SHU_GVL.ANB.Ps_Tkp_4_v.ANB_Internal);
SHU_GVL.AI.Tkp_4.ToHMI.ps := SHU_GVL.ANB.Ps_Tkp_4_v.ANB;
// Температура коренного подшипника № 4
SHU_GVL.ANB.As_Tkp_4_v.ANB := VGALG.fnANB_Processing(SHU_GVL.ANB.As_Tkp_4_v.ANB_Settings, SHU_GVL.AI.Tkp_4.ToHMI.PV, SHU_GVL.AI.Tkp_4.ToHMI.fault_common, SHU_GVL.ANB.As_Tkp_4_v.Ust, SHU_GVL.ANB.As_Tkp_4_v.ANB_Internal);
SHU_GVL.AI.Tkp_4.ToHMI.as := SHU_GVL.ANB.As_Tkp_4_v.ANB;
// Температура коренного подшипника № 5
SHU_GVL.ANB.Ps_Tkp_5_v.ANB := VGALG.fnANB_Processing(SHU_GVL.ANB.Ps_Tkp_5_v.ANB_Settings, SHU_GVL.AI.Tkp_5.ToHMI.PV, SHU_GVL.AI.Tkp_5.ToHMI.fault_common, SHU_GVL.ANB.Ps_Tkp_5_v.Ust, SHU_GVL.ANB.Ps_Tkp_5_v.ANB_Internal);
SHU_GVL.AI.Tkp_5.ToHMI.ps := SHU_GVL.ANB.Ps_Tkp_5_v.ANB;
// Температура коренного подшипника № 5
SHU_GVL.ANB.As_Tkp_5_v.ANB := VGALG.fnANB_Processing(SHU_GVL.ANB.As_Tkp_5_v.ANB_Settings, SHU_GVL.AI.Tkp_5.ToHMI.PV, SHU_GVL.AI.Tkp_5.ToHMI.fault_common, SHU_GVL.ANB.As_Tkp_5_v.Ust, SHU_GVL.ANB.As_Tkp_5_v.ANB_Internal);
SHU_GVL.AI.Tkp_5.ToHMI.as := SHU_GVL.ANB.As_Tkp_5_v.ANB;
// Температура коренного подшипника № 6
SHU_GVL.ANB.Ps_Tkp_6_v.ANB := VGALG.fnANB_Processing(SHU_GVL.ANB.Ps_Tkp_6_v.ANB_Settings, SHU_GVL.AI.Tkp_6.ToHMI.PV, SHU_GVL.AI.Tkp_6.ToHMI.fault_common, SHU_GVL.ANB.Ps_Tkp_6_v.Ust, SHU_GVL.ANB.Ps_Tkp_6_v.ANB_Internal);
SHU_GVL.AI.Tkp_6.ToHMI.ps := SHU_GVL.ANB.Ps_Tkp_6_v.ANB;
// Температура коренного подшипника № 6
SHU_GVL.ANB.As_Tkp_6_v.ANB := VGALG.fnANB_Processing(SHU_GVL.ANB.As_Tkp_6_v.ANB_Settings, SHU_GVL.AI.Tkp_6.ToHMI.PV, SHU_GVL.AI.Tkp_6.ToHMI.fault_common, SHU_GVL.ANB.As_Tkp_6_v.Ust, SHU_GVL.ANB.As_Tkp_6_v.ANB_Internal);
SHU_GVL.AI.Tkp_6.ToHMI.as := SHU_GVL.ANB.As_Tkp_6_v.ANB;
// Температура коренного подшипника № 7
SHU_GVL.ANB.Ps_Tkp_7_v.ANB := VGALG.fnANB_Processing(SHU_GVL.ANB.Ps_Tkp_7_v.ANB_Settings, SHU_GVL.AI.Tkp_7.ToHMI.PV, SHU_GVL.AI.Tkp_7.ToHMI.fault_common, SHU_GVL.ANB.Ps_Tkp_7_v.Ust, SHU_GVL.ANB.Ps_Tkp_7_v.ANB_Internal);
SHU_GVL.AI.Tkp_7.ToHMI.ps := SHU_GVL.ANB.Ps_Tkp_7_v.ANB;
// Температура коренного подшипника № 7
SHU_GVL.ANB.As_Tkp_7_v.ANB := VGALG.fnANB_Processing(SHU_GVL.ANB.As_Tkp_7_v.ANB_Settings, SHU_GVL.AI.Tkp_7.ToHMI.PV, SHU_GVL.AI.Tkp_7.ToHMI.fault_common, SHU_GVL.ANB.As_Tkp_7_v.Ust, SHU_GVL.ANB.As_Tkp_7_v.ANB_Internal);
SHU_GVL.AI.Tkp_7.ToHMI.as := SHU_GVL.ANB.As_Tkp_7_v.ANB;
// Температура коренного подшипника № 8
SHU_GVL.ANB.Ps_Tkp_8_v.ANB := VGALG.fnANB_Processing(SHU_GVL.ANB.Ps_Tkp_8_v.ANB_Settings, SHU_GVL.AI.Tkp_8.ToHMI.PV, SHU_GVL.AI.Tkp_8.ToHMI.fault_common, SHU_GVL.ANB.Ps_Tkp_8_v.Ust, SHU_GVL.ANB.Ps_Tkp_8_v.ANB_Internal);
SHU_GVL.AI.Tkp_8.ToHMI.ps := SHU_GVL.ANB.Ps_Tkp_8_v.ANB;
// Температура коренного подшипника № 8
SHU_GVL.ANB.As_Tkp_8_v.ANB := VGALG.fnANB_Processing(SHU_GVL.ANB.As_Tkp_8_v.ANB_Settings, SHU_GVL.AI.Tkp_8.ToHMI.PV, SHU_GVL.AI.Tkp_8.ToHMI.fault_common, SHU_GVL.ANB.As_Tkp_8_v.Ust, SHU_GVL.ANB.As_Tkp_8_v.ANB_Internal);
SHU_GVL.AI.Tkp_8.ToHMI.as := SHU_GVL.ANB.As_Tkp_8_v.ANB;
// Температура коренного подшипника № 9
SHU_GVL.ANB.Ps_Tkp_9_v.ANB := VGALG.fnANB_Processing(SHU_GVL.ANB.Ps_Tkp_9_v.ANB_Settings, SHU_GVL.AI.Tkp_9.ToHMI.PV, SHU_GVL.AI.Tkp_9.ToHMI.fault_common, SHU_GVL.ANB.Ps_Tkp_9_v.Ust, SHU_GVL.ANB.Ps_Tkp_9_v.ANB_Internal);
SHU_GVL.AI.Tkp_9.ToHMI.ps := SHU_GVL.ANB.Ps_Tkp_9_v.ANB;
// Температура коренного подшипника № 9
SHU_GVL.ANB.As_Tkp_9_v.ANB := VGALG.fnANB_Processing(SHU_GVL.ANB.As_Tkp_9_v.ANB_Settings, SHU_GVL.AI.Tkp_9.ToHMI.PV, SHU_GVL.AI.Tkp_9.ToHMI.fault_common, SHU_GVL.ANB.As_Tkp_9_v.Ust, SHU_GVL.ANB.As_Tkp_9_v.ANB_Internal);
SHU_GVL.AI.Tkp_9.ToHMI.as := SHU_GVL.ANB.As_Tkp_9_v.ANB;
// Температура коренного подшипника № 10
SHU_GVL.ANB.Ps_Tkp_10_v.ANB := VGALG.fnANB_Processing(SHU_GVL.ANB.Ps_Tkp_10_v.ANB_Settings, SHU_GVL.AI.Tkp_10.ToHMI.PV, SHU_GVL.AI.Tkp_10.ToHMI.fault_common, SHU_GVL.ANB.Ps_Tkp_10_v.Ust, SHU_GVL.ANB.Ps_Tkp_10_v.ANB_Internal);
SHU_GVL.AI.Tkp_10.ToHMI.ps := SHU_GVL.ANB.Ps_Tkp_10_v.ANB;
// Температура коренного подшипника № 10
SHU_GVL.ANB.As_Tkp_10_v.ANB := VGALG.fnANB_Processing(SHU_GVL.ANB.As_Tkp_10_v.ANB_Settings, SHU_GVL.AI.Tkp_10.ToHMI.PV, SHU_GVL.AI.Tkp_10.ToHMI.fault_common, SHU_GVL.ANB.As_Tkp_10_v.Ust, SHU_GVL.ANB.As_Tkp_10_v.ANB_Internal);
SHU_GVL.AI.Tkp_10.ToHMI.as := SHU_GVL.ANB.As_Tkp_10_v.ANB;
// Температура воды на выходе из двигателя
SHU_GVL.ANB.Ps_Tv_outD_v.ANB := VGALG.fnANB_Processing(SHU_GVL.ANB.Ps_Tv_outD_v.ANB_Settings, SHU_GVL.AI.Tv_outD.ToHMI.PV, SHU_GVL.AI.Tv_outD.ToHMI.fault_common, SHU_GVL.ANB.Ps_Tv_outD_v.Ust, SHU_GVL.ANB.Ps_Tv_outD_v.ANB_Internal);
SHU_GVL.AI.Tv_outD.ToHMI.ps := SHU_GVL.ANB.Ps_Tv_outD_v.ANB;
// Температура воды на выходе из двигателя
SHU_GVL.ANB.As_Tv_outD_v.ANB := VGALG.fnANB_Processing(SHU_GVL.ANB.As_Tv_outD_v.ANB_Settings, SHU_GVL.AI.Tv_outD.ToHMI.PV, SHU_GVL.AI.Tv_outD.ToHMI.fault_common, SHU_GVL.ANB.As_Tv_outD_v.Ust, SHU_GVL.ANB.As_Tv_outD_v.ANB_Internal);
SHU_GVL.AI.Tv_outD.ToHMI.as := SHU_GVL.ANB.As_Tv_outD_v.ANB;
// Температура масла на входе в ГМК
SHU_GVL.ANB.Ps_Tm_inGMK_n.ANB := VGALG.fnANB_Processing(SHU_GVL.ANB.Ps_Tm_inGMK_n.ANB_Settings, SHU_GVL.AI.Tm_inGMK.ToHMI.PV, SHU_GVL.AI.Tm_inGMK.ToHMI.fault_common, SHU_GVL.ANB.Ps_Tm_inGMK_n.Ust, SHU_GVL.ANB.Ps_Tm_inGMK_n.ANB_Internal);
SHU_GVL.AI.Tm_inGMK.ToHMI.ps := SHU_GVL.ANB.Ps_Tm_inGMK_n.ANB;
// Температура масла на выходе из ГМК
SHU_GVL.ANB.Ps_Tm_outGMK_v.ANB := VGALG.fnANB_Processing(SHU_GVL.ANB.Ps_Tm_outGMK_v.ANB_Settings, SHU_GVL.AI.Tm_outGMK.ToHMI.PV, SHU_GVL.AI.Tm_outGMK.ToHMI.fault_common, SHU_GVL.ANB.Ps_Tm_outGMK_v.Ust, SHU_GVL.ANB.Ps_Tm_outGMK_v.ANB_Internal);
SHU_GVL.AI.Tm_outGMK.ToHMI.ps := SHU_GVL.ANB.Ps_Tm_outGMK_v.ANB;
// Температура масла на выходе из ГМК
SHU_GVL.ANB.As_Tm_outGMK_v.ANB := VGALG.fnANB_Processing(SHU_GVL.ANB.As_Tm_outGMK_v.ANB_Settings, SHU_GVL.AI.Tm_outGMK.ToHMI.PV, SHU_GVL.AI.Tm_outGMK.ToHMI.fault_common, SHU_GVL.ANB.As_Tm_outGMK_v.Ust, SHU_GVL.ANB.As_Tm_outGMK_v.ANB_Internal);
SHU_GVL.AI.Tm_outGMK.ToHMI.as := SHU_GVL.ANB.As_Tm_outGMK_v.ANB;
// Температура газа на выходе компрессорного цилиндра 1
SHU_GVL.ANB.Ps_Tg_outKC_1_v.ANB := VGALG.fnANB_Processing(SHU_GVL.ANB.Ps_Tg_outKC_1_v.ANB_Settings, SHU_GVL.AI.Tg_outKC_1.ToHMI.PV, SHU_GVL.AI.Tg_outKC_1.ToHMI.fault_common, SHU_GVL.ANB.Ps_Tg_outKC_1_v.Ust, SHU_GVL.ANB.Ps_Tg_outKC_1_v.ANB_Internal);
SHU_GVL.AI.Tg_outKC_1.ToHMI.ps := SHU_GVL.ANB.Ps_Tg_outKC_1_v.ANB;
// Температура газа на выходе компрессорного цилиндра 1
SHU_GVL.ANB.As_Tg_outKC_1_v.ANB := VGALG.fnANB_Processing(SHU_GVL.ANB.As_Tg_outKC_1_v.ANB_Settings, SHU_GVL.AI.Tg_outKC_1.ToHMI.PV, SHU_GVL.AI.Tg_outKC_1.ToHMI.fault_common, SHU_GVL.ANB.As_Tg_outKC_1_v.Ust, SHU_GVL.ANB.As_Tg_outKC_1_v.ANB_Internal);
SHU_GVL.AI.Tg_outKC_1.ToHMI.as := SHU_GVL.ANB.As_Tg_outKC_1_v.ANB;
// Температура газа на выходе компрессорного цилиндра 2
SHU_GVL.ANB.Ps_Tg_outKC_2_v.ANB := VGALG.fnANB_Processing(SHU_GVL.ANB.Ps_Tg_outKC_2_v.ANB_Settings, SHU_GVL.AI.Tg_outKC_2.ToHMI.PV, SHU_GVL.AI.Tg_outKC_2.ToHMI.fault_common, SHU_GVL.ANB.Ps_Tg_outKC_2_v.Ust, SHU_GVL.ANB.Ps_Tg_outKC_2_v.ANB_Internal);
SHU_GVL.AI.Tg_outKC_2.ToHMI.ps := SHU_GVL.ANB.Ps_Tg_outKC_2_v.ANB;
// Температура газа на выходе компрессорного цилиндра 2
SHU_GVL.ANB.As_Tg_outKC_2_v.ANB := VGALG.fnANB_Processing(SHU_GVL.ANB.As_Tg_outKC_2_v.ANB_Settings, SHU_GVL.AI.Tg_outKC_2.ToHMI.PV, SHU_GVL.AI.Tg_outKC_2.ToHMI.fault_common, SHU_GVL.ANB.As_Tg_outKC_2_v.Ust, SHU_GVL.ANB.As_Tg_outKC_2_v.ANB_Internal);
SHU_GVL.AI.Tg_outKC_2.ToHMI.as := SHU_GVL.ANB.As_Tg_outKC_2_v.ANB;
// Температура газа на выходе компрессорного цилиндра 3
SHU_GVL.ANB.Ps_Tg_outKC_3_v.ANB := VGALG.fnANB_Processing(SHU_GVL.ANB.Ps_Tg_outKC_3_v.ANB_Settings, SHU_GVL.AI.Tg_outKC_3.ToHMI.PV, SHU_GVL.AI.Tg_outKC_3.ToHMI.fault_common, SHU_GVL.ANB.Ps_Tg_outKC_3_v.Ust, SHU_GVL.ANB.Ps_Tg_outKC_3_v.ANB_Internal);
SHU_GVL.AI.Tg_outKC_3.ToHMI.ps := SHU_GVL.ANB.Ps_Tg_outKC_3_v.ANB;
// Температура газа на выходе компрессорного цилиндра 3
SHU_GVL.ANB.As_Tg_outKC_3_v.ANB := VGALG.fnANB_Processing(SHU_GVL.ANB.As_Tg_outKC_3_v.ANB_Settings, SHU_GVL.AI.Tg_outKC_3.ToHMI.PV, SHU_GVL.AI.Tg_outKC_3.ToHMI.fault_common, SHU_GVL.ANB.As_Tg_outKC_3_v.Ust, SHU_GVL.ANB.As_Tg_outKC_3_v.ANB_Internal);
SHU_GVL.AI.Tg_outKC_3.ToHMI.as := SHU_GVL.ANB.As_Tg_outKC_3_v.ANB;
// Температура газа на выходе компрессорного цилиндра 4
SHU_GVL.ANB.Ps_Tg_outKC_4_v.ANB := VGALG.fnANB_Processing(SHU_GVL.ANB.Ps_Tg_outKC_4_v.ANB_Settings, SHU_GVL.AI.Tg_outKC_4.ToHMI.PV, SHU_GVL.AI.Tg_outKC_4.ToHMI.fault_common, SHU_GVL.ANB.Ps_Tg_outKC_4_v.Ust, SHU_GVL.ANB.Ps_Tg_outKC_4_v.ANB_Internal);
SHU_GVL.AI.Tg_outKC_4.ToHMI.ps := SHU_GVL.ANB.Ps_Tg_outKC_4_v.ANB;
// Температура газа на выходе компрессорного цилиндра 4
SHU_GVL.ANB.As_Tg_outKC_4_v.ANB := VGALG.fnANB_Processing(SHU_GVL.ANB.As_Tg_outKC_4_v.ANB_Settings, SHU_GVL.AI.Tg_outKC_4.ToHMI.PV, SHU_GVL.AI.Tg_outKC_4.ToHMI.fault_common, SHU_GVL.ANB.As_Tg_outKC_4_v.Ust, SHU_GVL.ANB.As_Tg_outKC_4_v.ANB_Internal);
SHU_GVL.AI.Tg_outKC_4.ToHMI.as := SHU_GVL.ANB.As_Tg_outKC_4_v.ANB;
// Температура газа на выходе компрессорного цилиндра 5
SHU_GVL.ANB.Ps_Tg_outKC_5_v.ANB := VGALG.fnANB_Processing(SHU_GVL.ANB.Ps_Tg_outKC_5_v.ANB_Settings, SHU_GVL.AI.Tg_outKC_5.ToHMI.PV, SHU_GVL.AI.Tg_outKC_5.ToHMI.fault_common, SHU_GVL.ANB.Ps_Tg_outKC_5_v.Ust, SHU_GVL.ANB.Ps_Tg_outKC_5_v.ANB_Internal);
SHU_GVL.AI.Tg_outKC_5.ToHMI.ps := SHU_GVL.ANB.Ps_Tg_outKC_5_v.ANB;
// Температура газа на выходе компрессорного цилиндра 5
SHU_GVL.ANB.As_Tg_outKC_5_v.ANB := VGALG.fnANB_Processing(SHU_GVL.ANB.As_Tg_outKC_5_v.ANB_Settings, SHU_GVL.AI.Tg_outKC_5.ToHMI.PV, SHU_GVL.AI.Tg_outKC_5.ToHMI.fault_common, SHU_GVL.ANB.As_Tg_outKC_5_v.Ust, SHU_GVL.ANB.As_Tg_outKC_5_v.ANB_Internal);
SHU_GVL.AI.Tg_outKC_5.ToHMI.as := SHU_GVL.ANB.As_Tg_outKC_5_v.ANB;
// Давление газа на входе в ГМК
SHU_GVL.ANB.Ps_Pg_inGMK_n.ANB := VGALG.fnANB_Processing(SHU_GVL.ANB.Ps_Pg_inGMK_n.ANB_Settings, SHU_GVL.AI.Pg_inGMK.ToHMI.PV, SHU_GVL.AI.Pg_inGMK.ToHMI.fault_common, SHU_GVL.ANB.Ps_Pg_inGMK_n.Ust, SHU_GVL.ANB.Ps_Pg_inGMK_n.ANB_Internal);
SHU_GVL.AI.Pg_inGMK.ToHMI.ps := SHU_GVL.ANB.Ps_Pg_inGMK_n.ANB;
// Давление газа на входе в ГМК
SHU_GVL.ANB.Ps_Pg_inGMK_v.ANB := VGALG.fnANB_Processing(SHU_GVL.ANB.Ps_Pg_inGMK_v.ANB_Settings, SHU_GVL.AI.Pg_inGMK.ToHMI.PV, SHU_GVL.AI.Pg_inGMK.ToHMI.fault_common, SHU_GVL.ANB.Ps_Pg_inGMK_v.Ust, SHU_GVL.ANB.Ps_Pg_inGMK_v.ANB_Internal);
SHU_GVL.AI.Pg_inGMK.ToHMI.ps := SHU_GVL.ANB.Ps_Pg_inGMK_v.ANB;
// Давление газа на выходе из ГМК
SHU_GVL.ANB.Ps_Pg_outGMK_SHU_GMK_v.ANB := VGALG.fnANB_Processing(SHU_GVL.ANB.Ps_Pg_outGMK_SHU_GMK_v.ANB_Settings, SHU_GVL.AI.Pg_outGMK_SHU_GMK.ToHMI.PV, SHU_GVL.AI.Pg_outGMK_SHU_GMK.ToHMI.fault_common, SHU_GVL.ANB.Ps_Pg_outGMK_SHU_GMK_v.Ust, SHU_GVL.ANB.Ps_Pg_outGMK_SHU_GMK_v.ANB_Internal);
SHU_GVL.AI.Pg_outGMK_SHU_GMK.ToHMI.ps := SHU_GVL.ANB.Ps_Pg_outGMK_SHU_GMK_v.ANB;
// Давление газа на выходе из ГМК
SHU_GVL.ANB.As_Pg_outGMK_SHU_GMK_v.ANB := VGALG.fnANB_Processing(SHU_GVL.ANB.As_Pg_outGMK_SHU_GMK_v.ANB_Settings, SHU_GVL.AI.Pg_outGMK_SHU_GMK.ToHMI.PV, SHU_GVL.AI.Pg_outGMK_SHU_GMK.ToHMI.fault_common, SHU_GVL.ANB.As_Pg_outGMK_SHU_GMK_v.Ust, SHU_GVL.ANB.As_Pg_outGMK_SHU_GMK_v.ANB_Internal);
SHU_GVL.AI.Pg_outGMK_SHU_GMK.ToHMI.as := SHU_GVL.ANB.As_Pg_outGMK_SHU_GMK_v.ANB;
// Давление пускового воздуха
SHU_GVL.ANB.Ps_Ppv_n.ANB := VGALG.fnANB_Processing(SHU_GVL.ANB.Ps_Ppv_n.ANB_Settings, SHU_GVL.AI.Ppv.ToHMI.PV, SHU_GVL.AI.Ppv.ToHMI.fault_common, SHU_GVL.ANB.Ps_Ppv_n.Ust, SHU_GVL.ANB.Ps_Ppv_n.ANB_Internal);
SHU_GVL.AI.Ppv.ToHMI.ps := SHU_GVL.ANB.Ps_Ppv_n.ANB;
// Давление топливного газа до ТРК
SHU_GVL.ANB.Ps_Ptg_inTRK_n.ANB := VGALG.fnANB_Processing(SHU_GVL.ANB.Ps_Ptg_inTRK_n.ANB_Settings, SHU_GVL.AI.Ptg_inTRK.ToHMI.PV, SHU_GVL.AI.Ptg_inTRK.ToHMI.fault_common, SHU_GVL.ANB.Ps_Ptg_inTRK_n.Ust, SHU_GVL.ANB.Ps_Ptg_inTRK_n.ANB_Internal);
SHU_GVL.AI.Ptg_inTRK.ToHMI.ps := SHU_GVL.ANB.Ps_Ptg_inTRK_n.ANB;
// Давление топливного газа до ТРК
SHU_GVL.ANB.Ps_Ptg_inTRK_v.ANB := VGALG.fnANB_Processing(SHU_GVL.ANB.Ps_Ptg_inTRK_v.ANB_Settings, SHU_GVL.AI.Ptg_inTRK.ToHMI.PV, SHU_GVL.AI.Ptg_inTRK.ToHMI.fault_common, SHU_GVL.ANB.Ps_Ptg_inTRK_v.Ust, SHU_GVL.ANB.Ps_Ptg_inTRK_v.ANB_Internal);
SHU_GVL.AI.Ptg_inTRK.ToHMI.ps := SHU_GVL.ANB.Ps_Ptg_inTRK_v.ANB;
// Давление топливного газа до ТРК
SHU_GVL.ANB.As_Ptg_inTRK_n.ANB := VGALG.fnANB_Processing(SHU_GVL.ANB.As_Ptg_inTRK_n.ANB_Settings, SHU_GVL.AI.Ptg_inTRK.ToHMI.PV, SHU_GVL.AI.Ptg_inTRK.ToHMI.fault_common, SHU_GVL.ANB.As_Ptg_inTRK_n.Ust, SHU_GVL.ANB.As_Ptg_inTRK_n.ANB_Internal);
SHU_GVL.AI.Ptg_inTRK.ToHMI.as := SHU_GVL.ANB.As_Ptg_inTRK_n.ANB;
// Давление топливного газа до ТРК
SHU_GVL.ANB.As_Ptg_inTRK_v.ANB := VGALG.fnANB_Processing(SHU_GVL.ANB.As_Ptg_inTRK_v.ANB_Settings, SHU_GVL.AI.Ptg_inTRK.ToHMI.PV, SHU_GVL.AI.Ptg_inTRK.ToHMI.fault_common, SHU_GVL.ANB.As_Ptg_inTRK_v.Ust, SHU_GVL.ANB.As_Ptg_inTRK_v.ANB_Internal);
SHU_GVL.AI.Ptg_inTRK.ToHMI.as := SHU_GVL.ANB.As_Ptg_inTRK_v.ANB;
// Давление масла на входе в турбокомпрессоры
SHU_GVL.ANB.Ps_Pm_inTK_n.ANB := VGALG.fnANB_Processing(SHU_GVL.ANB.Ps_Pm_inTK_n.ANB_Settings, SHU_GVL.AI.Pm_inTK.ToHMI.PV, SHU_GVL.AI.Pm_inTK.ToHMI.fault_common, SHU_GVL.ANB.Ps_Pm_inTK_n.Ust, SHU_GVL.ANB.Ps_Pm_inTK_n.ANB_Internal);
SHU_GVL.AI.Pm_inTK.ToHMI.ps := SHU_GVL.ANB.Ps_Pm_inTK_n.ANB;
// Давление масла на входе в турбокомпрессоры
SHU_GVL.ANB.As_Pm_inTK_n.ANB := VGALG.fnANB_Processing(SHU_GVL.ANB.As_Pm_inTK_n.ANB_Settings, SHU_GVL.AI.Pm_inTK.ToHMI.PV, SHU_GVL.AI.Pm_inTK.ToHMI.fault_common, SHU_GVL.ANB.As_Pm_inTK_n.Ust, SHU_GVL.ANB.As_Pm_inTK_n.ANB_Internal);
SHU_GVL.AI.Pm_inTK.ToHMI.as := SHU_GVL.ANB.As_Pm_inTK_n.ANB;
// Давление масла на входе в двигатель
SHU_GVL.ANB.Ps_Pm_inD_SHU_GMK_n.ANB := VGALG.fnANB_Processing(SHU_GVL.ANB.Ps_Pm_inD_SHU_GMK_n.ANB_Settings, SHU_GVL.AI.Pm_inD_SHU_GMK.ToHMI.PV, SHU_GVL.AI.Pm_inD_SHU_GMK.ToHMI.fault_common, SHU_GVL.ANB.Ps_Pm_inD_SHU_GMK_n.Ust, SHU_GVL.ANB.Ps_Pm_inD_SHU_GMK_n.ANB_Internal);
SHU_GVL.AI.Pm_inD_SHU_GMK.ToHMI.ps := SHU_GVL.ANB.Ps_Pm_inD_SHU_GMK_n.ANB;
// Давление масла на входе в двигатель
SHU_GVL.ANB.As_Pm_inD_SHU_GMK_n.ANB := VGALG.fnANB_Processing(SHU_GVL.ANB.As_Pm_inD_SHU_GMK_n.ANB_Settings, SHU_GVL.AI.Pm_inD_SHU_GMK.ToHMI.PV, SHU_GVL.AI.Pm_inD_SHU_GMK.ToHMI.fault_common, SHU_GVL.ANB.As_Pm_inD_SHU_GMK_n.Ust, SHU_GVL.ANB.As_Pm_inD_SHU_GMK_n.ANB_Internal);
SHU_GVL.AI.Pm_inD_SHU_GMK.ToHMI.as := SHU_GVL.ANB.As_Pm_inD_SHU_GMK_n.ANB;
// Перепад давления масла на фильтре
SHU_GVL.ANB.Ps_dPmf_v.ANB := VGALG.fnANB_Processing(SHU_GVL.ANB.Ps_dPmf_v.ANB_Settings, SHU_GVL.AI.dPmf.ToHMI.PV, SHU_GVL.AI.dPmf.ToHMI.fault_common, SHU_GVL.ANB.Ps_dPmf_v.Ust, SHU_GVL.ANB.Ps_dPmf_v.ANB_Internal);
SHU_GVL.AI.dPmf.ToHMI.ps := SHU_GVL.ANB.Ps_dPmf_v.ANB;
// Давление воды на выходе из двигателя
SHU_GVL.ANB.As_Pv_outD_n.ANB := VGALG.fnANB_Processing(SHU_GVL.ANB.As_Pv_outD_n.ANB_Settings, SHU_GVL.AI.Pv_outD.ToHMI.PV, SHU_GVL.AI.Pv_outD.ToHMI.fault_common, SHU_GVL.ANB.As_Pv_outD_n.Ust, SHU_GVL.ANB.As_Pv_outD_n.ANB_Internal);
SHU_GVL.AI.Pv_outD.ToHMI.as := SHU_GVL.ANB.As_Pv_outD_n.ANB;
// Уровень вибрации ГМК (виброскорость), канал 1
SHU_GVL.ANB.Ps_Vb_Ch_1_v.ANB := VGALG.fnANB_Processing(SHU_GVL.ANB.Ps_Vb_Ch_1_v.ANB_Settings, SHU_GVL.AI.Vb_Ch_1.ToHMI.PV, SHU_GVL.AI.Vb_Ch_1.ToHMI.fault_common, SHU_GVL.ANB.Ps_Vb_Ch_1_v.Ust, SHU_GVL.ANB.Ps_Vb_Ch_1_v.ANB_Internal);
SHU_GVL.AI.Vb_Ch_1.ToHMI.ps := SHU_GVL.ANB.Ps_Vb_Ch_1_v.ANB;
// Уровень вибрации ГМК (виброскорость), канал 1
SHU_GVL.ANB.As_Vb_Ch_1_v.ANB := VGALG.fnANB_Processing(SHU_GVL.ANB.As_Vb_Ch_1_v.ANB_Settings, SHU_GVL.AI.Vb_Ch_1.ToHMI.PV, SHU_GVL.AI.Vb_Ch_1.ToHMI.fault_common, SHU_GVL.ANB.As_Vb_Ch_1_v.Ust, SHU_GVL.ANB.As_Vb_Ch_1_v.ANB_Internal);
SHU_GVL.AI.Vb_Ch_1.ToHMI.as := SHU_GVL.ANB.As_Vb_Ch_1_v.ANB;
// Уровень вибрации ГМК (виброскорость), канал 2
SHU_GVL.ANB.Ps_Vb_Ch_2_v.ANB := VGALG.fnANB_Processing(SHU_GVL.ANB.Ps_Vb_Ch_2_v.ANB_Settings, SHU_GVL.AI.Vb_Ch_2.ToHMI.PV, SHU_GVL.AI.Vb_Ch_2.ToHMI.fault_common, SHU_GVL.ANB.Ps_Vb_Ch_2_v.Ust, SHU_GVL.ANB.Ps_Vb_Ch_2_v.ANB_Internal);
SHU_GVL.AI.Vb_Ch_2.ToHMI.ps := SHU_GVL.ANB.Ps_Vb_Ch_2_v.ANB;
// Уровень вибрации ГМК (виброскорость), канал 2
SHU_GVL.ANB.As_Vb_Ch_2_v.ANB := VGALG.fnANB_Processing(SHU_GVL.ANB.As_Vb_Ch_2_v.ANB_Settings, SHU_GVL.AI.Vb_Ch_2.ToHMI.PV, SHU_GVL.AI.Vb_Ch_2.ToHMI.fault_common, SHU_GVL.ANB.As_Vb_Ch_2_v.Ust, SHU_GVL.ANB.As_Vb_Ch_2_v.ANB_Internal);
SHU_GVL.AI.Vb_Ch_2.ToHMI.as := SHU_GVL.ANB.As_Vb_Ch_2_v.ANB;
"""
proj = projects.primary
folder = proj.find('ANB SHU', recursive=True)[0]
struktur = folder.create_pou('SHU_ANB_Call', type = PouType.Function,language=None, return_type='BOOL', base_type=None, interfaces=None)
struktur.textual_declaration.insert(4, 0, CONTENT_var)
struktur.textual_implementation.insert(0, 0, CONTENT_body)
