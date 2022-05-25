#encoding:utf-8
from __future__ import print_function
CONTENT_var = """\
"""
CONTENT_body = """\
//================ Обработчик дискретных выходов================
// [A1.11:1] Клапан ESDV9601.1 на приёме ГМК открыть/закрыть
VGSig.fnDO_Processing(algOut := PAZ_GVL.DGO.Kl_ESDV9601_1_ON.PV, fromHMI := PAZ_GVL.DGO.Kl_ESDV9601_1_ON.FromHMI, toHMI := PAZ_GVL.DGO.Kl_ESDV9601_1_ON.ToHMI, drv => PAZ_GVL.DGO.Kl_ESDV9601_1_ON.DRV);
// [A1.11:2] Клапан ESDV9602.1 на выходе ГМК открыть/закрыть
VGSig.fnDO_Processing(algOut := PAZ_GVL.DGO.Kl_ESDV9602_1_ON.PV, fromHMI := PAZ_GVL.DGO.Kl_ESDV9602_1_ON.FromHMI, toHMI := PAZ_GVL.DGO.Kl_ESDV9602_1_ON.ToHMI, drv => PAZ_GVL.DGO.Kl_ESDV9602_1_ON.DRV);
// [A1.11:3] Клапан ESDV9611.1 на топливной линии открыть/закрыть
VGSig.fnDO_Processing(algOut := PAZ_GVL.DGO.Kl_ESDV9611_1_ON.PV, fromHMI := PAZ_GVL.DGO.Kl_ESDV9611_1_ON.FromHMI, toHMI := PAZ_GVL.DGO.Kl_ESDV9611_1_ON.ToHMI, drv => PAZ_GVL.DGO.Kl_ESDV9611_1_ON.DRV);
// [A1.11:4] Резерв
VGSig.fnDO_Processing(algOut := PAZ_GVL.DGO.Reserv_0.PV, fromHMI := PAZ_GVL.DGO.Reserv_0.FromHMI, toHMI := PAZ_GVL.DGO.Reserv_0.ToHMI, drv => PAZ_GVL.DGO.Reserv_0.DRV);
// [A1.11:5] Клапан ESDV9601.2 на приёме ГМК открыть/закрыть
VGSig.fnDO_Processing(algOut := PAZ_GVL.DGO.Kl_ESDV9601_2_ON.PV, fromHMI := PAZ_GVL.DGO.Kl_ESDV9601_2_ON.FromHMI, toHMI := PAZ_GVL.DGO.Kl_ESDV9601_2_ON.ToHMI, drv => PAZ_GVL.DGO.Kl_ESDV9601_2_ON.DRV);
// [A1.11:6] Клапан ESDV9602.2 на выходе ГМК открыть/закрыть
VGSig.fnDO_Processing(algOut := PAZ_GVL.DGO.Kl_ESDV9602_2_ON.PV, fromHMI := PAZ_GVL.DGO.Kl_ESDV9602_2_ON.FromHMI, toHMI := PAZ_GVL.DGO.Kl_ESDV9602_2_ON.ToHMI, drv => PAZ_GVL.DGO.Kl_ESDV9602_2_ON.DRV);
// [A1.11:7] Клапан ESDV9611.2 на топливной линии открыть/закрыть
VGSig.fnDO_Processing(algOut := PAZ_GVL.DGO.Kl_ESDV9611_2_ON.PV, fromHMI := PAZ_GVL.DGO.Kl_ESDV9611_2_ON.FromHMI, toHMI := PAZ_GVL.DGO.Kl_ESDV9611_2_ON.ToHMI, drv => PAZ_GVL.DGO.Kl_ESDV9611_2_ON.DRV);
// [A1.11:8] Резерв
VGSig.fnDO_Processing(algOut := PAZ_GVL.DGO.Reserv_1.PV, fromHMI := PAZ_GVL.DGO.Reserv_1.FromHMI, toHMI := PAZ_GVL.DGO.Reserv_1.ToHMI, drv => PAZ_GVL.DGO.Reserv_1.DRV);
// [A1.12:1] Клапан ESDV9601.3 на приёме ГМК открыть/закрыть
VGSig.fnDO_Processing(algOut := PAZ_GVL.DGO.Kl_ESDV9601_3_ON.PV, fromHMI := PAZ_GVL.DGO.Kl_ESDV9601_3_ON.FromHMI, toHMI := PAZ_GVL.DGO.Kl_ESDV9601_3_ON.ToHMI, drv => PAZ_GVL.DGO.Kl_ESDV9601_3_ON.DRV);
// [A1.12:2] Клапан ESDV9602.3 на выходе ГМК открыть/закрыть
VGSig.fnDO_Processing(algOut := PAZ_GVL.DGO.Kl_ESDV9602_3_ON.PV, fromHMI := PAZ_GVL.DGO.Kl_ESDV9602_3_ON.FromHMI, toHMI := PAZ_GVL.DGO.Kl_ESDV9602_3_ON.ToHMI, drv => PAZ_GVL.DGO.Kl_ESDV9602_3_ON.DRV);
// [A1.12:3] Клапан ESDV9611.3 на топливной линии открыть/закрыть
VGSig.fnDO_Processing(algOut := PAZ_GVL.DGO.Kl_ESDV9611_3_ON.PV, fromHMI := PAZ_GVL.DGO.Kl_ESDV9611_3_ON.FromHMI, toHMI := PAZ_GVL.DGO.Kl_ESDV9611_3_ON.ToHMI, drv => PAZ_GVL.DGO.Kl_ESDV9611_3_ON.DRV);
// [A1.12:4] Резерв
VGSig.fnDO_Processing(algOut := PAZ_GVL.DGO.Reserv_2.PV, fromHMI := PAZ_GVL.DGO.Reserv_2.FromHMI, toHMI := PAZ_GVL.DGO.Reserv_2.ToHMI, drv => PAZ_GVL.DGO.Reserv_2.DRV);
// [A1.12:5] Клапан ESDV9601.4 на приёме ГМК открыть/закрыть
VGSig.fnDO_Processing(algOut := PAZ_GVL.DGO.Kl_ESDV9601_4_ON.PV, fromHMI := PAZ_GVL.DGO.Kl_ESDV9601_4_ON.FromHMI, toHMI := PAZ_GVL.DGO.Kl_ESDV9601_4_ON.ToHMI, drv => PAZ_GVL.DGO.Kl_ESDV9601_4_ON.DRV);
// [A1.12:6] Клапан ESDV9602.4 на выходе ГМК открыть/закрыть
VGSig.fnDO_Processing(algOut := PAZ_GVL.DGO.Kl_ESDV9602_4_ON.PV, fromHMI := PAZ_GVL.DGO.Kl_ESDV9602_4_ON.FromHMI, toHMI := PAZ_GVL.DGO.Kl_ESDV9602_4_ON.ToHMI, drv => PAZ_GVL.DGO.Kl_ESDV9602_4_ON.DRV);
// [A1.12:7] Клапан ESDV9611.4 на топливной линии открыть/закрыть
VGSig.fnDO_Processing(algOut := PAZ_GVL.DGO.Kl_ESDV9611_4_ON.PV, fromHMI := PAZ_GVL.DGO.Kl_ESDV9611_4_ON.FromHMI, toHMI := PAZ_GVL.DGO.Kl_ESDV9611_4_ON.ToHMI, drv => PAZ_GVL.DGO.Kl_ESDV9611_4_ON.DRV);
// [A1.12:8] Резерв
VGSig.fnDO_Processing(algOut := PAZ_GVL.DGO.Reserv_3.PV, fromHMI := PAZ_GVL.DGO.Reserv_3.FromHMI, toHMI := PAZ_GVL.DGO.Reserv_3.ToHMI, drv => PAZ_GVL.DGO.Reserv_3.DRV);
// [A1.13:1] Клапан ESDV9601.5 на приёме ГМК открыть/закрыть
VGSig.fnDO_Processing(algOut := PAZ_GVL.DGO.Kl_ESDV9601_5_ON.PV, fromHMI := PAZ_GVL.DGO.Kl_ESDV9601_5_ON.FromHMI, toHMI := PAZ_GVL.DGO.Kl_ESDV9601_5_ON.ToHMI, drv => PAZ_GVL.DGO.Kl_ESDV9601_5_ON.DRV);
// [A1.13:2] Клапан ESDV9602.5 на выходе ГМК открыть/закрыть
VGSig.fnDO_Processing(algOut := PAZ_GVL.DGO.Kl_ESDV9602_5_ON.PV, fromHMI := PAZ_GVL.DGO.Kl_ESDV9602_5_ON.FromHMI, toHMI := PAZ_GVL.DGO.Kl_ESDV9602_5_ON.ToHMI, drv => PAZ_GVL.DGO.Kl_ESDV9602_5_ON.DRV);
// [A1.13:3] Клапан ESDV9611.5 на топливной линии открыть/закрыть
VGSig.fnDO_Processing(algOut := PAZ_GVL.DGO.Kl_ESDV9611_5_ON.PV, fromHMI := PAZ_GVL.DGO.Kl_ESDV9611_5_ON.FromHMI, toHMI := PAZ_GVL.DGO.Kl_ESDV9611_5_ON.ToHMI, drv => PAZ_GVL.DGO.Kl_ESDV9611_5_ON.DRV);
// [A1.13:4] Резерв
VGSig.fnDO_Processing(algOut := PAZ_GVL.DGO.Reserv_4.PV, fromHMI := PAZ_GVL.DGO.Reserv_4.FromHMI, toHMI := PAZ_GVL.DGO.Reserv_4.ToHMI, drv => PAZ_GVL.DGO.Reserv_4.DRV);
// [A1.13:5] Клапан ESDV9601.6 на приёме ГМК открыть/закрыть
VGSig.fnDO_Processing(algOut := PAZ_GVL.DGO.Kl_ESDV9601_6_ON.PV, fromHMI := PAZ_GVL.DGO.Kl_ESDV9601_6_ON.FromHMI, toHMI := PAZ_GVL.DGO.Kl_ESDV9601_6_ON.ToHMI, drv => PAZ_GVL.DGO.Kl_ESDV9601_6_ON.DRV);
// [A1.13:6] Клапан ESDV9602.6 на выходе ГМК открыть/закрыть
VGSig.fnDO_Processing(algOut := PAZ_GVL.DGO.Kl_ESDV9602_6_ON.PV, fromHMI := PAZ_GVL.DGO.Kl_ESDV9602_6_ON.FromHMI, toHMI := PAZ_GVL.DGO.Kl_ESDV9602_6_ON.ToHMI, drv => PAZ_GVL.DGO.Kl_ESDV9602_6_ON.DRV);
// [A1.13:7] Клапан ESDV9611.6 на топливной линии открыть/закрыть
VGSig.fnDO_Processing(algOut := PAZ_GVL.DGO.Kl_ESDV9611_6_ON.PV, fromHMI := PAZ_GVL.DGO.Kl_ESDV9611_6_ON.FromHMI, toHMI := PAZ_GVL.DGO.Kl_ESDV9611_6_ON.ToHMI, drv => PAZ_GVL.DGO.Kl_ESDV9611_6_ON.DRV);
// [A1.13:8] Резерв
VGSig.fnDO_Processing(algOut := PAZ_GVL.DGO.Reserv_5.PV, fromHMI := PAZ_GVL.DGO.Reserv_5.FromHMI, toHMI := PAZ_GVL.DGO.Reserv_5.ToHMI, drv => PAZ_GVL.DGO.Reserv_5.DRV);
// [A1.14:1] Клапан ESDV9601.7 на приёме ГМК открыть/закрыть
VGSig.fnDO_Processing(algOut := PAZ_GVL.DGO.Kl_ESDV9601_7_ON.PV, fromHMI := PAZ_GVL.DGO.Kl_ESDV9601_7_ON.FromHMI, toHMI := PAZ_GVL.DGO.Kl_ESDV9601_7_ON.ToHMI, drv => PAZ_GVL.DGO.Kl_ESDV9601_7_ON.DRV);
// [A1.14:2] Клапан ESDV9602.7 на выходе ГМК открыть/закрыть
VGSig.fnDO_Processing(algOut := PAZ_GVL.DGO.Kl_ESDV9602_7_ON.PV, fromHMI := PAZ_GVL.DGO.Kl_ESDV9602_7_ON.FromHMI, toHMI := PAZ_GVL.DGO.Kl_ESDV9602_7_ON.ToHMI, drv => PAZ_GVL.DGO.Kl_ESDV9602_7_ON.DRV);
// [A1.14:3] Клапан ESDV9611.7 на топливной линии открыть/закрыть
VGSig.fnDO_Processing(algOut := PAZ_GVL.DGO.Kl_ESDV9611_7_ON.PV, fromHMI := PAZ_GVL.DGO.Kl_ESDV9611_7_ON.FromHMI, toHMI := PAZ_GVL.DGO.Kl_ESDV9611_7_ON.ToHMI, drv => PAZ_GVL.DGO.Kl_ESDV9611_7_ON.DRV);
// [A1.14:4] Резерв
VGSig.fnDO_Processing(algOut := PAZ_GVL.DGO.Reserv_6.PV, fromHMI := PAZ_GVL.DGO.Reserv_6.FromHMI, toHMI := PAZ_GVL.DGO.Reserv_6.ToHMI, drv => PAZ_GVL.DGO.Reserv_6.DRV);
// [A1.15:1] Аварийный останов в ГМК №44 (сигнал в ЛСУ)
VGSig.fnDO_Processing(algOut := PAZ_GVL.DGO.AO_v_GMK_44_signal_v_LSU.PV, fromHMI := PAZ_GVL.DGO.AO_v_GMK_44_signal_v_LSU.FromHMI, toHMI := PAZ_GVL.DGO.AO_v_GMK_44_signal_v_LSU.ToHMI, drv => PAZ_GVL.DGO.AO_v_GMK_44_signal_v_LSU.DRV);
// [A1.15:2] Аварийный останов в ГМК №45 (сигнал в ЛСУ)
VGSig.fnDO_Processing(algOut := PAZ_GVL.DGO.AO_v_GMK_45_signal_v_LSU.PV, fromHMI := PAZ_GVL.DGO.AO_v_GMK_45_signal_v_LSU.FromHMI, toHMI := PAZ_GVL.DGO.AO_v_GMK_45_signal_v_LSU.ToHMI, drv => PAZ_GVL.DGO.AO_v_GMK_45_signal_v_LSU.DRV);
// [A1.15:3] Аварийный останов в ГМК №46 (сигнал в ЛСУ)
VGSig.fnDO_Processing(algOut := PAZ_GVL.DGO.AO_v_GMK_46_signal_v_LSU.PV, fromHMI := PAZ_GVL.DGO.AO_v_GMK_46_signal_v_LSU.FromHMI, toHMI := PAZ_GVL.DGO.AO_v_GMK_46_signal_v_LSU.ToHMI, drv => PAZ_GVL.DGO.AO_v_GMK_46_signal_v_LSU.DRV);
// [A1.15:4] Аварийный останов в ГМК №47 (сигнал в ЛСУ)
VGSig.fnDO_Processing(algOut := PAZ_GVL.DGO.AO_v_GMK_47_signal_v_LSU.PV, fromHMI := PAZ_GVL.DGO.AO_v_GMK_47_signal_v_LSU.FromHMI, toHMI := PAZ_GVL.DGO.AO_v_GMK_47_signal_v_LSU.ToHMI, drv => PAZ_GVL.DGO.AO_v_GMK_47_signal_v_LSU.DRV);
// [A1.15:5] Аварийный останов в ГМК №48 (сигнал в ЛСУ)
VGSig.fnDO_Processing(algOut := PAZ_GVL.DGO.AO_v_GMK_48_signal_v_LSU.PV, fromHMI := PAZ_GVL.DGO.AO_v_GMK_48_signal_v_LSU.FromHMI, toHMI := PAZ_GVL.DGO.AO_v_GMK_48_signal_v_LSU.ToHMI, drv => PAZ_GVL.DGO.AO_v_GMK_48_signal_v_LSU.DRV);
// [A1.15:6] Аварийный останов в ГМК №51 (сигнал в ЛСУ)
VGSig.fnDO_Processing(algOut := PAZ_GVL.DGO.AO_v_GMK_51_signal_v_LSU.PV, fromHMI := PAZ_GVL.DGO.AO_v_GMK_51_signal_v_LSU.FromHMI, toHMI := PAZ_GVL.DGO.AO_v_GMK_51_signal_v_LSU.ToHMI, drv => PAZ_GVL.DGO.AO_v_GMK_51_signal_v_LSU.DRV);
// [A1.15:7] Аварийный останов в ГМК №52 (сигнал в ЛСУ)
VGSig.fnDO_Processing(algOut := PAZ_GVL.DGO.AO_v_GMK_52_signal_v_LSU.PV, fromHMI := PAZ_GVL.DGO.AO_v_GMK_52_signal_v_LSU.FromHMI, toHMI := PAZ_GVL.DGO.AO_v_GMK_52_signal_v_LSU.ToHMI, drv => PAZ_GVL.DGO.AO_v_GMK_52_signal_v_LSU.DRV);
// [A1.15:8] Аварийный останов в ГМК №44 (сигнал в АСУ ТП КУОГ)
VGSig.fnDO_Processing(algOut := PAZ_GVL.DGO.AO_v_GMK_44_signal_v_ASUTP_KUOG.PV, fromHMI := PAZ_GVL.DGO.AO_v_GMK_44_signal_v_ASUTP_KUOG.FromHMI, toHMI := PAZ_GVL.DGO.AO_v_GMK_44_signal_v_ASUTP_KUOG.ToHMI, drv => PAZ_GVL.DGO.AO_v_GMK_44_signal_v_ASUTP_KUOG.DRV);
// [A1.15:9] Аварийный останов в ГМК №45 (сигнал в АСУ ТП КУОГ)
VGSig.fnDO_Processing(algOut := PAZ_GVL.DGO.AO_v_GMK_45_signal_v_ASUTP_KUOG.PV, fromHMI := PAZ_GVL.DGO.AO_v_GMK_45_signal_v_ASUTP_KUOG.FromHMI, toHMI := PAZ_GVL.DGO.AO_v_GMK_45_signal_v_ASUTP_KUOG.ToHMI, drv => PAZ_GVL.DGO.AO_v_GMK_45_signal_v_ASUTP_KUOG.DRV);
// [A1.15:10] Аварийный останов в ГМК №46 (сигнал в АСУ ТП КУОГ)
VGSig.fnDO_Processing(algOut := PAZ_GVL.DGO.AO_v_GMK_46_signal_v_ASUTP_KUOG.PV, fromHMI := PAZ_GVL.DGO.AO_v_GMK_46_signal_v_ASUTP_KUOG.FromHMI, toHMI := PAZ_GVL.DGO.AO_v_GMK_46_signal_v_ASUTP_KUOG.ToHMI, drv => PAZ_GVL.DGO.AO_v_GMK_46_signal_v_ASUTP_KUOG.DRV);
// [A1.15:11] Аварийный останов в ГМК №47 (сигнал в АСУ ТП КУОГ)
VGSig.fnDO_Processing(algOut := PAZ_GVL.DGO.AO_v_GMK_47_signal_v_ASUTP_KUOG.PV, fromHMI := PAZ_GVL.DGO.AO_v_GMK_47_signal_v_ASUTP_KUOG.FromHMI, toHMI := PAZ_GVL.DGO.AO_v_GMK_47_signal_v_ASUTP_KUOG.ToHMI, drv => PAZ_GVL.DGO.AO_v_GMK_47_signal_v_ASUTP_KUOG.DRV);
// [A1.15:12] Аварийный останов в ГМК №48 (сигнал в АСУ ТП КУОГ)
VGSig.fnDO_Processing(algOut := PAZ_GVL.DGO.AO_v_GMK_48_signal_v_ASUTP_KUOG.PV, fromHMI := PAZ_GVL.DGO.AO_v_GMK_48_signal_v_ASUTP_KUOG.FromHMI, toHMI := PAZ_GVL.DGO.AO_v_GMK_48_signal_v_ASUTP_KUOG.ToHMI, drv => PAZ_GVL.DGO.AO_v_GMK_48_signal_v_ASUTP_KUOG.DRV);
// [A1.15:13] Аварийный останов в ГМК №51 (сигнал в АСУ ТП КУОГ)
VGSig.fnDO_Processing(algOut := PAZ_GVL.DGO.AO_v_GMK_51_signal_v_ASUTP_KUOG.PV, fromHMI := PAZ_GVL.DGO.AO_v_GMK_51_signal_v_ASUTP_KUOG.FromHMI, toHMI := PAZ_GVL.DGO.AO_v_GMK_51_signal_v_ASUTP_KUOG.ToHMI, drv => PAZ_GVL.DGO.AO_v_GMK_51_signal_v_ASUTP_KUOG.DRV);
// [A1.15:14] Аварийный останов в ГМК №52 (сигнал в АСУ ТП КУОГ)
VGSig.fnDO_Processing(algOut := PAZ_GVL.DGO.AO_v_GMK_52_signal_v_ASUTP_KUOG.PV, fromHMI := PAZ_GVL.DGO.AO_v_GMK_52_signal_v_ASUTP_KUOG.FromHMI, toHMI := PAZ_GVL.DGO.AO_v_GMK_52_signal_v_ASUTP_KUOG.ToHMI, drv => PAZ_GVL.DGO.AO_v_GMK_52_signal_v_ASUTP_KUOG.DRV);
// [A1.15:15] Резерв
VGSig.fnDO_Processing(algOut := PAZ_GVL.DGO.Reserv_7.PV, fromHMI := PAZ_GVL.DGO.Reserv_7.FromHMI, toHMI := PAZ_GVL.DGO.Reserv_7.ToHMI, drv => PAZ_GVL.DGO.Reserv_7.DRV);
// [A1.15:16] Резерв
VGSig.fnDO_Processing(algOut := PAZ_GVL.DGO.Reserv_8.PV, fromHMI := PAZ_GVL.DGO.Reserv_8.FromHMI, toHMI := PAZ_GVL.DGO.Reserv_8.ToHMI, drv => PAZ_GVL.DGO.Reserv_8.DRV);
// [A1.16:1] Клапан ESDV9601.1 на приёме ГМК открыт в ГМК44
VGSig.fnDO_Processing(algOut := PAZ_GVL.DGO.Kl_ESDV9601_1_ON_v_GMK44.PV, fromHMI := PAZ_GVL.DGO.Kl_ESDV9601_1_ON_v_GMK44.FromHMI, toHMI := PAZ_GVL.DGO.Kl_ESDV9601_1_ON_v_GMK44.ToHMI, drv => PAZ_GVL.DGO.Kl_ESDV9601_1_ON_v_GMK44.DRV);
// [A1.16:2] Клапан ESDV9601.1 на приёме ГМК закрыт в ГМК44
VGSig.fnDO_Processing(algOut := PAZ_GVL.DGO.Kl_ESDV9601_1_OF_v_GMK44.PV, fromHMI := PAZ_GVL.DGO.Kl_ESDV9601_1_OF_v_GMK44.FromHMI, toHMI := PAZ_GVL.DGO.Kl_ESDV9601_1_OF_v_GMK44.ToHMI, drv => PAZ_GVL.DGO.Kl_ESDV9601_1_OF_v_GMK44.DRV);
// [A1.16:3] Клапан ESDV9602.1 на выходе ГМК открыт в ГМК44
VGSig.fnDO_Processing(algOut := PAZ_GVL.DGO.Kl_ESDV9602_1_ON_v_GMK44.PV, fromHMI := PAZ_GVL.DGO.Kl_ESDV9602_1_ON_v_GMK44.FromHMI, toHMI := PAZ_GVL.DGO.Kl_ESDV9602_1_ON_v_GMK44.ToHMI, drv => PAZ_GVL.DGO.Kl_ESDV9602_1_ON_v_GMK44.DRV);
// [A1.16:4] Клапан ESDV9602.1 на выходе ГМК закрыт в ГМК44
VGSig.fnDO_Processing(algOut := PAZ_GVL.DGO.Kl_ESDV9602_1_OF_v_GMK44.PV, fromHMI := PAZ_GVL.DGO.Kl_ESDV9602_1_OF_v_GMK44.FromHMI, toHMI := PAZ_GVL.DGO.Kl_ESDV9602_1_OF_v_GMK44.ToHMI, drv => PAZ_GVL.DGO.Kl_ESDV9602_1_OF_v_GMK44.DRV);
// [A1.16:5] Клапан ESDV9611.1 на топливной линии открыт в ГМК44
VGSig.fnDO_Processing(algOut := PAZ_GVL.DGO.Kl_ESDV9611_1_ON_v_GMK44.PV, fromHMI := PAZ_GVL.DGO.Kl_ESDV9611_1_ON_v_GMK44.FromHMI, toHMI := PAZ_GVL.DGO.Kl_ESDV9611_1_ON_v_GMK44.ToHMI, drv => PAZ_GVL.DGO.Kl_ESDV9611_1_ON_v_GMK44.DRV);
// [A1.16:6] Клапан ESDV9611.1 на топливной линии закрыт в ГМК44
VGSig.fnDO_Processing(algOut := PAZ_GVL.DGO.Kl_ESDV9611_1_OF_v_GMK44.PV, fromHMI := PAZ_GVL.DGO.Kl_ESDV9611_1_OF_v_GMK44.FromHMI, toHMI := PAZ_GVL.DGO.Kl_ESDV9611_1_OF_v_GMK44.ToHMI, drv => PAZ_GVL.DGO.Kl_ESDV9611_1_OF_v_GMK44.DRV);
// [A1.16:7] Клапан ESDV9601.2 на приёме ГМК открыт в ГМК45
VGSig.fnDO_Processing(algOut := PAZ_GVL.DGO.Kl_ESDV9601_2_ON_v_GMK45.PV, fromHMI := PAZ_GVL.DGO.Kl_ESDV9601_2_ON_v_GMK45.FromHMI, toHMI := PAZ_GVL.DGO.Kl_ESDV9601_2_ON_v_GMK45.ToHMI, drv => PAZ_GVL.DGO.Kl_ESDV9601_2_ON_v_GMK45.DRV);
// [A1.16:8] Клапан ESDV9601.2 на приёме ГМК закрыт в ГМК45
VGSig.fnDO_Processing(algOut := PAZ_GVL.DGO.Kl_ESDV9601_2_OF_v_GMK45.PV, fromHMI := PAZ_GVL.DGO.Kl_ESDV9601_2_OF_v_GMK45.FromHMI, toHMI := PAZ_GVL.DGO.Kl_ESDV9601_2_OF_v_GMK45.ToHMI, drv => PAZ_GVL.DGO.Kl_ESDV9601_2_OF_v_GMK45.DRV);
// [A1.16:9] Клапан ESDV9602.2 на выходе ГМК открыт в ГМК45
VGSig.fnDO_Processing(algOut := PAZ_GVL.DGO.Kl_ESDV9602_2_ON_v_GMK45.PV, fromHMI := PAZ_GVL.DGO.Kl_ESDV9602_2_ON_v_GMK45.FromHMI, toHMI := PAZ_GVL.DGO.Kl_ESDV9602_2_ON_v_GMK45.ToHMI, drv => PAZ_GVL.DGO.Kl_ESDV9602_2_ON_v_GMK45.DRV);
// [A1.16:10] Клапан ESDV9602.2 на выходе ГМК закрыт в ГМК45
VGSig.fnDO_Processing(algOut := PAZ_GVL.DGO.Kl_ESDV9602_2_OF_v_GMK45.PV, fromHMI := PAZ_GVL.DGO.Kl_ESDV9602_2_OF_v_GMK45.FromHMI, toHMI := PAZ_GVL.DGO.Kl_ESDV9602_2_OF_v_GMK45.ToHMI, drv => PAZ_GVL.DGO.Kl_ESDV9602_2_OF_v_GMK45.DRV);
// [A1.16:11] Клапан ESDV9611.2 на топливной линии открыт в ГМК45
VGSig.fnDO_Processing(algOut := PAZ_GVL.DGO.Kl_ESDV9611_2_ON_v_GMK45.PV, fromHMI := PAZ_GVL.DGO.Kl_ESDV9611_2_ON_v_GMK45.FromHMI, toHMI := PAZ_GVL.DGO.Kl_ESDV9611_2_ON_v_GMK45.ToHMI, drv => PAZ_GVL.DGO.Kl_ESDV9611_2_ON_v_GMK45.DRV);
// [A1.16:12] Клапан ESDV9611.2 на топливной линии закрыт в ГМК45
VGSig.fnDO_Processing(algOut := PAZ_GVL.DGO.Kl_ESDV9611_2_OF_v_GMK45.PV, fromHMI := PAZ_GVL.DGO.Kl_ESDV9611_2_OF_v_GMK45.FromHMI, toHMI := PAZ_GVL.DGO.Kl_ESDV9611_2_OF_v_GMK45.ToHMI, drv => PAZ_GVL.DGO.Kl_ESDV9611_2_OF_v_GMK45.DRV);
// [A1.16:13] Клапан ESDV9601.3 на приёме ГМК открыт в ГМК46
VGSig.fnDO_Processing(algOut := PAZ_GVL.DGO.Kl_ESDV9601_3_ON_v_GMK46.PV, fromHMI := PAZ_GVL.DGO.Kl_ESDV9601_3_ON_v_GMK46.FromHMI, toHMI := PAZ_GVL.DGO.Kl_ESDV9601_3_ON_v_GMK46.ToHMI, drv => PAZ_GVL.DGO.Kl_ESDV9601_3_ON_v_GMK46.DRV);
// [A1.16:14] Клапан ESDV9601.3 на приёме ГМК закрыт в ГМК46
VGSig.fnDO_Processing(algOut := PAZ_GVL.DGO.Kl_ESDV9601_3_OF_v_GMK46.PV, fromHMI := PAZ_GVL.DGO.Kl_ESDV9601_3_OF_v_GMK46.FromHMI, toHMI := PAZ_GVL.DGO.Kl_ESDV9601_3_OF_v_GMK46.ToHMI, drv => PAZ_GVL.DGO.Kl_ESDV9601_3_OF_v_GMK46.DRV);
// [A1.16:15] Клапан ESDV9602.3 на выходе ГМК открыт в ГМК46
VGSig.fnDO_Processing(algOut := PAZ_GVL.DGO.Kl_ESDV9602_3_ON_v_GMK46.PV, fromHMI := PAZ_GVL.DGO.Kl_ESDV9602_3_ON_v_GMK46.FromHMI, toHMI := PAZ_GVL.DGO.Kl_ESDV9602_3_ON_v_GMK46.ToHMI, drv => PAZ_GVL.DGO.Kl_ESDV9602_3_ON_v_GMK46.DRV);
// [A1.16:16] Клапан ESDV9602.3 на выходе ГМК закрыт в ГМК46
VGSig.fnDO_Processing(algOut := PAZ_GVL.DGO.Kl_ESDV9602_3_OF_v_GMK46.PV, fromHMI := PAZ_GVL.DGO.Kl_ESDV9602_3_OF_v_GMK46.FromHMI, toHMI := PAZ_GVL.DGO.Kl_ESDV9602_3_OF_v_GMK46.ToHMI, drv => PAZ_GVL.DGO.Kl_ESDV9602_3_OF_v_GMK46.DRV);
// [A1.17:1] Клапан ESDV9611.3 на топливной линии открыт в ГМК46
VGSig.fnDO_Processing(algOut := PAZ_GVL.DGO.Kl_ESDV9611_3_ON_v_GMK46.PV, fromHMI := PAZ_GVL.DGO.Kl_ESDV9611_3_ON_v_GMK46.FromHMI, toHMI := PAZ_GVL.DGO.Kl_ESDV9611_3_ON_v_GMK46.ToHMI, drv => PAZ_GVL.DGO.Kl_ESDV9611_3_ON_v_GMK46.DRV);
// [A1.17:2] Клапан ESDV9611.3 на топливной линии закрыт в ГМК46
VGSig.fnDO_Processing(algOut := PAZ_GVL.DGO.Kl_ESDV9611_3_OF_v_GMK46.PV, fromHMI := PAZ_GVL.DGO.Kl_ESDV9611_3_OF_v_GMK46.FromHMI, toHMI := PAZ_GVL.DGO.Kl_ESDV9611_3_OF_v_GMK46.ToHMI, drv => PAZ_GVL.DGO.Kl_ESDV9611_3_OF_v_GMK46.DRV);
// [A1.17:3] Клапан ESDV9601.4 на приёме ГМК открыт в ГМК47
VGSig.fnDO_Processing(algOut := PAZ_GVL.DGO.Kl_ESDV9601_4_ON_v_GMK47.PV, fromHMI := PAZ_GVL.DGO.Kl_ESDV9601_4_ON_v_GMK47.FromHMI, toHMI := PAZ_GVL.DGO.Kl_ESDV9601_4_ON_v_GMK47.ToHMI, drv => PAZ_GVL.DGO.Kl_ESDV9601_4_ON_v_GMK47.DRV);
// [A1.17:4] Клапан ESDV9601.4 на приёме ГМК закрыт в ГМК47
VGSig.fnDO_Processing(algOut := PAZ_GVL.DGO.Kl_ESDV9601_4_OF_v_GMK47.PV, fromHMI := PAZ_GVL.DGO.Kl_ESDV9601_4_OF_v_GMK47.FromHMI, toHMI := PAZ_GVL.DGO.Kl_ESDV9601_4_OF_v_GMK47.ToHMI, drv => PAZ_GVL.DGO.Kl_ESDV9601_4_OF_v_GMK47.DRV);
// [A1.17:5] Клапан ESDV9602.4 на выходе ГМК открыт в ГМК47
VGSig.fnDO_Processing(algOut := PAZ_GVL.DGO.Kl_ESDV9602_4_ON_v_GMK47.PV, fromHMI := PAZ_GVL.DGO.Kl_ESDV9602_4_ON_v_GMK47.FromHMI, toHMI := PAZ_GVL.DGO.Kl_ESDV9602_4_ON_v_GMK47.ToHMI, drv => PAZ_GVL.DGO.Kl_ESDV9602_4_ON_v_GMK47.DRV);
// [A1.17:6] Клапан ESDV9602.4 на выходе ГМК закрыт в ГМК47
VGSig.fnDO_Processing(algOut := PAZ_GVL.DGO.Kl_ESDV9602_4_OF_v_GMK47.PV, fromHMI := PAZ_GVL.DGO.Kl_ESDV9602_4_OF_v_GMK47.FromHMI, toHMI := PAZ_GVL.DGO.Kl_ESDV9602_4_OF_v_GMK47.ToHMI, drv => PAZ_GVL.DGO.Kl_ESDV9602_4_OF_v_GMK47.DRV);
// [A1.17:7] Клапан ESDV9611.4 на топливной линии открыт в ГМК47
VGSig.fnDO_Processing(algOut := PAZ_GVL.DGO.Kl_ESDV9611_4_ON_v_GMK47.PV, fromHMI := PAZ_GVL.DGO.Kl_ESDV9611_4_ON_v_GMK47.FromHMI, toHMI := PAZ_GVL.DGO.Kl_ESDV9611_4_ON_v_GMK47.ToHMI, drv => PAZ_GVL.DGO.Kl_ESDV9611_4_ON_v_GMK47.DRV);
// [A1.17:8] Клапан ESDV9611.4 на топливной линии закрыт в ГМК47
VGSig.fnDO_Processing(algOut := PAZ_GVL.DGO.Kl_ESDV9611_4_OF_v_GMK47.PV, fromHMI := PAZ_GVL.DGO.Kl_ESDV9611_4_OF_v_GMK47.FromHMI, toHMI := PAZ_GVL.DGO.Kl_ESDV9611_4_OF_v_GMK47.ToHMI, drv => PAZ_GVL.DGO.Kl_ESDV9611_4_OF_v_GMK47.DRV);
// [A1.17:9] Клапан ESDV9601.5 на приёме ГМК открыт в ГМК48
VGSig.fnDO_Processing(algOut := PAZ_GVL.DGO.Kl_ESDV9601_5_ON_v_GMK48.PV, fromHMI := PAZ_GVL.DGO.Kl_ESDV9601_5_ON_v_GMK48.FromHMI, toHMI := PAZ_GVL.DGO.Kl_ESDV9601_5_ON_v_GMK48.ToHMI, drv => PAZ_GVL.DGO.Kl_ESDV9601_5_ON_v_GMK48.DRV);
// [A1.17:10] Клапан ESDV9601.5 на приёме ГМК закрыт в ГМК48
VGSig.fnDO_Processing(algOut := PAZ_GVL.DGO.Kl_ESDV9601_5_OF_v_GMK48.PV, fromHMI := PAZ_GVL.DGO.Kl_ESDV9601_5_OF_v_GMK48.FromHMI, toHMI := PAZ_GVL.DGO.Kl_ESDV9601_5_OF_v_GMK48.ToHMI, drv => PAZ_GVL.DGO.Kl_ESDV9601_5_OF_v_GMK48.DRV);
// [A1.17:11] Клапан ESDV9602.5 на выходе ГМК открыт в ГМК48
VGSig.fnDO_Processing(algOut := PAZ_GVL.DGO.Kl_ESDV9602_5_ON_v_GMK48.PV, fromHMI := PAZ_GVL.DGO.Kl_ESDV9602_5_ON_v_GMK48.FromHMI, toHMI := PAZ_GVL.DGO.Kl_ESDV9602_5_ON_v_GMK48.ToHMI, drv => PAZ_GVL.DGO.Kl_ESDV9602_5_ON_v_GMK48.DRV);
// [A1.17:12] Клапан ESDV9602.5 на выходе ГМК закрыт в ГМК48
VGSig.fnDO_Processing(algOut := PAZ_GVL.DGO.Kl_ESDV9602_5_OF_v_GMK48.PV, fromHMI := PAZ_GVL.DGO.Kl_ESDV9602_5_OF_v_GMK48.FromHMI, toHMI := PAZ_GVL.DGO.Kl_ESDV9602_5_OF_v_GMK48.ToHMI, drv => PAZ_GVL.DGO.Kl_ESDV9602_5_OF_v_GMK48.DRV);
// [A1.17:13] Клапан ESDV9611.5 на топливной линии открыт в ГМК48
VGSig.fnDO_Processing(algOut := PAZ_GVL.DGO.Kl_ESDV9611_5_ON_v_GMK48.PV, fromHMI := PAZ_GVL.DGO.Kl_ESDV9611_5_ON_v_GMK48.FromHMI, toHMI := PAZ_GVL.DGO.Kl_ESDV9611_5_ON_v_GMK48.ToHMI, drv => PAZ_GVL.DGO.Kl_ESDV9611_5_ON_v_GMK48.DRV);
// [A1.17:14] Клапан ESDV9611.5 на топливной линии закрыт в ГМК48
VGSig.fnDO_Processing(algOut := PAZ_GVL.DGO.Kl_ESDV9611_5_OF_v_GMK48.PV, fromHMI := PAZ_GVL.DGO.Kl_ESDV9611_5_OF_v_GMK48.FromHMI, toHMI := PAZ_GVL.DGO.Kl_ESDV9611_5_OF_v_GMK48.ToHMI, drv => PAZ_GVL.DGO.Kl_ESDV9611_5_OF_v_GMK48.DRV);
// [A1.17:15] Клапан ESDV9601.6 на приёме ГМК открыт в ГМК51
VGSig.fnDO_Processing(algOut := PAZ_GVL.DGO.Kl_ESDV9601_6_ON_v_GMK51.PV, fromHMI := PAZ_GVL.DGO.Kl_ESDV9601_6_ON_v_GMK51.FromHMI, toHMI := PAZ_GVL.DGO.Kl_ESDV9601_6_ON_v_GMK51.ToHMI, drv => PAZ_GVL.DGO.Kl_ESDV9601_6_ON_v_GMK51.DRV);
// [A1.17:16] Клапан ESDV9601.6 на приёме ГМК закрыт в ГМК51
VGSig.fnDO_Processing(algOut := PAZ_GVL.DGO.Kl_ESDV9601_6_OF_v_GMK51.PV, fromHMI := PAZ_GVL.DGO.Kl_ESDV9601_6_OF_v_GMK51.FromHMI, toHMI := PAZ_GVL.DGO.Kl_ESDV9601_6_OF_v_GMK51.ToHMI, drv => PAZ_GVL.DGO.Kl_ESDV9601_6_OF_v_GMK51.DRV);
// [A1.18:1] Клапан ESDV9602.6 на выходе ГМК открыт в ГМК51
VGSig.fnDO_Processing(algOut := PAZ_GVL.DGO.Kl_ESDV9602_6_ON_v_GMK51.PV, fromHMI := PAZ_GVL.DGO.Kl_ESDV9602_6_ON_v_GMK51.FromHMI, toHMI := PAZ_GVL.DGO.Kl_ESDV9602_6_ON_v_GMK51.ToHMI, drv => PAZ_GVL.DGO.Kl_ESDV9602_6_ON_v_GMK51.DRV);
// [A1.18:2] Клапан ESDV9602.6 на выходе ГМК закрыт в ГМК51
VGSig.fnDO_Processing(algOut := PAZ_GVL.DGO.Kl_ESDV9602_6_OF_v_GMK51.PV, fromHMI := PAZ_GVL.DGO.Kl_ESDV9602_6_OF_v_GMK51.FromHMI, toHMI := PAZ_GVL.DGO.Kl_ESDV9602_6_OF_v_GMK51.ToHMI, drv => PAZ_GVL.DGO.Kl_ESDV9602_6_OF_v_GMK51.DRV);
// [A1.18:3] Клапан ESDV9611.6 на топливной линии открыт в ГМК51
VGSig.fnDO_Processing(algOut := PAZ_GVL.DGO.Kl_ESDV9611_6_ON_v_GMK51.PV, fromHMI := PAZ_GVL.DGO.Kl_ESDV9611_6_ON_v_GMK51.FromHMI, toHMI := PAZ_GVL.DGO.Kl_ESDV9611_6_ON_v_GMK51.ToHMI, drv => PAZ_GVL.DGO.Kl_ESDV9611_6_ON_v_GMK51.DRV);
// [A1.18:4] Клапан ESDV9611.6 на топливной линии закрыт в ГМК51
VGSig.fnDO_Processing(algOut := PAZ_GVL.DGO.Kl_ESDV9611_6_OF_v_GMK51.PV, fromHMI := PAZ_GVL.DGO.Kl_ESDV9611_6_OF_v_GMK51.FromHMI, toHMI := PAZ_GVL.DGO.Kl_ESDV9611_6_OF_v_GMK51.ToHMI, drv => PAZ_GVL.DGO.Kl_ESDV9611_6_OF_v_GMK51.DRV);
// [A1.18:5] Клапан ESDV9601.7 на приёме ГМК открыт в ГМК51
VGSig.fnDO_Processing(algOut := PAZ_GVL.DGO.Kl_ESDV9601_7_ON_v_GMK51.PV, fromHMI := PAZ_GVL.DGO.Kl_ESDV9601_7_ON_v_GMK51.FromHMI, toHMI := PAZ_GVL.DGO.Kl_ESDV9601_7_ON_v_GMK51.ToHMI, drv => PAZ_GVL.DGO.Kl_ESDV9601_7_ON_v_GMK51.DRV);
// [A1.18:6] Клапан ESDV9601.7 на приёме ГМК закрыт в ГМК52
VGSig.fnDO_Processing(algOut := PAZ_GVL.DGO.Kl_ESDV9601_7_OF_v_GMK52.PV, fromHMI := PAZ_GVL.DGO.Kl_ESDV9601_7_OF_v_GMK52.FromHMI, toHMI := PAZ_GVL.DGO.Kl_ESDV9601_7_OF_v_GMK52.ToHMI, drv => PAZ_GVL.DGO.Kl_ESDV9601_7_OF_v_GMK52.DRV);
// [A1.18:7] Клапан ESDV9602.7 на выходе ГМК открыт в ГМК52
VGSig.fnDO_Processing(algOut := PAZ_GVL.DGO.Kl_ESDV9602_7_ON_v_GMK52.PV, fromHMI := PAZ_GVL.DGO.Kl_ESDV9602_7_ON_v_GMK52.FromHMI, toHMI := PAZ_GVL.DGO.Kl_ESDV9602_7_ON_v_GMK52.ToHMI, drv => PAZ_GVL.DGO.Kl_ESDV9602_7_ON_v_GMK52.DRV);
// [A1.18:8] Клапан ESDV9602.7 на выходе ГМК закрыт в ГМК52
VGSig.fnDO_Processing(algOut := PAZ_GVL.DGO.Kl_ESDV9602_7_OF_v_GMK52.PV, fromHMI := PAZ_GVL.DGO.Kl_ESDV9602_7_OF_v_GMK52.FromHMI, toHMI := PAZ_GVL.DGO.Kl_ESDV9602_7_OF_v_GMK52.ToHMI, drv => PAZ_GVL.DGO.Kl_ESDV9602_7_OF_v_GMK52.DRV);
// [A1.18:9] Клапан ESDV9611.7 на топливной линии открыт в ГМК52
VGSig.fnDO_Processing(algOut := PAZ_GVL.DGO.Kl_ESDV9611_7_ON_v_GMK52.PV, fromHMI := PAZ_GVL.DGO.Kl_ESDV9611_7_ON_v_GMK52.FromHMI, toHMI := PAZ_GVL.DGO.Kl_ESDV9611_7_ON_v_GMK52.ToHMI, drv => PAZ_GVL.DGO.Kl_ESDV9611_7_ON_v_GMK52.DRV);
// [A1.18:10] Клапан ESDV9611.7 на топливной линии закрыт в ГМК52
VGSig.fnDO_Processing(algOut := PAZ_GVL.DGO.Kl_ESDV9611_7_OF_v_GMK52.PV, fromHMI := PAZ_GVL.DGO.Kl_ESDV9611_7_OF_v_GMK52.FromHMI, toHMI := PAZ_GVL.DGO.Kl_ESDV9611_7_OF_v_GMK52.ToHMI, drv => PAZ_GVL.DGO.Kl_ESDV9611_7_OF_v_GMK52.DRV);
// [A1.19:1] Резерв
VGSig.fnDO_Processing(algOut := PAZ_GVL.DGO.Reserv_9.PV, fromHMI := PAZ_GVL.DGO.Reserv_9.FromHMI, toHMI := PAZ_GVL.DGO.Reserv_9.ToHMI, drv => PAZ_GVL.DGO.Reserv_9.DRV);
// [A1.19:2] Резерв
VGSig.fnDO_Processing(algOut := PAZ_GVL.DGO.Reserv_10.PV, fromHMI := PAZ_GVL.DGO.Reserv_10.FromHMI, toHMI := PAZ_GVL.DGO.Reserv_10.ToHMI, drv => PAZ_GVL.DGO.Reserv_10.DRV);
// [A1.19:3] Резерв
VGSig.fnDO_Processing(algOut := PAZ_GVL.DGO.Reserv_11.PV, fromHMI := PAZ_GVL.DGO.Reserv_11.FromHMI, toHMI := PAZ_GVL.DGO.Reserv_11.ToHMI, drv => PAZ_GVL.DGO.Reserv_11.DRV);
// [A1.19:4] Резерв
VGSig.fnDO_Processing(algOut := PAZ_GVL.DGO.Reserv_12.PV, fromHMI := PAZ_GVL.DGO.Reserv_12.FromHMI, toHMI := PAZ_GVL.DGO.Reserv_12.ToHMI, drv => PAZ_GVL.DGO.Reserv_12.DRV);
// [A1.19:5] Резерв
VGSig.fnDO_Processing(algOut := PAZ_GVL.DGO.Reserv_13.PV, fromHMI := PAZ_GVL.DGO.Reserv_13.FromHMI, toHMI := PAZ_GVL.DGO.Reserv_13.ToHMI, drv => PAZ_GVL.DGO.Reserv_13.DRV);
// [A1.19:6] Резерв
VGSig.fnDO_Processing(algOut := PAZ_GVL.DGO.Reserv_14.PV, fromHMI := PAZ_GVL.DGO.Reserv_14.FromHMI, toHMI := PAZ_GVL.DGO.Reserv_14.ToHMI, drv => PAZ_GVL.DGO.Reserv_14.DRV);
// [A1.19:7] Резерв
VGSig.fnDO_Processing(algOut := PAZ_GVL.DGO.Reserv_15.PV, fromHMI := PAZ_GVL.DGO.Reserv_15.FromHMI, toHMI := PAZ_GVL.DGO.Reserv_15.ToHMI, drv => PAZ_GVL.DGO.Reserv_15.DRV);
// [A1.19:8] Резерв
VGSig.fnDO_Processing(algOut := PAZ_GVL.DGO.Reserv_16.PV, fromHMI := PAZ_GVL.DGO.Reserv_16.FromHMI, toHMI := PAZ_GVL.DGO.Reserv_16.ToHMI, drv => PAZ_GVL.DGO.Reserv_16.DRV);
// [A1.19:9] Резерв
VGSig.fnDO_Processing(algOut := PAZ_GVL.DGO.Reserv_17.PV, fromHMI := PAZ_GVL.DGO.Reserv_17.FromHMI, toHMI := PAZ_GVL.DGO.Reserv_17.ToHMI, drv => PAZ_GVL.DGO.Reserv_17.DRV);
// [A1.19:10] Резерв
VGSig.fnDO_Processing(algOut := PAZ_GVL.DGO.Reserv_18.PV, fromHMI := PAZ_GVL.DGO.Reserv_18.FromHMI, toHMI := PAZ_GVL.DGO.Reserv_18.ToHMI, drv => PAZ_GVL.DGO.Reserv_18.DRV);
// [A1.19:11] Резерв
VGSig.fnDO_Processing(algOut := PAZ_GVL.DGO.Reserv_19.PV, fromHMI := PAZ_GVL.DGO.Reserv_19.FromHMI, toHMI := PAZ_GVL.DGO.Reserv_19.ToHMI, drv => PAZ_GVL.DGO.Reserv_19.DRV);
// [A1.19:12] Резерв
VGSig.fnDO_Processing(algOut := PAZ_GVL.DGO.Reserv_20.PV, fromHMI := PAZ_GVL.DGO.Reserv_20.FromHMI, toHMI := PAZ_GVL.DGO.Reserv_20.ToHMI, drv => PAZ_GVL.DGO.Reserv_20.DRV);
// [A1.19:13] Резерв
VGSig.fnDO_Processing(algOut := PAZ_GVL.DGO.Reserv_21.PV, fromHMI := PAZ_GVL.DGO.Reserv_21.FromHMI, toHMI := PAZ_GVL.DGO.Reserv_21.ToHMI, drv => PAZ_GVL.DGO.Reserv_21.DRV);
// [A1.19:14] Резерв
VGSig.fnDO_Processing(algOut := PAZ_GVL.DGO.Reserv_22.PV, fromHMI := PAZ_GVL.DGO.Reserv_22.FromHMI, toHMI := PAZ_GVL.DGO.Reserv_22.ToHMI, drv => PAZ_GVL.DGO.Reserv_22.DRV);
// [A1.19:15] Резерв
VGSig.fnDO_Processing(algOut := PAZ_GVL.DGO.Reserv_23.PV, fromHMI := PAZ_GVL.DGO.Reserv_23.FromHMI, toHMI := PAZ_GVL.DGO.Reserv_23.ToHMI, drv => PAZ_GVL.DGO.Reserv_23.DRV);
// [A1.19:16] Резерв
VGSig.fnDO_Processing(algOut := PAZ_GVL.DGO.Reserv_24.PV, fromHMI := PAZ_GVL.DGO.Reserv_24.FromHMI, toHMI := PAZ_GVL.DGO.Reserv_24.ToHMI, drv => PAZ_GVL.DGO.Reserv_24.DRV);
// [A1.20:1] Активность управляющего ПЛК А1 (А2)
VGSig.fnDO_Processing(algOut := PAZ_GVL.DGO.Aktiv_PLC_A1_A2.PV, fromHMI := PAZ_GVL.DGO.Aktiv_PLC_A1_A2.FromHMI, toHMI := PAZ_GVL.DGO.Aktiv_PLC_A1_A2.ToHMI, drv => PAZ_GVL.DGO.Aktiv_PLC_A1_A2.DRV);
// [A1.20:2] Звуковая сигнализация тон 1
VGSig.fnDO_Processing(algOut := PAZ_GVL.DGO.Snd_ton_1.PV, fromHMI := PAZ_GVL.DGO.Snd_ton_1.FromHMI, toHMI := PAZ_GVL.DGO.Snd_ton_1.ToHMI, drv => PAZ_GVL.DGO.Snd_ton_1.DRV);
// [A1.20:3] Звуковая сигнализация тон 2
VGSig.fnDO_Processing(algOut := PAZ_GVL.DGO.Snd_ton_2.PV, fromHMI := PAZ_GVL.DGO.Snd_ton_2.FromHMI, toHMI := PAZ_GVL.DGO.Snd_ton_2.ToHMI, drv => PAZ_GVL.DGO.Snd_ton_2.DRV);
// [A1.20:4] Световая сигнализация "Запуск ПАЗ ГМК №44"
VGSig.fnDO_Processing(algOut := PAZ_GVL.DGO.SvetSig_Pusk_PAZ_GMK_44_.PV, fromHMI := PAZ_GVL.DGO.SvetSig_Pusk_PAZ_GMK_44_.FromHMI, toHMI := PAZ_GVL.DGO.SvetSig_Pusk_PAZ_GMK_44_.ToHMI, drv => PAZ_GVL.DGO.SvetSig_Pusk_PAZ_GMK_44_.DRV);
// [A1.20:5] Световая сигнализация "Запуск ПАЗ ГМК №45"
VGSig.fnDO_Processing(algOut := PAZ_GVL.DGO.SvetSig_Pusk_PAZ_GMK_45_.PV, fromHMI := PAZ_GVL.DGO.SvetSig_Pusk_PAZ_GMK_45_.FromHMI, toHMI := PAZ_GVL.DGO.SvetSig_Pusk_PAZ_GMK_45_.ToHMI, drv => PAZ_GVL.DGO.SvetSig_Pusk_PAZ_GMK_45_.DRV);
// [A1.20:6] Световая сигнализация "Запуск ПАЗ ГМК №46"
VGSig.fnDO_Processing(algOut := PAZ_GVL.DGO.SvetSig_Pusk_PAZ_GMK_46_.PV, fromHMI := PAZ_GVL.DGO.SvetSig_Pusk_PAZ_GMK_46_.FromHMI, toHMI := PAZ_GVL.DGO.SvetSig_Pusk_PAZ_GMK_46_.ToHMI, drv => PAZ_GVL.DGO.SvetSig_Pusk_PAZ_GMK_46_.DRV);
// [A1.20:7] Световая сигнализация "Запуск ПАЗ ГМК №47"
VGSig.fnDO_Processing(algOut := PAZ_GVL.DGO.SvetSig_Pusk_PAZ_GMK_47_.PV, fromHMI := PAZ_GVL.DGO.SvetSig_Pusk_PAZ_GMK_47_.FromHMI, toHMI := PAZ_GVL.DGO.SvetSig_Pusk_PAZ_GMK_47_.ToHMI, drv => PAZ_GVL.DGO.SvetSig_Pusk_PAZ_GMK_47_.DRV);
// [A1.20:8] Световая сигнализация "Запуск ПАЗ ГМК №48"
VGSig.fnDO_Processing(algOut := PAZ_GVL.DGO.SvetSig_Pusk_PAZ_GMK_48_.PV, fromHMI := PAZ_GVL.DGO.SvetSig_Pusk_PAZ_GMK_48_.FromHMI, toHMI := PAZ_GVL.DGO.SvetSig_Pusk_PAZ_GMK_48_.ToHMI, drv => PAZ_GVL.DGO.SvetSig_Pusk_PAZ_GMK_48_.DRV);
// [A1.20:9] Световая сигнализация "Запуск ПАЗ ГМК №51"
VGSig.fnDO_Processing(algOut := PAZ_GVL.DGO.SvetSig_Pusk_PAZ_GMK_51_.PV, fromHMI := PAZ_GVL.DGO.SvetSig_Pusk_PAZ_GMK_51_.FromHMI, toHMI := PAZ_GVL.DGO.SvetSig_Pusk_PAZ_GMK_51_.ToHMI, drv => PAZ_GVL.DGO.SvetSig_Pusk_PAZ_GMK_51_.DRV);
// [A1.20:10] Световая сигнализация "Запуск ПАЗ ГМК №52"
VGSig.fnDO_Processing(algOut := PAZ_GVL.DGO.SvetSig_Pusk_PAZ_GMK_52_.PV, fromHMI := PAZ_GVL.DGO.SvetSig_Pusk_PAZ_GMK_52_.FromHMI, toHMI := PAZ_GVL.DGO.SvetSig_Pusk_PAZ_GMK_52_.ToHMI, drv => PAZ_GVL.DGO.SvetSig_Pusk_PAZ_GMK_52_.DRV);
"""
proj = projects.primary
folder = proj.find('DO PAZ', recursive=True)[0]
struktur = folder.create_pou('PAZ_DO_Call', type = PouType.Function,language=None, return_type='BOOL', base_type=None, interfaces=None)
struktur.textual_declaration.insert(4, 0, CONTENT_var)
struktur.textual_implementation.insert(0, 0, CONTENT_body)
