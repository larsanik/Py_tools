#encoding:utf-8
from __future__ import print_function
CONTENT_var = """\
"""
CONTENT_body = """\
//================ Привязка входов к HW ================
SHU_GVL.DGI.Kr1_ON.DRV := SHU_GVL.A1_8.in_ch.0; //Клапан ESDV9601.1 на приёме ГМК открыт
SHU_GVL.DGI.Kr1_OF.DRV := SHU_GVL.A1_8.in_ch.1; //Клапан ESDV9601.1 на приёме ГМК закрыт
SHU_GVL.DGI.Kr2_ON.DRV := SHU_GVL.A1_8.in_ch.2; //Клапан ESDV9602.1 на выходе ГМК открыт
SHU_GVL.DGI.Kr2_OF.DRV := SHU_GVL.A1_8.in_ch.3; //Клапан ESDV9602.1 на выходе ГМК закрыт
SHU_GVL.DGI.Kr5_ON.DRV := SHU_GVL.A1_8.in_ch.4; //Клапан XV9605.1 на перемычке открыт
SHU_GVL.DGI.Kr5_OF.DRV := SHU_GVL.A1_8.in_ch.5; //Клапан XV9605.1 на перемычке закрыт
SHU_GVL.DGI.Kr13_ON.DRV := SHU_GVL.A1_8.in_ch.6; //Клапан XV9613.1 на сбросе приёмной линии открыт
SHU_GVL.DGI.Kr13_OF.DRV := SHU_GVL.A1_8.in_ch.7; //Клапан XV9613.1 на сбросе приёмной линии закрыт
SHU_GVL.DGI.Reserv_0.DRV := SHU_GVL.A1_8.in_ch.8; //Резерв
SHU_GVL.DGI.Reserv_1.DRV := SHU_GVL.A1_8.in_ch.9; //Резерв
SHU_GVL.DGI.Reserv_2.DRV := SHU_GVL.A1_8.in_ch.10; //Резерв
SHU_GVL.DGI.Reserv_3.DRV := SHU_GVL.A1_8.in_ch.11; //Резерв
SHU_GVL.DGI.Kr10_ON.DRV := SHU_GVL.A1_8.in_ch.12; //Трехходовой клапан XV9610.1 на топливной линии открыт
SHU_GVL.DGI.Kr10_OF.DRV := SHU_GVL.A1_8.in_ch.13; //Трехходовой клапан XV9610.1 на топливной линии закрыт
SHU_GVL.DGI.Kr8_ON.DRV := SHU_GVL.A1_8.in_ch.14; //Клапан пускового воздуха XV9608.1 открыт
SHU_GVL.DGI.Kr8_OF.DRV := SHU_GVL.A1_8.in_ch.15; //Клапан пускового воздуха XV9608.1 закрыт
SHU_GVL.DGI.Pmp_ppm_ON.DRV := SHU_GVL.A1_8.in_ch.16; //Насос прокачки масла включен
SHU_GVL.DGI.Pmp_ppm_AU.DRV := SHU_GVL.A1_8.in_ch.17; //Насос прокачки масла в автоматическом управлении
SHU_GVL.DGI.A_Pmp_ppm.DRV := SHU_GVL.A1_8.in_ch.18; //Авария насоса прокачки масла
SHU_GVL.DGI.Reserv_4.DRV := SHU_GVL.A1_8.in_ch.19; //Резерв
SHU_GVL.DGI.Reserv_5.DRV := SHU_GVL.A1_8.in_ch.20; //Резерв
SHU_GVL.DGI.Reserv_6.DRV := SHU_GVL.A1_8.in_ch.21; //Резерв
SHU_GVL.DGI.Reserv_7.DRV := SHU_GVL.A1_8.in_ch.22; //Резерв
SHU_GVL.DGI.Reserv_8.DRV := SHU_GVL.A1_8.in_ch.23; //Резерв
SHU_GVL.DGI.Zazh_ON.DRV := SHU_GVL.A1_8.in_ch.24; //Зажигание в работе
SHU_GVL.DGI.Kr11_ON.DRV := SHU_GVL.A1_8.in_ch.25; //Клапан ESDV9611.1 на топливной линии открыт
SHU_GVL.DGI.Kr11_OF.DRV := SHU_GVL.A1_8.in_ch.26; //Клапан ESDV9611.1 на топливной линии закрыт
SHU_GVL.DGI.Reserv_9.DRV := SHU_GVL.A1_8.in_ch.27; //Резерв
SHU_GVL.DGI.U_Osn_AC_ON.DRV := SHU_GVL.A1_9.in_ch.8; //Контроль основного пит. ШУ ГМК ~220 В
SHU_GVL.DGI.U_Res_AC_ON.DRV := SHU_GVL.A1_9.in_ch.9; //Контроль резервного пит. ШУ ГМК ~220 В
SHU_GVL.DGI.RazrGood.DRV := SHU_GVL.A1_9.in_ch.10; //Контроль исправности разрядников
SHU_GVL.DGI.AvtPwr_ON.DRV := SHU_GVL.A1_9.in_ch.11; //Автоматы питания включены
SHU_GVL.DGI.DoorOpen.DRV := SHU_GVL.A1_9.in_ch.12; //Двери ШУ ГМК открыты
SHU_GVL.DGI.Ispr_Osn_DC_inC.DRV := SHU_GVL.A1_9.in_ch.13; //Исправность осн. ИП =24 В внутр. цепей
SHU_GVL.DGI.Ispr_Res_DC_inC.DRV := SHU_GVL.A1_9.in_ch.14; //Исправность рез. ИП =24 В внутр. цепей
SHU_GVL.DGI.Ispr_Osn_DC_AI.DRV := SHU_GVL.A1_9.in_ch.15; //Исправность осн. ИП =24 В AI
SHU_GVL.DGI.Ispr_Res_DC_AI.DRV := SHU_GVL.A1_9.in_ch.16; //Исправность рез. ИП =24 В AI
SHU_GVL.DGI.Ispr_Osn_DC_DI.DRV := SHU_GVL.A1_9.in_ch.17; //Исправность осн. ИП =24 В DI (внеш.)
SHU_GVL.DGI.Ispr_Res_DC_DI.DRV := SHU_GVL.A1_9.in_ch.18; //Исправность рез. ИП =24 В DI (внеш.)
SHU_GVL.DGI.Ispr_Osn_DC_DO.DRV := SHU_GVL.A1_9.in_ch.19; //Исправность осн. ИП =24 В DO (внеш.)
SHU_GVL.DGI.Ispr_Res_DC_DO.DRV := SHU_GVL.A1_9.in_ch.20; //Исправность рез. ИП =24 В DO (внеш.)
SHU_GVL.DGI.Btn_AO.DRV := SHU_GVL.A1_9.in_ch.21; //Кнопка на двери "Аварийный останов"
SHU_GVL.DGI.Btn_NO.DRV := SHU_GVL.A1_9.in_ch.22; //Кнопка на двери "Нормальный останов"
SHU_GVL.DGI.Btn_Deblock.DRV := SHU_GVL.A1_9.in_ch.23; //Кнопка на двери "Деблокировка"
SHU_GVL.DGI.U_AC_outC_ON.DRV := SHU_GVL.A1_9.in_ch.24; //Контроль внешнего питания ~220 В от ШУ ГМК
"""
proj = projects.primary
folder = proj.find('DI SHU', recursive=True)[0]
struktur = folder.create_pou('SHU_DI_binding_Hw_to_Lg', type = PouType.Function,language=None, return_type='BOOL', base_type=None, interfaces=None)
struktur.textual_declaration.insert(4, 0, CONTENT_var)
struktur.textual_implementation.insert(0, 0, CONTENT_body)
