#Получаем данные о АПС из файла с параметрами
def getDataXls(f_name, sigName, minPS, maxPS, minAS, maxAS):
    import pandas as pd
    df = pd.read_excel(io=f_name, engine ='openpyxl')#открытие файла
    headsList = [sigName, minPS, maxPS, minAS, maxAS]
    sample = df[headsList]#чтение столбцов с нужной инфой (пока требуется модификация файла xlsx, чтобы заголовки были в первой строке)
    n = len(sample)#количество строк со значениями
    apsList = [headsList]#закинем в шапку заголовки для порядку
    for i in range(n):
        param = sample.iloc[i]
        if str(param[sigName]) != 'nan': #если в наименованиее ничего нет табаним
            if str(param[minPS]) != 'nan' or str(param[maxPS]) != 'nan' or str(param[minAS]) != 'nan' or str(param[maxAS]) != 'nan':# если все поля пустые табаним
                apsList.append(param.values.tolist())# Собираем все в список
    return apsList



if __name__ == '__main__':
    #получаем список с именами и значениями уставок
    #apsList = getDataXls('lp_v15.xlsx','Наименование сигнала', 'ПС min', 'ПС max', 'АС min', 'АС max')
    #print(apsList)
    # формируем алгоритмические имена

    '''import translit_ru_to_eng as tr
    for i in range(len(apsList)):
        apsList[i].append(tr.transliterate(apsList[i][0]))
        #print(tr.transliterate(apsList[i][0]))
        print(apsList[i])'''
    import translit_ru_to_eng as tr
    import IO_AI
    import IO_DI
    import IO_DO

    for i in range(len(IO_AI.AI_Struct)):
        apsList[i].append(tr.transliterate(apsList[i][0]))
        # print(tr.transliterate(apsList[i][0]))
        print(apsList[i])
        '''
