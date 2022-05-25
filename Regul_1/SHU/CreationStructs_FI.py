#encoding:utf-8
from __future__ import print_function
STRUCT_CONTENT_FI = """\
"""
proj = projects.primary
folder = proj.find('Parameter lists SHU', recursive=True)[0]
struktur = folder.create_dut('SHU_list_FI')  # DutType.Structure is the default
struktur.textual_declaration.insert(2, 0, STRUCT_CONTENT_FI)
