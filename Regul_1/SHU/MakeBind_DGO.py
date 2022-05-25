#encoding:utf-8
from __future__ import print_function
CONTENT_var = """\
"""
CONTENT_body = """\
//================ Привязка вЫходов к HW ================
SHU_GVL.A1_11.out_ch.0 := SHU_GVL.DGO.Reserv_0.DRV; //Резерв
SHU_GVL.A1_11.out_ch.1 := SHU_GVL.DGO.Reserv_1.DRV; //Резерв
SHU_GVL.A1_11.out_ch.2 := SHU_GVL.DGO.Kr5_ON.DRV; //Клапан XV9605.1 на перемычке открыть/закрыть
SHU_GVL.A1_11.out_ch.3 := SHU_GVL.DGO.Kr13_ON.DRV; //Клапан XV9613.1 на сбросе приёмной линии открыть/закрыть
SHU_GVL.A1_11.out_ch.4 := SHU_GVL.DGO.Reserv_2.DRV; //Резерв
SHU_GVL.A1_11.out_ch.5 := SHU_GVL.DGO.Reserv_3.DRV; //Резерв
SHU_GVL.A1_11.out_ch.6 := SHU_GVL.DGO.Kr10_ON.DRV; //Трехходовой клапан XV9610.1 на топливной линии открыть/закрыть
SHU_GVL.A1_11.out_ch.7 := SHU_GVL.DGO.Kr8_ON.DRV; //Клапан пускового воздуха XV9608.1 открыть/закрыть
SHU_GVL.A1_11.out_ch.8 := SHU_GVL.DGO.Reserv_4.DRV; //Резерв
SHU_GVL.A1_11.out_ch.9 := SHU_GVL.DGO.Reserv_5.DRV; //Резерв
SHU_GVL.A1_11.out_ch.10 := SHU_GVL.DGO.Pmp_ppm_ON.DRV; //Предпусковой насос прокачки масла включить
SHU_GVL.A1_11.out_ch.11 := SHU_GVL.DGO.Pmp_ppm_OF.DRV; //Предпусковой насос прокачки масла отключить
SHU_GVL.A1_11.out_ch.12 := SHU_GVL.DGO.Reserv_6.DRV; //Резерв
SHU_GVL.A1_11.out_ch.13 := SHU_GVL.DGO.Reserv_7.DRV; //Резерв
SHU_GVL.A1_11.out_ch.16 := SHU_GVL.DGO.Zazh_ON.DRV; //Включить зажигание
SHU_GVL.A1_11.out_ch.17 := SHU_GVL.DGO.Reserv_8.DRV; //Резерв
SHU_GVL.A1_11.out_ch.18 := SHU_GVL.DGO.Reserv_9.DRV; //Резерв
SHU_GVL.A1_11.out_ch.19 := SHU_GVL.DGO.Reserv_10.DRV; //Резерв
SHU_GVL.A1_11.out_ch.20 := SHU_GVL.DGO.Reserv_11.DRV; //Резерв
SHU_GVL.A1_11.out_ch.21 := SHU_GVL.DGO.Reserv_12.DRV; //Резерв
SHU_GVL.A1_11.out_ch.22 := SHU_GVL.DGO.Reserv_13.DRV; //Резерв
SHU_GVL.A1_11.out_ch.23 := SHU_GVL.DGO.Reserv_14.DRV; //Резерв
SHU_GVL.A1_11.out_ch.24 := SHU_GVL.DGO.Snd_PS.DRV; //Сирена на двери "ПС"
SHU_GVL.A1_11.out_ch.25 := SHU_GVL.DGO.Snd_AS.DRV; //Сирена на двери "АС"
SHU_GVL.A1_11.out_ch.26 := SHU_GVL.DGO.SvetInd_PS.DRV; //Световая индикатор на двери "ПС"
SHU_GVL.A1_11.out_ch.27 := SHU_GVL.DGO.SvetInd_AS.DRV; //Световая индикатор на двери "АС"
SHU_GVL.A1_11.out_ch.28 := SHU_GVL.DGO.SvetInd_Btn_AO.DRV; //Световая индикация кнопки на двери "АО"
SHU_GVL.A1_11.out_ch.29 := SHU_GVL.DGO.SvetInd_Btn_NO.DRV; //Световая индикация кнопки на двери "НО"
SHU_GVL.A1_11.out_ch.30 := SHU_GVL.DGO.Meandr.DRV; //Исправность контроллера ЛСУ
"""
proj = projects.primary
folder = proj.find('DO SHU', recursive=True)[0]
struktur = folder.create_pou('SHU_DO_binding_Lg_to_Hw', type = PouType.Function,language=None, return_type='BOOL', base_type=None, interfaces=None)
struktur.textual_declaration.insert(4, 0, CONTENT_var)
struktur.textual_implementation.insert(0, 0, CONTENT_body)
