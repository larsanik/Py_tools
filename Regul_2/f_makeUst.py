def f_makeUst(ai_name, ust_comment, ust_dir, ust_copy, ust_init):
    if ust_dir == '+':
        dir = '_vu'+ust_copy
        init_ust = 'TRUE'
    elif ust_dir == '-':
        dir = '_nu'+ust_copy
        init_ust = 'FALSE'
    else:
        print('Ошибка в коде направления уставки')
        sys.exit() 

    print(ai_name+dir, ': BOOL; //' + ust_comment)
    print('')
    print(ai_name+dir, ': REAL; //' + ust_comment)
    print('')
    print(ai_name+dir, ': VGALG.strANB_Settings; //' + ust_comment)
    print('')
    print('    algGVL.GPA_Ust.'+ai_name+dir+' := '+ust_init+'; //'+ust_comment)
    print('')
    print('    algGVL.GPA_ANB_Settings.'+ai_name+dir+' := VGALG.fnANB_init('+init_ust+', 0, 0); //'+ust_comment)
    print('')
    print('//'+ust_comment)
    print('algGVL.GPA_ANB.'+ai_name+dir+' := VGALG.fnANB_Processing(algGVL.GPA_ANB_Settings.'+ai_name+dir+',algGVL.GPA_AI_ToHMI.'+ai_name+'.PV,algGVL.GPA_AI_ToHMI.'+ai_name+'.fault_common,algGVL.GPA_Ust.'+ai_name+dir+', algGVL.GPA_ANB_Internal.'+ai_name+dir+');')