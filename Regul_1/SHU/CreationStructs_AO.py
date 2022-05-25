#encoding:utf-8
from __future__ import print_function
STRUCT_CONTENT_AO = """\
	Set_RegKr1:str_AO; //[A1.12:1] Управление запорно-регулирующим клапаном на приёме ГМК PV4601.1
"""
proj = projects.primary
folder = proj.find('Parameter lists SHU', recursive=True)[0]
struktur = folder.create_dut('SHU_list_AO')  # DutType.Structure is the default
struktur.textual_declaration.insert(2, 0, STRUCT_CONTENT_AO)
