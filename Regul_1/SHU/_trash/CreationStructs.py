#encoding:utf-8

from __future__ import print_function
import  StructContent
proj = projects.primary

folder = proj.find('Parameter lists SHU', recursive = True)[0]

# Create a struct DUT and insert the list of variables just into the right
# place in line two, row 0 (line numbering starts with line 0)
struktur = folder.create_dut('SHU_list_AI_test') # DutType.Structure is the default
struktur.textual_declaration.insert(2, 0, StructContent.STRUCT_CONTENT_AI)
#struktur = folder.create_dut('SHU_list_AO') # DutType.Structure is the default
#struktur.textual_declaration.insert(2, 0, StructContent.STRUCT_CONTENT_AO)
#struktur = folder.create_dut('SHU_list_DI') # DutType.Structure is the default
#struktur.textual_declaration.insert(2, 0, StructContent.STRUCT_CONTENT_DI)
#struktur = folder.create_dut('SHU_list_DO') # DutType.Structure is the default
#struktur.textual_declaration.insert(2, 0, StructContent.STRUCT_CONTENT_DO)
