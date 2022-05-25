#encoding:utf-8
from __future__ import print_function
CONTENT_var = """\
"""
CONTENT_body = """\
//================ Обработчик дискретных выходов================
// [A1.11:1] Резерв
VGSig.fnDO_Processing(algOut := SHU_GVL.DGO.Reserv_0.PV, fromHMI := SHU_GVL.DGO.Reserv_0.FromHMI, toHMI := SHU_GVL.DGO.Reserv_0.ToHMI, drv => SHU_GVL.DGO.Reserv_0.DRV);
// [A1.11:2] Резерв
VGSig.fnDO_Processing(algOut := SHU_GVL.DGO.Reserv_1.PV, fromHMI := SHU_GVL.DGO.Reserv_1.FromHMI, toHMI := SHU_GVL.DGO.Reserv_1.ToHMI, drv => SHU_GVL.DGO.Reserv_1.DRV);
// [A1.11:3] Клапан XV9605.1 на перемычке открыть/закрыть
VGSig.fnDO_Processing(algOut := SHU_GVL.DGO.Kr5_ON.PV, fromHMI := SHU_GVL.DGO.Kr5_ON.FromHMI, toHMI := SHU_GVL.DGO.Kr5_ON.ToHMI, drv => SHU_GVL.DGO.Kr5_ON.DRV);
// [A1.11:4] Клапан XV9613.1 на сбросе приёмной линии открыть/закрыть
VGSig.fnDO_Processing(algOut := SHU_GVL.DGO.Kr13_ON.PV, fromHMI := SHU_GVL.DGO.Kr13_ON.FromHMI, toHMI := SHU_GVL.DGO.Kr13_ON.ToHMI, drv => SHU_GVL.DGO.Kr13_ON.DRV);
// [A1.11:5] Резерв
VGSig.fnDO_Processing(algOut := SHU_GVL.DGO.Reserv_2.PV, fromHMI := SHU_GVL.DGO.Reserv_2.FromHMI, toHMI := SHU_GVL.DGO.Reserv_2.ToHMI, drv => SHU_GVL.DGO.Reserv_2.DRV);
// [A1.11:6] Резерв
VGSig.fnDO_Processing(algOut := SHU_GVL.DGO.Reserv_3.PV, fromHMI := SHU_GVL.DGO.Reserv_3.FromHMI, toHMI := SHU_GVL.DGO.Reserv_3.ToHMI, drv => SHU_GVL.DGO.Reserv_3.DRV);
// [A1.11:7] Трехходовой клапан XV9610.1 на топливной линии открыть/закрыть
VGSig.fnDO_Processing(algOut := SHU_GVL.DGO.Kr10_ON.PV, fromHMI := SHU_GVL.DGO.Kr10_ON.FromHMI, toHMI := SHU_GVL.DGO.Kr10_ON.ToHMI, drv => SHU_GVL.DGO.Kr10_ON.DRV);
// [A1.11:8] Клапан пускового воздуха XV9608.1 открыть/закрыть
VGSig.fnDO_Processing(algOut := SHU_GVL.DGO.Kr8_ON.PV, fromHMI := SHU_GVL.DGO.Kr8_ON.FromHMI, toHMI := SHU_GVL.DGO.Kr8_ON.ToHMI, drv => SHU_GVL.DGO.Kr8_ON.DRV);
// [A1.11:9] Резерв
VGSig.fnDO_Processing(algOut := SHU_GVL.DGO.Reserv_4.PV, fromHMI := SHU_GVL.DGO.Reserv_4.FromHMI, toHMI := SHU_GVL.DGO.Reserv_4.ToHMI, drv => SHU_GVL.DGO.Reserv_4.DRV);
// [A1.11:10] Резерв
VGSig.fnDO_Processing(algOut := SHU_GVL.DGO.Reserv_5.PV, fromHMI := SHU_GVL.DGO.Reserv_5.FromHMI, toHMI := SHU_GVL.DGO.Reserv_5.ToHMI, drv => SHU_GVL.DGO.Reserv_5.DRV);
// [A1.11:11] Предпусковой насос прокачки масла включить
VGSig.fnDO_Processing(algOut := SHU_GVL.DGO.Pmp_ppm_ON.PV, fromHMI := SHU_GVL.DGO.Pmp_ppm_ON.FromHMI, toHMI := SHU_GVL.DGO.Pmp_ppm_ON.ToHMI, drv => SHU_GVL.DGO.Pmp_ppm_ON.DRV);
// [A1.11:12] Предпусковой насос прокачки масла отключить
VGSig.fnDO_Processing(algOut := SHU_GVL.DGO.Pmp_ppm_OF.PV, fromHMI := SHU_GVL.DGO.Pmp_ppm_OF.FromHMI, toHMI := SHU_GVL.DGO.Pmp_ppm_OF.ToHMI, drv => SHU_GVL.DGO.Pmp_ppm_OF.DRV);
// [A1.11:13] Резерв
VGSig.fnDO_Processing(algOut := SHU_GVL.DGO.Reserv_6.PV, fromHMI := SHU_GVL.DGO.Reserv_6.FromHMI, toHMI := SHU_GVL.DGO.Reserv_6.ToHMI, drv => SHU_GVL.DGO.Reserv_6.DRV);
// [A1.11:14] Резерв
VGSig.fnDO_Processing(algOut := SHU_GVL.DGO.Reserv_7.PV, fromHMI := SHU_GVL.DGO.Reserv_7.FromHMI, toHMI := SHU_GVL.DGO.Reserv_7.ToHMI, drv => SHU_GVL.DGO.Reserv_7.DRV);
// [A1.11:17] Включить зажигание
VGSig.fnDO_Processing(algOut := SHU_GVL.DGO.Zazh_ON.PV, fromHMI := SHU_GVL.DGO.Zazh_ON.FromHMI, toHMI := SHU_GVL.DGO.Zazh_ON.ToHMI, drv => SHU_GVL.DGO.Zazh_ON.DRV);
// [A1.11:18] Резерв
VGSig.fnDO_Processing(algOut := SHU_GVL.DGO.Reserv_8.PV, fromHMI := SHU_GVL.DGO.Reserv_8.FromHMI, toHMI := SHU_GVL.DGO.Reserv_8.ToHMI, drv => SHU_GVL.DGO.Reserv_8.DRV);
// [A1.11:19] Резерв
VGSig.fnDO_Processing(algOut := SHU_GVL.DGO.Reserv_9.PV, fromHMI := SHU_GVL.DGO.Reserv_9.FromHMI, toHMI := SHU_GVL.DGO.Reserv_9.ToHMI, drv => SHU_GVL.DGO.Reserv_9.DRV);
// [A1.11:20] Резерв
VGSig.fnDO_Processing(algOut := SHU_GVL.DGO.Reserv_10.PV, fromHMI := SHU_GVL.DGO.Reserv_10.FromHMI, toHMI := SHU_GVL.DGO.Reserv_10.ToHMI, drv => SHU_GVL.DGO.Reserv_10.DRV);
// [A1.11:21] Резерв
VGSig.fnDO_Processing(algOut := SHU_GVL.DGO.Reserv_11.PV, fromHMI := SHU_GVL.DGO.Reserv_11.FromHMI, toHMI := SHU_GVL.DGO.Reserv_11.ToHMI, drv => SHU_GVL.DGO.Reserv_11.DRV);
// [A1.11:22] Резерв
VGSig.fnDO_Processing(algOut := SHU_GVL.DGO.Reserv_12.PV, fromHMI := SHU_GVL.DGO.Reserv_12.FromHMI, toHMI := SHU_GVL.DGO.Reserv_12.ToHMI, drv => SHU_GVL.DGO.Reserv_12.DRV);
// [A1.11:23] Резерв
VGSig.fnDO_Processing(algOut := SHU_GVL.DGO.Reserv_13.PV, fromHMI := SHU_GVL.DGO.Reserv_13.FromHMI, toHMI := SHU_GVL.DGO.Reserv_13.ToHMI, drv => SHU_GVL.DGO.Reserv_13.DRV);
// [A1.11:24] Резерв
VGSig.fnDO_Processing(algOut := SHU_GVL.DGO.Reserv_14.PV, fromHMI := SHU_GVL.DGO.Reserv_14.FromHMI, toHMI := SHU_GVL.DGO.Reserv_14.ToHMI, drv => SHU_GVL.DGO.Reserv_14.DRV);
// [A1.11:25] Сирена на двери "ПС"
VGSig.fnDO_Processing(algOut := SHU_GVL.DGO.Snd_PS.PV, fromHMI := SHU_GVL.DGO.Snd_PS.FromHMI, toHMI := SHU_GVL.DGO.Snd_PS.ToHMI, drv => SHU_GVL.DGO.Snd_PS.DRV);
// [A1.11:26] Сирена на двери "АС"
VGSig.fnDO_Processing(algOut := SHU_GVL.DGO.Snd_AS.PV, fromHMI := SHU_GVL.DGO.Snd_AS.FromHMI, toHMI := SHU_GVL.DGO.Snd_AS.ToHMI, drv => SHU_GVL.DGO.Snd_AS.DRV);
// [A1.11:27] Световая индикатор на двери "ПС"
VGSig.fnDO_Processing(algOut := SHU_GVL.DGO.SvetInd_PS.PV, fromHMI := SHU_GVL.DGO.SvetInd_PS.FromHMI, toHMI := SHU_GVL.DGO.SvetInd_PS.ToHMI, drv => SHU_GVL.DGO.SvetInd_PS.DRV);
// [A1.11:28] Световая индикатор на двери "АС"
VGSig.fnDO_Processing(algOut := SHU_GVL.DGO.SvetInd_AS.PV, fromHMI := SHU_GVL.DGO.SvetInd_AS.FromHMI, toHMI := SHU_GVL.DGO.SvetInd_AS.ToHMI, drv => SHU_GVL.DGO.SvetInd_AS.DRV);
// [A1.11:29] Световая индикация кнопки на двери "АО"
VGSig.fnDO_Processing(algOut := SHU_GVL.DGO.SvetInd_Btn_AO.PV, fromHMI := SHU_GVL.DGO.SvetInd_Btn_AO.FromHMI, toHMI := SHU_GVL.DGO.SvetInd_Btn_AO.ToHMI, drv => SHU_GVL.DGO.SvetInd_Btn_AO.DRV);
// [A1.11:30] Световая индикация кнопки на двери "НО"
VGSig.fnDO_Processing(algOut := SHU_GVL.DGO.SvetInd_Btn_NO.PV, fromHMI := SHU_GVL.DGO.SvetInd_Btn_NO.FromHMI, toHMI := SHU_GVL.DGO.SvetInd_Btn_NO.ToHMI, drv => SHU_GVL.DGO.SvetInd_Btn_NO.DRV);
// [A1.11:31] Исправность контроллера ЛСУ
VGSig.fnDO_Processing(algOut := SHU_GVL.DGO.Meandr.PV, fromHMI := SHU_GVL.DGO.Meandr.FromHMI, toHMI := SHU_GVL.DGO.Meandr.ToHMI, drv => SHU_GVL.DGO.Meandr.DRV);
"""
proj = projects.primary
folder = proj.find('DO SHU', recursive=True)[0]
struktur = folder.create_pou('SHU_DO_Call', type = PouType.Function,language=None, return_type='BOOL', base_type=None, interfaces=None)
struktur.textual_declaration.insert(4, 0, CONTENT_var)
struktur.textual_implementation.insert(0, 0, CONTENT_body)
