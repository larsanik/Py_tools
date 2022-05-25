#encoding:utf-8
from __future__ import print_function
CONTENT_var = """\
"""
CONTENT_body = """\
//================ Обработчик дискретных выходов================
// [A1.5:1] Световой индикатор "ПС"
VGSig.fnDO_Processing(algOut := SHMSH_GVL.DGO.SvetInd_PS.PV, fromHMI := SHMSH_GVL.DGO.SvetInd_PS.FromHMI, toHMI := SHMSH_GVL.DGO.SvetInd_PS.ToHMI, drv => SHMSH_GVL.DGO.SvetInd_PS.DRV);
// [A1.5:2] Световой индикатор "АС"
VGSig.fnDO_Processing(algOut := SHMSH_GVL.DGO.SvetInd_AS.PV, fromHMI := SHMSH_GVL.DGO.SvetInd_AS.FromHMI, toHMI := SHMSH_GVL.DGO.SvetInd_AS.ToHMI, drv => SHMSH_GVL.DGO.SvetInd_AS.DRV);
// [A1.5:3] Световой индикатор "Принудительный останов"
VGSig.fnDO_Processing(algOut := SHMSH_GVL.DGO.SvetInd_AO.PV, fromHMI := SHMSH_GVL.DGO.SvetInd_AO.FromHMI, toHMI := SHMSH_GVL.DGO.SvetInd_AO.ToHMI, drv => SHMSH_GVL.DGO.SvetInd_AO.DRV);
// [A1.5:4] Световой индикатор "Нормальный останов"
VGSig.fnDO_Processing(algOut := SHMSH_GVL.DGO.SvetInd_NO.PV, fromHMI := SHMSH_GVL.DGO.SvetInd_NO.FromHMI, toHMI := SHMSH_GVL.DGO.SvetInd_NO.ToHMI, drv => SHMSH_GVL.DGO.SvetInd_NO.DRV);
// [A1.5:5] Световой индикатор "Пуск ГПА"
VGSig.fnDO_Processing(algOut := SHMSH_GVL.DGO.SvetInd_Pusk_GPA.PV, fromHMI := SHMSH_GVL.DGO.SvetInd_Pusk_GPA.FromHMI, toHMI := SHMSH_GVL.DGO.SvetInd_Pusk_GPA.ToHMI, drv => SHMSH_GVL.DGO.SvetInd_Pusk_GPA.DRV);
// [A1.5:6] Световой индикатор "Деблокировка"
VGSig.fnDO_Processing(algOut := SHMSH_GVL.DGO.SvetInd_Deblock.PV, fromHMI := SHMSH_GVL.DGO.SvetInd_Deblock.FromHMI, toHMI := SHMSH_GVL.DGO.SvetInd_Deblock.ToHMI, drv => SHMSH_GVL.DGO.SvetInd_Deblock.DRV);
"""
proj = projects.primary
folder = proj.find('DO SHMSH', recursive=True)[0]
struktur = folder.create_pou('SHMSH_DO_Call', type = PouType.Function,language=None, return_type='BOOL', base_type=None, interfaces=None)
struktur.textual_declaration.insert(4, 0, CONTENT_var)
struktur.textual_implementation.insert(0, 0, CONTENT_body)
