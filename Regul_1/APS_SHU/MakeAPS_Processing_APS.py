#encoding:utf-8
from __future__ import print_function
CONTENT_var = """\
 unlock:BOOL;
END_VAR
VAR_IN_OUT
    i: INT;
    FirstOutIndex: INT;
    new_wrn: BOOL;
    new_crs: BOOL;
    AlarmTarget: ARRAY[0..8] OF BOOL;
"""
CONTENT_body = """\
//[ШУ ГМК] Температура силового цилиндра 1
VGALG.fnAPS_Processing(SHU_GVL.ANB.Ps_Tsc_1_n.ANB, 0.1, unlock, SHU_GVL.APS.Ps_Tsc_1_n.Intern, FirstOutIndex, i, SHU_GVL.APS.Ps_Tsc_1_n.PV, new_wrn, new_crs, SHU_GVL.Alarms, AlarmTarget);
//[ШУ ГМК] Температура силового цилиндра 1
VGALG.fnAPS_Processing(SHU_GVL.ANB.Ps_Tsc_1_v.ANB, 0.1, unlock, SHU_GVL.APS.Ps_Tsc_1_v.Intern, FirstOutIndex, i, SHU_GVL.APS.Ps_Tsc_1_v.PV, new_wrn, new_crs, SHU_GVL.Alarms, AlarmTarget);
//[ШУ ГМК] Температура силового цилиндра 1
VGALG.fnAPS_Processing(SHU_GVL.ANB.As_Tsc_1_v.ANB, 0.1, unlock, SHU_GVL.APS.As_Tsc_1_v.Intern, FirstOutIndex, i, SHU_GVL.APS.As_Tsc_1_v.PV, new_wrn, new_crs, SHU_GVL.Alarms, AlarmTarget);
//[ШУ ГМК] Температура силового цилиндра 2
VGALG.fnAPS_Processing(SHU_GVL.ANB.Ps_Tsc_2_n.ANB, 0.1, unlock, SHU_GVL.APS.Ps_Tsc_2_n.Intern, FirstOutIndex, i, SHU_GVL.APS.Ps_Tsc_2_n.PV, new_wrn, new_crs, SHU_GVL.Alarms, AlarmTarget);
//[ШУ ГМК] Температура силового цилиндра 2
VGALG.fnAPS_Processing(SHU_GVL.ANB.Ps_Tsc_2_v.ANB, 0.1, unlock, SHU_GVL.APS.Ps_Tsc_2_v.Intern, FirstOutIndex, i, SHU_GVL.APS.Ps_Tsc_2_v.PV, new_wrn, new_crs, SHU_GVL.Alarms, AlarmTarget);
//[ШУ ГМК] Температура силового цилиндра 2
VGALG.fnAPS_Processing(SHU_GVL.ANB.As_Tsc_2_v.ANB, 0.1, unlock, SHU_GVL.APS.As_Tsc_2_v.Intern, FirstOutIndex, i, SHU_GVL.APS.As_Tsc_2_v.PV, new_wrn, new_crs, SHU_GVL.Alarms, AlarmTarget);
//[ШУ ГМК] Температура силового цилиндра 3
VGALG.fnAPS_Processing(SHU_GVL.ANB.Ps_Tsc_3_n.ANB, 0.1, unlock, SHU_GVL.APS.Ps_Tsc_3_n.Intern, FirstOutIndex, i, SHU_GVL.APS.Ps_Tsc_3_n.PV, new_wrn, new_crs, SHU_GVL.Alarms, AlarmTarget);
//[ШУ ГМК] Температура силового цилиндра 3
VGALG.fnAPS_Processing(SHU_GVL.ANB.Ps_Tsc_3_v.ANB, 0.1, unlock, SHU_GVL.APS.Ps_Tsc_3_v.Intern, FirstOutIndex, i, SHU_GVL.APS.Ps_Tsc_3_v.PV, new_wrn, new_crs, SHU_GVL.Alarms, AlarmTarget);
//[ШУ ГМК] Температура силового цилиндра 3
VGALG.fnAPS_Processing(SHU_GVL.ANB.As_Tsc_3_v.ANB, 0.1, unlock, SHU_GVL.APS.As_Tsc_3_v.Intern, FirstOutIndex, i, SHU_GVL.APS.As_Tsc_3_v.PV, new_wrn, new_crs, SHU_GVL.Alarms, AlarmTarget);
//[ШУ ГМК] Температура силового цилиндра 4
VGALG.fnAPS_Processing(SHU_GVL.ANB.Ps_Tsc_4_n.ANB, 0.1, unlock, SHU_GVL.APS.Ps_Tsc_4_n.Intern, FirstOutIndex, i, SHU_GVL.APS.Ps_Tsc_4_n.PV, new_wrn, new_crs, SHU_GVL.Alarms, AlarmTarget);
//[ШУ ГМК] Температура силового цилиндра 4
VGALG.fnAPS_Processing(SHU_GVL.ANB.Ps_Tsc_4_v.ANB, 0.1, unlock, SHU_GVL.APS.Ps_Tsc_4_v.Intern, FirstOutIndex, i, SHU_GVL.APS.Ps_Tsc_4_v.PV, new_wrn, new_crs, SHU_GVL.Alarms, AlarmTarget);
//[ШУ ГМК] Температура силового цилиндра 4
VGALG.fnAPS_Processing(SHU_GVL.ANB.As_Tsc_4_v.ANB, 0.1, unlock, SHU_GVL.APS.As_Tsc_4_v.Intern, FirstOutIndex, i, SHU_GVL.APS.As_Tsc_4_v.PV, new_wrn, new_crs, SHU_GVL.Alarms, AlarmTarget);
//[ШУ ГМК] Температура силового цилиндра 5
VGALG.fnAPS_Processing(SHU_GVL.ANB.Ps_Tsc_5_n.ANB, 0.1, unlock, SHU_GVL.APS.Ps_Tsc_5_n.Intern, FirstOutIndex, i, SHU_GVL.APS.Ps_Tsc_5_n.PV, new_wrn, new_crs, SHU_GVL.Alarms, AlarmTarget);
//[ШУ ГМК] Температура силового цилиндра 5
VGALG.fnAPS_Processing(SHU_GVL.ANB.Ps_Tsc_5_v.ANB, 0.1, unlock, SHU_GVL.APS.Ps_Tsc_5_v.Intern, FirstOutIndex, i, SHU_GVL.APS.Ps_Tsc_5_v.PV, new_wrn, new_crs, SHU_GVL.Alarms, AlarmTarget);
//[ШУ ГМК] Температура силового цилиндра 5
VGALG.fnAPS_Processing(SHU_GVL.ANB.As_Tsc_5_v.ANB, 0.1, unlock, SHU_GVL.APS.As_Tsc_5_v.Intern, FirstOutIndex, i, SHU_GVL.APS.As_Tsc_5_v.PV, new_wrn, new_crs, SHU_GVL.Alarms, AlarmTarget);
//[ШУ ГМК] Температура силового цилиндра 6
VGALG.fnAPS_Processing(SHU_GVL.ANB.Ps_Tsc_6_n.ANB, 0.1, unlock, SHU_GVL.APS.Ps_Tsc_6_n.Intern, FirstOutIndex, i, SHU_GVL.APS.Ps_Tsc_6_n.PV, new_wrn, new_crs, SHU_GVL.Alarms, AlarmTarget);
//[ШУ ГМК] Температура силового цилиндра 6
VGALG.fnAPS_Processing(SHU_GVL.ANB.Ps_Tsc_6_v.ANB, 0.1, unlock, SHU_GVL.APS.Ps_Tsc_6_v.Intern, FirstOutIndex, i, SHU_GVL.APS.Ps_Tsc_6_v.PV, new_wrn, new_crs, SHU_GVL.Alarms, AlarmTarget);
//[ШУ ГМК] Температура силового цилиндра 6
VGALG.fnAPS_Processing(SHU_GVL.ANB.As_Tsc_6_v.ANB, 0.1, unlock, SHU_GVL.APS.As_Tsc_6_v.Intern, FirstOutIndex, i, SHU_GVL.APS.As_Tsc_6_v.PV, new_wrn, new_crs, SHU_GVL.Alarms, AlarmTarget);
//[ШУ ГМК] Температура силового цилиндра 7
VGALG.fnAPS_Processing(SHU_GVL.ANB.Ps_Tsc_7_n.ANB, 0.1, unlock, SHU_GVL.APS.Ps_Tsc_7_n.Intern, FirstOutIndex, i, SHU_GVL.APS.Ps_Tsc_7_n.PV, new_wrn, new_crs, SHU_GVL.Alarms, AlarmTarget);
//[ШУ ГМК] Температура силового цилиндра 7
VGALG.fnAPS_Processing(SHU_GVL.ANB.Ps_Tsc_7_v.ANB, 0.1, unlock, SHU_GVL.APS.Ps_Tsc_7_v.Intern, FirstOutIndex, i, SHU_GVL.APS.Ps_Tsc_7_v.PV, new_wrn, new_crs, SHU_GVL.Alarms, AlarmTarget);
//[ШУ ГМК] Температура силового цилиндра 7
VGALG.fnAPS_Processing(SHU_GVL.ANB.As_Tsc_7_v.ANB, 0.1, unlock, SHU_GVL.APS.As_Tsc_7_v.Intern, FirstOutIndex, i, SHU_GVL.APS.As_Tsc_7_v.PV, new_wrn, new_crs, SHU_GVL.Alarms, AlarmTarget);
//[ШУ ГМК] Температура силового цилиндра 8
VGALG.fnAPS_Processing(SHU_GVL.ANB.Ps_Tsc_8_n.ANB, 0.1, unlock, SHU_GVL.APS.Ps_Tsc_8_n.Intern, FirstOutIndex, i, SHU_GVL.APS.Ps_Tsc_8_n.PV, new_wrn, new_crs, SHU_GVL.Alarms, AlarmTarget);
//[ШУ ГМК] Температура силового цилиндра 8
VGALG.fnAPS_Processing(SHU_GVL.ANB.Ps_Tsc_8_v.ANB, 0.1, unlock, SHU_GVL.APS.Ps_Tsc_8_v.Intern, FirstOutIndex, i, SHU_GVL.APS.Ps_Tsc_8_v.PV, new_wrn, new_crs, SHU_GVL.Alarms, AlarmTarget);
//[ШУ ГМК] Температура силового цилиндра 8
VGALG.fnAPS_Processing(SHU_GVL.ANB.As_Tsc_8_v.ANB, 0.1, unlock, SHU_GVL.APS.As_Tsc_8_v.Intern, FirstOutIndex, i, SHU_GVL.APS.As_Tsc_8_v.PV, new_wrn, new_crs, SHU_GVL.Alarms, AlarmTarget);
//[ШУ ГМК] Температура силового цилиндра 9
VGALG.fnAPS_Processing(SHU_GVL.ANB.Ps_Tsc_9_n.ANB, 0.1, unlock, SHU_GVL.APS.Ps_Tsc_9_n.Intern, FirstOutIndex, i, SHU_GVL.APS.Ps_Tsc_9_n.PV, new_wrn, new_crs, SHU_GVL.Alarms, AlarmTarget);
//[ШУ ГМК] Температура силового цилиндра 9
VGALG.fnAPS_Processing(SHU_GVL.ANB.Ps_Tsc_9_v.ANB, 0.1, unlock, SHU_GVL.APS.Ps_Tsc_9_v.Intern, FirstOutIndex, i, SHU_GVL.APS.Ps_Tsc_9_v.PV, new_wrn, new_crs, SHU_GVL.Alarms, AlarmTarget);
//[ШУ ГМК] Температура силового цилиндра 9
VGALG.fnAPS_Processing(SHU_GVL.ANB.As_Tsc_9_v.ANB, 0.1, unlock, SHU_GVL.APS.As_Tsc_9_v.Intern, FirstOutIndex, i, SHU_GVL.APS.As_Tsc_9_v.PV, new_wrn, new_crs, SHU_GVL.Alarms, AlarmTarget);
//[ШУ ГМК] Температура силового цилиндра 10
VGALG.fnAPS_Processing(SHU_GVL.ANB.Ps_Tsc_10_n.ANB, 0.1, unlock, SHU_GVL.APS.Ps_Tsc_10_n.Intern, FirstOutIndex, i, SHU_GVL.APS.Ps_Tsc_10_n.PV, new_wrn, new_crs, SHU_GVL.Alarms, AlarmTarget);
//[ШУ ГМК] Температура силового цилиндра 10
VGALG.fnAPS_Processing(SHU_GVL.ANB.Ps_Tsc_10_v.ANB, 0.1, unlock, SHU_GVL.APS.Ps_Tsc_10_v.Intern, FirstOutIndex, i, SHU_GVL.APS.Ps_Tsc_10_v.PV, new_wrn, new_crs, SHU_GVL.Alarms, AlarmTarget);
//[ШУ ГМК] Температура силового цилиндра 10
VGALG.fnAPS_Processing(SHU_GVL.ANB.As_Tsc_10_v.ANB, 0.1, unlock, SHU_GVL.APS.As_Tsc_10_v.Intern, FirstOutIndex, i, SHU_GVL.APS.As_Tsc_10_v.PV, new_wrn, new_crs, SHU_GVL.Alarms, AlarmTarget);
//[ШУ ГМК] Температура выхлопных газов в левом коллекторе
VGALG.fnAPS_Processing(SHU_GVL.ANB.Ps_Tvg_lk_n.ANB, 0.1, unlock, SHU_GVL.APS.Ps_Tvg_lk_n.Intern, FirstOutIndex, i, SHU_GVL.APS.Ps_Tvg_lk_n.PV, new_wrn, new_crs, SHU_GVL.Alarms, AlarmTarget);
//[ШУ ГМК] Температура выхлопных газов в левом коллекторе
VGALG.fnAPS_Processing(SHU_GVL.ANB.Ps_Tvg_lk_v.ANB, 0.1, unlock, SHU_GVL.APS.Ps_Tvg_lk_v.Intern, FirstOutIndex, i, SHU_GVL.APS.Ps_Tvg_lk_v.PV, new_wrn, new_crs, SHU_GVL.Alarms, AlarmTarget);
//[ШУ ГМК] Температура выхлопных газов в левом коллекторе
VGALG.fnAPS_Processing(SHU_GVL.ANB.As_Tvg_lk_v.ANB, 0.1, unlock, SHU_GVL.APS.As_Tvg_lk_v.Intern, FirstOutIndex, i, SHU_GVL.APS.As_Tvg_lk_v.PV, new_wrn, new_crs, SHU_GVL.Alarms, AlarmTarget);
//[ШУ ГМК] Температура выхлопных газов в правом коллекторе
VGALG.fnAPS_Processing(SHU_GVL.ANB.Ps_Tvg_pk_n.ANB, 0.1, unlock, SHU_GVL.APS.Ps_Tvg_pk_n.Intern, FirstOutIndex, i, SHU_GVL.APS.Ps_Tvg_pk_n.PV, new_wrn, new_crs, SHU_GVL.Alarms, AlarmTarget);
//[ШУ ГМК] Температура выхлопных газов в правом коллекторе
VGALG.fnAPS_Processing(SHU_GVL.ANB.Ps_Tvg_pk_v.ANB, 0.1, unlock, SHU_GVL.APS.Ps_Tvg_pk_v.Intern, FirstOutIndex, i, SHU_GVL.APS.Ps_Tvg_pk_v.PV, new_wrn, new_crs, SHU_GVL.Alarms, AlarmTarget);
//[ШУ ГМК] Температура выхлопных газов в правом коллекторе
VGALG.fnAPS_Processing(SHU_GVL.ANB.As_Tvg_pk_v.ANB, 0.1, unlock, SHU_GVL.APS.As_Tvg_pk_v.Intern, FirstOutIndex, i, SHU_GVL.APS.As_Tvg_pk_v.PV, new_wrn, new_crs, SHU_GVL.Alarms, AlarmTarget);
//[ШУ ГМК] Температура коренного подшипника № 1
VGALG.fnAPS_Processing(SHU_GVL.ANB.Ps_Tkp_1_v.ANB, 0.1, unlock, SHU_GVL.APS.Ps_Tkp_1_v.Intern, FirstOutIndex, i, SHU_GVL.APS.Ps_Tkp_1_v.PV, new_wrn, new_crs, SHU_GVL.Alarms, AlarmTarget);
//[ШУ ГМК] Температура коренного подшипника № 1
VGALG.fnAPS_Processing(SHU_GVL.ANB.As_Tkp_1_v.ANB, 0.1, unlock, SHU_GVL.APS.As_Tkp_1_v.Intern, FirstOutIndex, i, SHU_GVL.APS.As_Tkp_1_v.PV, new_wrn, new_crs, SHU_GVL.Alarms, AlarmTarget);
//[ШУ ГМК] Температура коренного подшипника № 2
VGALG.fnAPS_Processing(SHU_GVL.ANB.Ps_Tkp_2_v.ANB, 0.1, unlock, SHU_GVL.APS.Ps_Tkp_2_v.Intern, FirstOutIndex, i, SHU_GVL.APS.Ps_Tkp_2_v.PV, new_wrn, new_crs, SHU_GVL.Alarms, AlarmTarget);
//[ШУ ГМК] Температура коренного подшипника № 2
VGALG.fnAPS_Processing(SHU_GVL.ANB.As_Tkp_2_v.ANB, 0.1, unlock, SHU_GVL.APS.As_Tkp_2_v.Intern, FirstOutIndex, i, SHU_GVL.APS.As_Tkp_2_v.PV, new_wrn, new_crs, SHU_GVL.Alarms, AlarmTarget);
//[ШУ ГМК] Температура коренного подшипника № 3
VGALG.fnAPS_Processing(SHU_GVL.ANB.Ps_Tkp_3_v.ANB, 0.1, unlock, SHU_GVL.APS.Ps_Tkp_3_v.Intern, FirstOutIndex, i, SHU_GVL.APS.Ps_Tkp_3_v.PV, new_wrn, new_crs, SHU_GVL.Alarms, AlarmTarget);
//[ШУ ГМК] Температура коренного подшипника № 3
VGALG.fnAPS_Processing(SHU_GVL.ANB.As_Tkp_3_v.ANB, 0.1, unlock, SHU_GVL.APS.As_Tkp_3_v.Intern, FirstOutIndex, i, SHU_GVL.APS.As_Tkp_3_v.PV, new_wrn, new_crs, SHU_GVL.Alarms, AlarmTarget);
//[ШУ ГМК] Температура коренного подшипника № 4
VGALG.fnAPS_Processing(SHU_GVL.ANB.Ps_Tkp_4_v.ANB, 0.1, unlock, SHU_GVL.APS.Ps_Tkp_4_v.Intern, FirstOutIndex, i, SHU_GVL.APS.Ps_Tkp_4_v.PV, new_wrn, new_crs, SHU_GVL.Alarms, AlarmTarget);
//[ШУ ГМК] Температура коренного подшипника № 4
VGALG.fnAPS_Processing(SHU_GVL.ANB.As_Tkp_4_v.ANB, 0.1, unlock, SHU_GVL.APS.As_Tkp_4_v.Intern, FirstOutIndex, i, SHU_GVL.APS.As_Tkp_4_v.PV, new_wrn, new_crs, SHU_GVL.Alarms, AlarmTarget);
//[ШУ ГМК] Температура коренного подшипника № 5
VGALG.fnAPS_Processing(SHU_GVL.ANB.Ps_Tkp_5_v.ANB, 0.1, unlock, SHU_GVL.APS.Ps_Tkp_5_v.Intern, FirstOutIndex, i, SHU_GVL.APS.Ps_Tkp_5_v.PV, new_wrn, new_crs, SHU_GVL.Alarms, AlarmTarget);
//[ШУ ГМК] Температура коренного подшипника № 5
VGALG.fnAPS_Processing(SHU_GVL.ANB.As_Tkp_5_v.ANB, 0.1, unlock, SHU_GVL.APS.As_Tkp_5_v.Intern, FirstOutIndex, i, SHU_GVL.APS.As_Tkp_5_v.PV, new_wrn, new_crs, SHU_GVL.Alarms, AlarmTarget);
//[ШУ ГМК] Температура коренного подшипника № 6
VGALG.fnAPS_Processing(SHU_GVL.ANB.Ps_Tkp_6_v.ANB, 0.1, unlock, SHU_GVL.APS.Ps_Tkp_6_v.Intern, FirstOutIndex, i, SHU_GVL.APS.Ps_Tkp_6_v.PV, new_wrn, new_crs, SHU_GVL.Alarms, AlarmTarget);
//[ШУ ГМК] Температура коренного подшипника № 6
VGALG.fnAPS_Processing(SHU_GVL.ANB.As_Tkp_6_v.ANB, 0.1, unlock, SHU_GVL.APS.As_Tkp_6_v.Intern, FirstOutIndex, i, SHU_GVL.APS.As_Tkp_6_v.PV, new_wrn, new_crs, SHU_GVL.Alarms, AlarmTarget);
//[ШУ ГМК] Температура коренного подшипника № 7
VGALG.fnAPS_Processing(SHU_GVL.ANB.Ps_Tkp_7_v.ANB, 0.1, unlock, SHU_GVL.APS.Ps_Tkp_7_v.Intern, FirstOutIndex, i, SHU_GVL.APS.Ps_Tkp_7_v.PV, new_wrn, new_crs, SHU_GVL.Alarms, AlarmTarget);
//[ШУ ГМК] Температура коренного подшипника № 7
VGALG.fnAPS_Processing(SHU_GVL.ANB.As_Tkp_7_v.ANB, 0.1, unlock, SHU_GVL.APS.As_Tkp_7_v.Intern, FirstOutIndex, i, SHU_GVL.APS.As_Tkp_7_v.PV, new_wrn, new_crs, SHU_GVL.Alarms, AlarmTarget);
//[ШУ ГМК] Температура коренного подшипника № 8
VGALG.fnAPS_Processing(SHU_GVL.ANB.Ps_Tkp_8_v.ANB, 0.1, unlock, SHU_GVL.APS.Ps_Tkp_8_v.Intern, FirstOutIndex, i, SHU_GVL.APS.Ps_Tkp_8_v.PV, new_wrn, new_crs, SHU_GVL.Alarms, AlarmTarget);
//[ШУ ГМК] Температура коренного подшипника № 8
VGALG.fnAPS_Processing(SHU_GVL.ANB.As_Tkp_8_v.ANB, 0.1, unlock, SHU_GVL.APS.As_Tkp_8_v.Intern, FirstOutIndex, i, SHU_GVL.APS.As_Tkp_8_v.PV, new_wrn, new_crs, SHU_GVL.Alarms, AlarmTarget);
//[ШУ ГМК] Температура коренного подшипника № 9
VGALG.fnAPS_Processing(SHU_GVL.ANB.Ps_Tkp_9_v.ANB, 0.1, unlock, SHU_GVL.APS.Ps_Tkp_9_v.Intern, FirstOutIndex, i, SHU_GVL.APS.Ps_Tkp_9_v.PV, new_wrn, new_crs, SHU_GVL.Alarms, AlarmTarget);
//[ШУ ГМК] Температура коренного подшипника № 9
VGALG.fnAPS_Processing(SHU_GVL.ANB.As_Tkp_9_v.ANB, 0.1, unlock, SHU_GVL.APS.As_Tkp_9_v.Intern, FirstOutIndex, i, SHU_GVL.APS.As_Tkp_9_v.PV, new_wrn, new_crs, SHU_GVL.Alarms, AlarmTarget);
//[ШУ ГМК] Температура коренного подшипника № 10
VGALG.fnAPS_Processing(SHU_GVL.ANB.Ps_Tkp_10_v.ANB, 0.1, unlock, SHU_GVL.APS.Ps_Tkp_10_v.Intern, FirstOutIndex, i, SHU_GVL.APS.Ps_Tkp_10_v.PV, new_wrn, new_crs, SHU_GVL.Alarms, AlarmTarget);
//[ШУ ГМК] Температура коренного подшипника № 10
VGALG.fnAPS_Processing(SHU_GVL.ANB.As_Tkp_10_v.ANB, 0.1, unlock, SHU_GVL.APS.As_Tkp_10_v.Intern, FirstOutIndex, i, SHU_GVL.APS.As_Tkp_10_v.PV, new_wrn, new_crs, SHU_GVL.Alarms, AlarmTarget);
//[ШУ ГМК] Температура воды на выходе из двигателя
VGALG.fnAPS_Processing(SHU_GVL.ANB.Ps_Tv_outD_v.ANB, 0.1, unlock, SHU_GVL.APS.Ps_Tv_outD_v.Intern, FirstOutIndex, i, SHU_GVL.APS.Ps_Tv_outD_v.PV, new_wrn, new_crs, SHU_GVL.Alarms, AlarmTarget);
//[ШУ ГМК] Температура воды на выходе из двигателя
VGALG.fnAPS_Processing(SHU_GVL.ANB.As_Tv_outD_v.ANB, 0.1, unlock, SHU_GVL.APS.As_Tv_outD_v.Intern, FirstOutIndex, i, SHU_GVL.APS.As_Tv_outD_v.PV, new_wrn, new_crs, SHU_GVL.Alarms, AlarmTarget);
//[ШУ ГМК] Температура масла на входе в ГМК
VGALG.fnAPS_Processing(SHU_GVL.ANB.Ps_Tm_inGMK_n.ANB, 0.1, unlock, SHU_GVL.APS.Ps_Tm_inGMK_n.Intern, FirstOutIndex, i, SHU_GVL.APS.Ps_Tm_inGMK_n.PV, new_wrn, new_crs, SHU_GVL.Alarms, AlarmTarget);
//[ШУ ГМК] Температура масла на выходе из ГМК
VGALG.fnAPS_Processing(SHU_GVL.ANB.Ps_Tm_outGMK_v.ANB, 0.1, unlock, SHU_GVL.APS.Ps_Tm_outGMK_v.Intern, FirstOutIndex, i, SHU_GVL.APS.Ps_Tm_outGMK_v.PV, new_wrn, new_crs, SHU_GVL.Alarms, AlarmTarget);
//[ШУ ГМК] Температура масла на выходе из ГМК
VGALG.fnAPS_Processing(SHU_GVL.ANB.As_Tm_outGMK_v.ANB, 0.1, unlock, SHU_GVL.APS.As_Tm_outGMK_v.Intern, FirstOutIndex, i, SHU_GVL.APS.As_Tm_outGMK_v.PV, new_wrn, new_crs, SHU_GVL.Alarms, AlarmTarget);
//[ШУ ГМК] Температура газа на выходе компрессорного цилиндра 1
VGALG.fnAPS_Processing(SHU_GVL.ANB.Ps_Tg_outKC_1_v.ANB, 0.1, unlock, SHU_GVL.APS.Ps_Tg_outKC_1_v.Intern, FirstOutIndex, i, SHU_GVL.APS.Ps_Tg_outKC_1_v.PV, new_wrn, new_crs, SHU_GVL.Alarms, AlarmTarget);
//[ШУ ГМК] Температура газа на выходе компрессорного цилиндра 1
VGALG.fnAPS_Processing(SHU_GVL.ANB.As_Tg_outKC_1_v.ANB, 0.1, unlock, SHU_GVL.APS.As_Tg_outKC_1_v.Intern, FirstOutIndex, i, SHU_GVL.APS.As_Tg_outKC_1_v.PV, new_wrn, new_crs, SHU_GVL.Alarms, AlarmTarget);
//[ШУ ГМК] Температура газа на выходе компрессорного цилиндра 2
VGALG.fnAPS_Processing(SHU_GVL.ANB.Ps_Tg_outKC_2_v.ANB, 0.1, unlock, SHU_GVL.APS.Ps_Tg_outKC_2_v.Intern, FirstOutIndex, i, SHU_GVL.APS.Ps_Tg_outKC_2_v.PV, new_wrn, new_crs, SHU_GVL.Alarms, AlarmTarget);
//[ШУ ГМК] Температура газа на выходе компрессорного цилиндра 2
VGALG.fnAPS_Processing(SHU_GVL.ANB.As_Tg_outKC_2_v.ANB, 0.1, unlock, SHU_GVL.APS.As_Tg_outKC_2_v.Intern, FirstOutIndex, i, SHU_GVL.APS.As_Tg_outKC_2_v.PV, new_wrn, new_crs, SHU_GVL.Alarms, AlarmTarget);
//[ШУ ГМК] Температура газа на выходе компрессорного цилиндра 3
VGALG.fnAPS_Processing(SHU_GVL.ANB.Ps_Tg_outKC_3_v.ANB, 0.1, unlock, SHU_GVL.APS.Ps_Tg_outKC_3_v.Intern, FirstOutIndex, i, SHU_GVL.APS.Ps_Tg_outKC_3_v.PV, new_wrn, new_crs, SHU_GVL.Alarms, AlarmTarget);
//[ШУ ГМК] Температура газа на выходе компрессорного цилиндра 3
VGALG.fnAPS_Processing(SHU_GVL.ANB.As_Tg_outKC_3_v.ANB, 0.1, unlock, SHU_GVL.APS.As_Tg_outKC_3_v.Intern, FirstOutIndex, i, SHU_GVL.APS.As_Tg_outKC_3_v.PV, new_wrn, new_crs, SHU_GVL.Alarms, AlarmTarget);
//[ШУ ГМК] Температура газа на выходе компрессорного цилиндра 4
VGALG.fnAPS_Processing(SHU_GVL.ANB.Ps_Tg_outKC_4_v.ANB, 0.1, unlock, SHU_GVL.APS.Ps_Tg_outKC_4_v.Intern, FirstOutIndex, i, SHU_GVL.APS.Ps_Tg_outKC_4_v.PV, new_wrn, new_crs, SHU_GVL.Alarms, AlarmTarget);
//[ШУ ГМК] Температура газа на выходе компрессорного цилиндра 4
VGALG.fnAPS_Processing(SHU_GVL.ANB.As_Tg_outKC_4_v.ANB, 0.1, unlock, SHU_GVL.APS.As_Tg_outKC_4_v.Intern, FirstOutIndex, i, SHU_GVL.APS.As_Tg_outKC_4_v.PV, new_wrn, new_crs, SHU_GVL.Alarms, AlarmTarget);
//[ШУ ГМК] Температура газа на выходе компрессорного цилиндра 5
VGALG.fnAPS_Processing(SHU_GVL.ANB.Ps_Tg_outKC_5_v.ANB, 0.1, unlock, SHU_GVL.APS.Ps_Tg_outKC_5_v.Intern, FirstOutIndex, i, SHU_GVL.APS.Ps_Tg_outKC_5_v.PV, new_wrn, new_crs, SHU_GVL.Alarms, AlarmTarget);
//[ШУ ГМК] Температура газа на выходе компрессорного цилиндра 5
VGALG.fnAPS_Processing(SHU_GVL.ANB.As_Tg_outKC_5_v.ANB, 0.1, unlock, SHU_GVL.APS.As_Tg_outKC_5_v.Intern, FirstOutIndex, i, SHU_GVL.APS.As_Tg_outKC_5_v.PV, new_wrn, new_crs, SHU_GVL.Alarms, AlarmTarget);
//[ШУ ГМК] Давление газа на входе в ГМК
VGALG.fnAPS_Processing(SHU_GVL.ANB.Ps_Pg_inGMK_n.ANB, 0.1, unlock, SHU_GVL.APS.Ps_Pg_inGMK_n.Intern, FirstOutIndex, i, SHU_GVL.APS.Ps_Pg_inGMK_n.PV, new_wrn, new_crs, SHU_GVL.Alarms, AlarmTarget);
//[ШУ ГМК] Давление газа на входе в ГМК
VGALG.fnAPS_Processing(SHU_GVL.ANB.Ps_Pg_inGMK_v.ANB, 0.1, unlock, SHU_GVL.APS.Ps_Pg_inGMK_v.Intern, FirstOutIndex, i, SHU_GVL.APS.Ps_Pg_inGMK_v.PV, new_wrn, new_crs, SHU_GVL.Alarms, AlarmTarget);
//[ШУ ГМК] Давление газа на выходе из ГМК
VGALG.fnAPS_Processing(SHU_GVL.ANB.Ps_Pg_outGMK_SHU_GMK_v.ANB, 0.1, unlock, SHU_GVL.APS.Ps_Pg_outGMK_SHU_GMK_v.Intern, FirstOutIndex, i, SHU_GVL.APS.Ps_Pg_outGMK_SHU_GMK_v.PV, new_wrn, new_crs, SHU_GVL.Alarms, AlarmTarget);
//[ШУ ГМК] Давление газа на выходе из ГМК
VGALG.fnAPS_Processing(SHU_GVL.ANB.As_Pg_outGMK_SHU_GMK_v.ANB, 0.1, unlock, SHU_GVL.APS.As_Pg_outGMK_SHU_GMK_v.Intern, FirstOutIndex, i, SHU_GVL.APS.As_Pg_outGMK_SHU_GMK_v.PV, new_wrn, new_crs, SHU_GVL.Alarms, AlarmTarget);
//[ШУ ГМК] Давление пускового воздуха
VGALG.fnAPS_Processing(SHU_GVL.ANB.Ps_Ppv_n.ANB, 0.1, unlock, SHU_GVL.APS.Ps_Ppv_n.Intern, FirstOutIndex, i, SHU_GVL.APS.Ps_Ppv_n.PV, new_wrn, new_crs, SHU_GVL.Alarms, AlarmTarget);
//[ШУ ГМК] Давление топливного газа до ТРК
VGALG.fnAPS_Processing(SHU_GVL.ANB.Ps_Ptg_inTRK_n.ANB, 0.1, unlock, SHU_GVL.APS.Ps_Ptg_inTRK_n.Intern, FirstOutIndex, i, SHU_GVL.APS.Ps_Ptg_inTRK_n.PV, new_wrn, new_crs, SHU_GVL.Alarms, AlarmTarget);
//[ШУ ГМК] Давление топливного газа до ТРК
VGALG.fnAPS_Processing(SHU_GVL.ANB.Ps_Ptg_inTRK_v.ANB, 0.1, unlock, SHU_GVL.APS.Ps_Ptg_inTRK_v.Intern, FirstOutIndex, i, SHU_GVL.APS.Ps_Ptg_inTRK_v.PV, new_wrn, new_crs, SHU_GVL.Alarms, AlarmTarget);
//[ШУ ГМК] Давление топливного газа до ТРК
VGALG.fnAPS_Processing(SHU_GVL.ANB.As_Ptg_inTRK_n.ANB, 0.1, unlock, SHU_GVL.APS.As_Ptg_inTRK_n.Intern, FirstOutIndex, i, SHU_GVL.APS.As_Ptg_inTRK_n.PV, new_wrn, new_crs, SHU_GVL.Alarms, AlarmTarget);
//[ШУ ГМК] Давление топливного газа до ТРК
VGALG.fnAPS_Processing(SHU_GVL.ANB.As_Ptg_inTRK_v.ANB, 0.1, unlock, SHU_GVL.APS.As_Ptg_inTRK_v.Intern, FirstOutIndex, i, SHU_GVL.APS.As_Ptg_inTRK_v.PV, new_wrn, new_crs, SHU_GVL.Alarms, AlarmTarget);
//[ШУ ГМК] Давление масла на входе в турбокомпрессоры
VGALG.fnAPS_Processing(SHU_GVL.ANB.Ps_Pm_inTK_n.ANB, 0.1, unlock, SHU_GVL.APS.Ps_Pm_inTK_n.Intern, FirstOutIndex, i, SHU_GVL.APS.Ps_Pm_inTK_n.PV, new_wrn, new_crs, SHU_GVL.Alarms, AlarmTarget);
//[ШУ ГМК] Давление масла на входе в турбокомпрессоры
VGALG.fnAPS_Processing(SHU_GVL.ANB.As_Pm_inTK_n.ANB, 0.1, unlock, SHU_GVL.APS.As_Pm_inTK_n.Intern, FirstOutIndex, i, SHU_GVL.APS.As_Pm_inTK_n.PV, new_wrn, new_crs, SHU_GVL.Alarms, AlarmTarget);
//[ШУ ГМК] Давление масла на входе в двигатель
VGALG.fnAPS_Processing(SHU_GVL.ANB.Ps_Pm_inD_SHU_GMK_n.ANB, 0.1, unlock, SHU_GVL.APS.Ps_Pm_inD_SHU_GMK_n.Intern, FirstOutIndex, i, SHU_GVL.APS.Ps_Pm_inD_SHU_GMK_n.PV, new_wrn, new_crs, SHU_GVL.Alarms, AlarmTarget);
//[ШУ ГМК] Давление масла на входе в двигатель
VGALG.fnAPS_Processing(SHU_GVL.ANB.As_Pm_inD_SHU_GMK_n.ANB, 0.1, unlock, SHU_GVL.APS.As_Pm_inD_SHU_GMK_n.Intern, FirstOutIndex, i, SHU_GVL.APS.As_Pm_inD_SHU_GMK_n.PV, new_wrn, new_crs, SHU_GVL.Alarms, AlarmTarget);
//[ШУ ГМК] Перепад давления масла на фильтре
VGALG.fnAPS_Processing(SHU_GVL.ANB.Ps_dPmf_v.ANB, 0.1, unlock, SHU_GVL.APS.Ps_dPmf_v.Intern, FirstOutIndex, i, SHU_GVL.APS.Ps_dPmf_v.PV, new_wrn, new_crs, SHU_GVL.Alarms, AlarmTarget);
//[ШУ ГМК] Давление воды на выходе из двигателя
VGALG.fnAPS_Processing(SHU_GVL.ANB.As_Pv_outD_n.ANB, 0.1, unlock, SHU_GVL.APS.As_Pv_outD_n.Intern, FirstOutIndex, i, SHU_GVL.APS.As_Pv_outD_n.PV, new_wrn, new_crs, SHU_GVL.Alarms, AlarmTarget);
//[ШУ ГМК] Уровень вибрации ГМК (виброскорость), канал 1
VGALG.fnAPS_Processing(SHU_GVL.ANB.Ps_Vb_Ch_1_v.ANB, 0.1, unlock, SHU_GVL.APS.Ps_Vb_Ch_1_v.Intern, FirstOutIndex, i, SHU_GVL.APS.Ps_Vb_Ch_1_v.PV, new_wrn, new_crs, SHU_GVL.Alarms, AlarmTarget);
//[ШУ ГМК] Уровень вибрации ГМК (виброскорость), канал 1
VGALG.fnAPS_Processing(SHU_GVL.ANB.As_Vb_Ch_1_v.ANB, 0.1, unlock, SHU_GVL.APS.As_Vb_Ch_1_v.Intern, FirstOutIndex, i, SHU_GVL.APS.As_Vb_Ch_1_v.PV, new_wrn, new_crs, SHU_GVL.Alarms, AlarmTarget);
//[ШУ ГМК] Уровень вибрации ГМК (виброскорость), канал 2
VGALG.fnAPS_Processing(SHU_GVL.ANB.Ps_Vb_Ch_2_v.ANB, 0.1, unlock, SHU_GVL.APS.Ps_Vb_Ch_2_v.Intern, FirstOutIndex, i, SHU_GVL.APS.Ps_Vb_Ch_2_v.PV, new_wrn, new_crs, SHU_GVL.Alarms, AlarmTarget);
//[ШУ ГМК] Уровень вибрации ГМК (виброскорость), канал 2
VGALG.fnAPS_Processing(SHU_GVL.ANB.As_Vb_Ch_2_v.ANB, 0.1, unlock, SHU_GVL.APS.As_Vb_Ch_2_v.Intern, FirstOutIndex, i, SHU_GVL.APS.As_Vb_Ch_2_v.PV, new_wrn, new_crs, SHU_GVL.Alarms, AlarmTarget);
//[ШУ ГМК] Авария насоса прокачки масла
VGALG.fnAPS_Processing(SHU_GVL.ANB.Ps_A_Pmp_ppm.ANB, 0.1, unlock, SHU_GVL.APS.Ps_A_Pmp_ppm.Intern, FirstOutIndex, i, SHU_GVL.APS.Ps_A_Pmp_ppm.PV, new_wrn, new_crs, SHU_GVL.Alarms, AlarmTarget);
//[БКД] Детонация в цилиндре № 1
VGALG.fnAPS_Processing(SHU_GVL.ANB.Ps_Det_SC_1_v.ANB, 0.1, unlock, SHU_GVL.APS.Ps_Det_SC_1_v.Intern, FirstOutIndex, i, SHU_GVL.APS.Ps_Det_SC_1_v.PV, new_wrn, new_crs, SHU_GVL.Alarms, AlarmTarget);
//[БКД] Детонация в цилиндре № 1
VGALG.fnAPS_Processing(SHU_GVL.ANB.As_Det_SC_1_v.ANB, 0.1, unlock, SHU_GVL.APS.As_Det_SC_1_v.Intern, FirstOutIndex, i, SHU_GVL.APS.As_Det_SC_1_v.PV, new_wrn, new_crs, SHU_GVL.Alarms, AlarmTarget);
//[БКД] Детонация в цилиндре № 2
VGALG.fnAPS_Processing(SHU_GVL.ANB.Ps_Det_SC_2_v.ANB, 0.1, unlock, SHU_GVL.APS.Ps_Det_SC_2_v.Intern, FirstOutIndex, i, SHU_GVL.APS.Ps_Det_SC_2_v.PV, new_wrn, new_crs, SHU_GVL.Alarms, AlarmTarget);
//[БКД] Детонация в цилиндре № 2
VGALG.fnAPS_Processing(SHU_GVL.ANB.As_Det_SC_2_v.ANB, 0.1, unlock, SHU_GVL.APS.As_Det_SC_2_v.Intern, FirstOutIndex, i, SHU_GVL.APS.As_Det_SC_2_v.PV, new_wrn, new_crs, SHU_GVL.Alarms, AlarmTarget);
//[БКД] Детонация в цилиндре № 3
VGALG.fnAPS_Processing(SHU_GVL.ANB.Ps_Det_SC_3_v.ANB, 0.1, unlock, SHU_GVL.APS.Ps_Det_SC_3_v.Intern, FirstOutIndex, i, SHU_GVL.APS.Ps_Det_SC_3_v.PV, new_wrn, new_crs, SHU_GVL.Alarms, AlarmTarget);
//[БКД] Детонация в цилиндре № 3
VGALG.fnAPS_Processing(SHU_GVL.ANB.As_Det_SC_3_v.ANB, 0.1, unlock, SHU_GVL.APS.As_Det_SC_3_v.Intern, FirstOutIndex, i, SHU_GVL.APS.As_Det_SC_3_v.PV, new_wrn, new_crs, SHU_GVL.Alarms, AlarmTarget);
//[БКД] Детонация в цилиндре № 4
VGALG.fnAPS_Processing(SHU_GVL.ANB.Ps_Det_SC_4_v.ANB, 0.1, unlock, SHU_GVL.APS.Ps_Det_SC_4_v.Intern, FirstOutIndex, i, SHU_GVL.APS.Ps_Det_SC_4_v.PV, new_wrn, new_crs, SHU_GVL.Alarms, AlarmTarget);
//[БКД] Детонация в цилиндре № 4
VGALG.fnAPS_Processing(SHU_GVL.ANB.As_Det_SC_4_v.ANB, 0.1, unlock, SHU_GVL.APS.As_Det_SC_4_v.Intern, FirstOutIndex, i, SHU_GVL.APS.As_Det_SC_4_v.PV, new_wrn, new_crs, SHU_GVL.Alarms, AlarmTarget);
//[БКД] Детонация в цилиндре № 5
VGALG.fnAPS_Processing(SHU_GVL.ANB.Ps_Det_SC_5_v.ANB, 0.1, unlock, SHU_GVL.APS.Ps_Det_SC_5_v.Intern, FirstOutIndex, i, SHU_GVL.APS.Ps_Det_SC_5_v.PV, new_wrn, new_crs, SHU_GVL.Alarms, AlarmTarget);
//[БКД] Детонация в цилиндре № 5
VGALG.fnAPS_Processing(SHU_GVL.ANB.As_Det_SC_5_v.ANB, 0.1, unlock, SHU_GVL.APS.As_Det_SC_5_v.Intern, FirstOutIndex, i, SHU_GVL.APS.As_Det_SC_5_v.PV, new_wrn, new_crs, SHU_GVL.Alarms, AlarmTarget);
//[БКД] Детонация в цилиндре № 6
VGALG.fnAPS_Processing(SHU_GVL.ANB.Ps_Det_SC_6_v.ANB, 0.1, unlock, SHU_GVL.APS.Ps_Det_SC_6_v.Intern, FirstOutIndex, i, SHU_GVL.APS.Ps_Det_SC_6_v.PV, new_wrn, new_crs, SHU_GVL.Alarms, AlarmTarget);
//[БКД] Детонация в цилиндре № 6
VGALG.fnAPS_Processing(SHU_GVL.ANB.As_Det_SC_6_v.ANB, 0.1, unlock, SHU_GVL.APS.As_Det_SC_6_v.Intern, FirstOutIndex, i, SHU_GVL.APS.As_Det_SC_6_v.PV, new_wrn, new_crs, SHU_GVL.Alarms, AlarmTarget);
//[БКД] Детонация в цилиндре № 7
VGALG.fnAPS_Processing(SHU_GVL.ANB.Ps_Det_SC_7_v.ANB, 0.1, unlock, SHU_GVL.APS.Ps_Det_SC_7_v.Intern, FirstOutIndex, i, SHU_GVL.APS.Ps_Det_SC_7_v.PV, new_wrn, new_crs, SHU_GVL.Alarms, AlarmTarget);
//[БКД] Детонация в цилиндре № 7
VGALG.fnAPS_Processing(SHU_GVL.ANB.As_Det_SC_7_v.ANB, 0.1, unlock, SHU_GVL.APS.As_Det_SC_7_v.Intern, FirstOutIndex, i, SHU_GVL.APS.As_Det_SC_7_v.PV, new_wrn, new_crs, SHU_GVL.Alarms, AlarmTarget);
//[БКД] Детонация в цилиндре № 8
VGALG.fnAPS_Processing(SHU_GVL.ANB.Ps_Det_SC_8_v.ANB, 0.1, unlock, SHU_GVL.APS.Ps_Det_SC_8_v.Intern, FirstOutIndex, i, SHU_GVL.APS.Ps_Det_SC_8_v.PV, new_wrn, new_crs, SHU_GVL.Alarms, AlarmTarget);
//[БКД] Детонация в цилиндре № 8
VGALG.fnAPS_Processing(SHU_GVL.ANB.As_Det_SC_8_v.ANB, 0.1, unlock, SHU_GVL.APS.As_Det_SC_8_v.Intern, FirstOutIndex, i, SHU_GVL.APS.As_Det_SC_8_v.PV, new_wrn, new_crs, SHU_GVL.Alarms, AlarmTarget);
//[БКД] Детонация в цилиндре № 9
VGALG.fnAPS_Processing(SHU_GVL.ANB.Ps_Det_SC_9_v.ANB, 0.1, unlock, SHU_GVL.APS.Ps_Det_SC_9_v.Intern, FirstOutIndex, i, SHU_GVL.APS.Ps_Det_SC_9_v.PV, new_wrn, new_crs, SHU_GVL.Alarms, AlarmTarget);
//[БКД] Детонация в цилиндре № 9
VGALG.fnAPS_Processing(SHU_GVL.ANB.As_Det_SC_9_v.ANB, 0.1, unlock, SHU_GVL.APS.As_Det_SC_9_v.Intern, FirstOutIndex, i, SHU_GVL.APS.As_Det_SC_9_v.PV, new_wrn, new_crs, SHU_GVL.Alarms, AlarmTarget);
//[БКД] Детонация в цилиндре № 10
VGALG.fnAPS_Processing(SHU_GVL.ANB.Ps_Det_SC_10_v.ANB, 0.1, unlock, SHU_GVL.APS.Ps_Det_SC_10_v.Intern, FirstOutIndex, i, SHU_GVL.APS.Ps_Det_SC_10_v.PV, new_wrn, new_crs, SHU_GVL.Alarms, AlarmTarget);
//[БКД] Детонация в цилиндре № 10
VGALG.fnAPS_Processing(SHU_GVL.ANB.As_Det_SC_10_v.ANB, 0.1, unlock, SHU_GVL.APS.As_Det_SC_10_v.Intern, FirstOutIndex, i, SHU_GVL.APS.As_Det_SC_10_v.PV, new_wrn, new_crs, SHU_GVL.Alarms, AlarmTarget);
//[БУЗ] Частота 1 вращения коленчатого вала
VGALG.fnAPS_Processing(SHU_GVL.ANB.Ps_F_1_vkv_v.ANB, 0.1, unlock, SHU_GVL.APS.Ps_F_1_vkv_v.Intern, FirstOutIndex, i, SHU_GVL.APS.Ps_F_1_vkv_v.PV, new_wrn, new_crs, SHU_GVL.Alarms, AlarmTarget);
//[БУЗ] Частота 1 вращения коленчатого вала
VGALG.fnAPS_Processing(SHU_GVL.ANB.As_F_1_vkv_v.ANB, 0.1, unlock, SHU_GVL.APS.As_F_1_vkv_v.Intern, FirstOutIndex, i, SHU_GVL.APS.As_F_1_vkv_v.PV, new_wrn, new_crs, SHU_GVL.Alarms, AlarmTarget);
"""
proj = projects.primary
folder = proj.find('APS SHU', recursive=True)[0]
struktur = folder.create_pou('SHU_APS_Processing', type = PouType.Function,language=None, return_type='BOOL', base_type=None, interfaces=None)
struktur.textual_declaration.insert(2, 0, CONTENT_var)
struktur.textual_implementation.insert(0, 0, CONTENT_body)
