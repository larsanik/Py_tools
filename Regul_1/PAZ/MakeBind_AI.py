#encoding:utf-8
from __future__ import print_function
CONTENT_var = """\
"""
CONTENT_body = """\
//================ Привязка входов к HW ================
PAZ_GVL.AI.Pg_outGMK_44.DRV := PAZ_GVL.A1_3.in_ch1; //Давление газа на выходе из ГМК №44
PAZ_GVL.AI.Pg_outGMK_45.DRV := PAZ_GVL.A1_3.in_ch2; //Давление газа на выходе из ГМК №45
PAZ_GVL.AI.Pg_outGMK_46.DRV := PAZ_GVL.A1_3.in_ch3; //Давление газа на выходе из ГМК №46
PAZ_GVL.AI.Pg_outGMK_47.DRV := PAZ_GVL.A1_3.in_ch4; //Давление газа на выходе из ГМК №47
PAZ_GVL.AI.Pg_outGMK_48.DRV := PAZ_GVL.A1_3.in_ch5; //Давление газа на выходе из ГМК №48
PAZ_GVL.AI.Pg_outGMK_51.DRV := PAZ_GVL.A1_3.in_ch6; //Давление газа на выходе из ГМК №51
PAZ_GVL.AI.Pg_outGMK_52.DRV := PAZ_GVL.A1_3.in_ch7; //Давление газа на выходе из ГМК №52
PAZ_GVL.AI.Pm_inD_GMK_44.DRV := PAZ_GVL.A1_3.in_ch8; //Давление масла на входе в двигатель ГМК №44
PAZ_GVL.AI.Pm_inD_GMK_45.DRV := PAZ_GVL.A1_3.in_ch1; //Давление масла на входе в двигатель ГМК №45
PAZ_GVL.AI.Pm_inD_GMK_46.DRV := PAZ_GVL.A1_3.in_ch2; //Давление масла на входе в двигатель ГМК №46
PAZ_GVL.AI.Pm_inD_GMK_47.DRV := PAZ_GVL.A1_3.in_ch3; //Давление масла на входе в двигатель ГМК №47
PAZ_GVL.AI.Pm_inD_GMK_48.DRV := PAZ_GVL.A1_3.in_ch4; //Давление масла на входе в двигатель ГМК №48
PAZ_GVL.AI.Pm_inD_GMK_51.DRV := PAZ_GVL.A1_3.in_ch5; //Давление масла на входе в двигатель ГМК №51
PAZ_GVL.AI.Pm_inD_GMK_52.DRV := PAZ_GVL.A1_3.in_ch6; //Давление масла на входе в двигатель ГМК №52
PAZ_GVL.AI.Reserv_0.DRV := PAZ_GVL.A1_3.in_ch7; //Резерв
PAZ_GVL.AI.Reserv_1.DRV := PAZ_GVL.A1_3.in_ch8; //Резерв
PAZ_GVL.AI.U_Osn_AC.DRV := PAZ_GVL.A1_5.in_ch1; //Напряжение основного питания ~220 В
PAZ_GVL.AI.U_Res_AC.DRV := PAZ_GVL.A1_5.in_ch2; //Напряжение резервного питания ~220 В
"""
proj = projects.primary
folder = proj.find('AI PAZ', recursive=True)[0]
struktur = folder.create_pou('PAZ_AI_binding_Hw_to_Lg', type = PouType.Function,language=None, return_type='BOOL', base_type=None, interfaces=None)
struktur.textual_declaration.insert(4, 0, CONTENT_var)
struktur.textual_implementation.insert(0, 0, CONTENT_body)
