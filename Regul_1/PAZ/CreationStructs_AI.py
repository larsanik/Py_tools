#encoding:utf-8
from __future__ import print_function
STRUCT_CONTENT_AI = """\
	Pg_outGMK_44:str_AI; //[A1.3:1] Давление газа на выходе из ГМК №44
	Pg_outGMK_45:str_AI; //[A1.3:2] Давление газа на выходе из ГМК №45
	Pg_outGMK_46:str_AI; //[A1.3:3] Давление газа на выходе из ГМК №46
	Pg_outGMK_47:str_AI; //[A1.3:4] Давление газа на выходе из ГМК №47
	Pg_outGMK_48:str_AI; //[A1.3:5] Давление газа на выходе из ГМК №48
	Pg_outGMK_51:str_AI; //[A1.3:6] Давление газа на выходе из ГМК №51
	Pg_outGMK_52:str_AI; //[A1.3:7] Давление газа на выходе из ГМК №52
	Pm_inD_GMK_44:str_AI; //[A1.3:8] Давление масла на входе в двигатель ГМК №44
	Pm_inD_GMK_45:str_AI; //[A1.3:1] Давление масла на входе в двигатель ГМК №45
	Pm_inD_GMK_46:str_AI; //[A1.3:2] Давление масла на входе в двигатель ГМК №46
	Pm_inD_GMK_47:str_AI; //[A1.3:3] Давление масла на входе в двигатель ГМК №47
	Pm_inD_GMK_48:str_AI; //[A1.3:4] Давление масла на входе в двигатель ГМК №48
	Pm_inD_GMK_51:str_AI; //[A1.3:5] Давление масла на входе в двигатель ГМК №51
	Pm_inD_GMK_52:str_AI; //[A1.3:6] Давление масла на входе в двигатель ГМК №52
	Reserv_0:str_AI; //[A1.3:7] Резерв
	Reserv_1:str_AI; //[A1.3:8] Резерв
	U_Osn_AC:str_AI; //[A1.5:1] Напряжение основного питания ~220 В
	U_Res_AC:str_AI; //[A1.5:2] Напряжение резервного питания ~220 В
"""
proj = projects.primary
folder = proj.find('Parameter lists PAZ', recursive=True)[0]
struktur = folder.create_dut('PAZ_list_AI')  # DutType.Structure is the default
struktur.textual_declaration.insert(2, 0, STRUCT_CONTENT_AI)
