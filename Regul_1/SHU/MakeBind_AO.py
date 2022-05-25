#encoding:utf-8
from __future__ import print_function
CONTENT_var = """\
"""
CONTENT_body = """\
//================ Привязка вЫходов к HW ================
SHU_GVL.A1_12.out_ch1 := SHU_GVL.AO.Set_RegKr1.DRV; //Управление запорно-регулирующим клапаном на приёме ГМК PV4601.1
"""
proj = projects.primary
folder = proj.find('AO SHU', recursive=True)[0]
struktur = folder.create_pou('SHU_AO_binding_Lg_to_Hw', type = PouType.Function,language=None, return_type='BOOL', base_type=None, interfaces=None)
struktur.textual_declaration.insert(4, 0, CONTENT_var)
struktur.textual_implementation.insert(0, 0, CONTENT_body)
