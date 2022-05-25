Tv_KShT_nu_VodMinF : BOOL; //Темп. воздуха под КШТ Д, ВОД минимальные обороты

Tv_KShT_nu_VodMinF : REAL; //Темп. воздуха под КШТ Д, ВОД минимальные обороты

Tv_KShT_nu_VodMinF : VGALG.strANB_Settings; //Темп. воздуха под КШТ Д, ВОД минимальные обороты

    algGVL.GPA_Ust.Tv_KShT_nu_VodMinF := 65.0; //Темп. воздуха под КШТ Д, ВОД минимальные обороты

    algGVL.GPA_ANB_Settings.Tv_KShT_nu_VodMinF := VGALG.fnANB_init(FALSE, 0, 0); //Темп. воздуха под КШТ Д, ВОД минимальные обороты

//Темп. воздуха под КШТ Д, ВОД минимальные обороты
algGVL.GPA_ANB.Tv_KShT_nu_VodMinF := VGALG.fnANB_Processing(algGVL.GPA_ANB_Settings.Tv_KShT_nu_VodMinF,algGVL.GPA_AI_ToHMI.Tv_KShT.PV,algGVL.GPA_AI_ToHMI.Tv_KShT.fault_common,algGVL.GPA_Ust.Tv_KShT_nu_VodMinF, algGVL.GPA_ANB_Internal.Tv_KShT_nu_VodMinF);
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
Tv_KShT_vu_VodMaxF : BOOL; //Темп. воздуха под КШТ Д, ВОД максимальные обороты

Tv_KShT_vu_VodMaxF : REAL; //Темп. воздуха под КШТ Д, ВОД максимальные обороты

Tv_KShT_vu_VodMaxF : VGALG.strANB_Settings; //Темп. воздуха под КШТ Д, ВОД максимальные обороты

    algGVL.GPA_Ust.Tv_KShT_vu_VodMaxF := 75,0; //Темп. воздуха под КШТ Д, ВОД максимальные обороты

    algGVL.GPA_ANB_Settings.Tv_KShT_vu_VodMaxF := VGALG.fnANB_init(TRUE, 0, 0); //Темп. воздуха под КШТ Д, ВОД максимальные обороты

//Темп. воздуха под КШТ Д, ВОД максимальные обороты
algGVL.GPA_ANB.Tv_KShT_vu_VodMaxF := VGALG.fnANB_Processing(algGVL.GPA_ANB_Settings.Tv_KShT_vu_VodMaxF,algGVL.GPA_AI_ToHMI.Tv_KShT.PV,algGVL.GPA_AI_ToHMI.Tv_KShT.fault_common,algGVL.GPA_Ust.Tv_KShT_vu_VodMaxF, algGVL.GPA_ANB_Internal.Tv_KShT_vu_VodMaxF);
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
Tv_KShT_vu_VodPID_UpSc : BOOL; //Темп. воздуха под КШТ Д, работает ПИД регулятор

Tv_KShT_vu_VodPID_UpSc : REAL; //Темп. воздуха под КШТ Д, работает ПИД регулятор

Tv_KShT_vu_VodPID_UpSc : VGALG.strANB_Settings; //Темп. воздуха под КШТ Д, работает ПИД регулятор

    algGVL.GPA_Ust.Tv_KShT_vu_VodPID_UpSc := 65.0; //Темп. воздуха под КШТ Д, работает ПИД регулятор

    algGVL.GPA_ANB_Settings.Tv_KShT_vu_VodPID_UpSc := VGALG.fnANB_init(TRUE, 0, 0); //Темп. воздуха под КШТ Д, работает ПИД регулятор

//Темп. воздуха под КШТ Д, работает ПИД регулятор
algGVL.GPA_ANB.Tv_KShT_vu_VodPID_UpSc := VGALG.fnANB_Processing(algGVL.GPA_ANB_Settings.Tv_KShT_vu_VodPID_UpSc,algGVL.GPA_AI_ToHMI.Tv_KShT.PV,algGVL.GPA_AI_ToHMI.Tv_KShT.fault_common,algGVL.GPA_Ust.Tv_KShT_vu_VodPID_UpSc, algGVL.GPA_ANB_Internal.Tv_KShT_vu_VodPID_UpSc);
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
Tv_KShT_nu_VodPID_DownSc : BOOL; //Темп. воздуха под КШТ Д, работает ПИД регулятор

Tv_KShT_nu_VodPID_DownSc : REAL; //Темп. воздуха под КШТ Д, работает ПИД регулятор

Tv_KShT_nu_VodPID_DownSc : VGALG.strANB_Settings; //Темп. воздуха под КШТ Д, работает ПИД регулятор

    algGVL.GPA_Ust.Tv_KShT_nu_VodPID_DownSc := 75.0; //Темп. воздуха под КШТ Д, работает ПИД регулятор

    algGVL.GPA_ANB_Settings.Tv_KShT_nu_VodPID_DownSc := VGALG.fnANB_init(FALSE, 0, 0); //Темп. воздуха под КШТ Д, работает ПИД регулятор

//Темп. воздуха под КШТ Д, работает ПИД регулятор
algGVL.GPA_ANB.Tv_KShT_nu_VodPID_DownSc := VGALG.fnANB_Processing(algGVL.GPA_ANB_Settings.Tv_KShT_nu_VodPID_DownSc,algGVL.GPA_AI_ToHMI.Tv_KShT.PV,algGVL.GPA_AI_ToHMI.Tv_KShT.fault_common,algGVL.GPA_Ust.Tv_KShT_nu_VodPID_DownSc, algGVL.GPA_ANB_Internal.Tv_KShT_nu_VodPID_DownSc);
