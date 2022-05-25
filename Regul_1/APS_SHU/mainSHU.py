#транслятор в латиницу
def transliterate(name):
    # Слоаврь с заменами слов на обозначения
    w_dictionary = {
        '~': 'AC',
        '=': 'DC',
        '«НАГРЕВ»': 'heat',
        '«НОРМА»': 'norm',
        '«ОХЛАЖДЕНИЕ»': 'cool',
        'Bently': 'B',
        'CO': 'CO',
        'cтопорн': 'SK',
        'Nevada': 'N',
        'аварийн': 'A',
        'Аварийн': 'A',
        'Аварийно-выс': 'HHi',
        'Аварийно-выс': 'HHi',
        'Аварийно-низ': 'LLo',
        'Аварийно-низ': 'LLo',
        'Авария': 'A',
        'авария': 'A',
        'АВО': 'AVO',
        'АВОМ': 'AVOM',
        'АВОМД': 'AVOMD',
        'АВОМК': 'AVOMK',
        'АВР': 'AVR',
        'Автомат': 'CB',
        'автомат': 'CB',
        'Агрегат': 'Agr',
        'агрегат': 'Agr',
        'аккумуляторн': 'Akkm',
        'Аккумуляторн': 'Akkm',
        'алюминиев': 'al',
        'Алюминиев': 'al',
        'аналоговых': 'AI',
        'Аналоговых': 'AI',
        'АО': 'AO',
        'АО1': 'AO1',
        'АО2': 'AO2',
        'АО3': 'AO3',
        'АО4': 'AO4',
        'АО5': 'AO5',
        'АПК': 'APK',
        'Аппарат': 'Apar',
        'аппарат': 'Apar',
        'АС': 'AS',
        'АСПС': 'ASPT',
        'АСПТ': 'ASPT',
        'АСПТ:': 'ASPT',
        'Байпас': 'Bp',
        'байпас': 'Bp',
        'Барометрическое': 'Patm',
        'барометрическое': 'Patm',
        'барьерн': 'bf',
        'БД': 'BD',
        'БЗА': 'BZA',
        'БК': 'N',
        'блок-бокс': 'BB',
        'Блок-бокс': 'BB',
        'Блокир': 'lock',
        'блокир': 'lock',
        'буферн': 'br',
        'БУШД': 'TRK',
        'быстр': 'Bystr',
        'Быстр': 'Bystr',
        'БЭАО': 'BEO',
        'БЭО': 'BEO',
        'БЭТ': 'OET',
        'Ввод': 'Vvod',
        'вентиля': 'Vent',
        'Вентиля': 'Vent',
        'вертикальная': 'x',
        'Вибрац': 'Vb',
        'вибрац': 'Vb',
        'Виброперемещ': 'Vb',
        'виброперемещ': 'Vb',
        'вкладыш': 'vkl',
        'Вкладыш': 'vkl',
        'вклю': 'ON',
        'Вклю': 'ON',
        'влагомер': 'Vlagom',
        'Влагомер': 'Vlagom',
        'влажн': 'Vlag',
        'Влажн': 'Vlag',
        'ВНА': 'VNA',
        'внешнего': 'vnesh',
        'Внешнего': 'vnesh',
        'внешних': 'vne',
        'Внешних': 'vne',
        'внутреннего': 'vnytr',
        'Внутреннего': 'vnytr',
        'внутренних': 'vnytr',
        'Внутренних': 'vnytr',
        'возвратном': 'Vozv',
        'Возвратном': 'Vozv',
        'возд': 'vzd',
        'ВОУ': 'VOU',
        'Вращ': 'vrash',
        'вращ': 'vrash',
        'всас': 'vsas',
        'Всас': 'vsas',
        'Вторичн': 'vtor',
        'вторичн': 'vtor',
        'Вход': 'in',
        'вход': 'in',
        'выкл': 'OF',
        'Выкл': 'OF',
        'Выс': 'Hi',
        'выс': 'Hi',
        'Высок': 'Hi',
        'высок': 'Hi',
        'вытяжной': 'Vyt',
        'Вытяжной': 'Vyt',
        'выхлопных': 'vg',
        'выход': 'out',
        'газ': 'g',
        'газ-газ': 'gg',
        'газоанализат': 'Gas_sens',
        'Газоанализат': 'Gas_sens',
        'Газогенератор': 'GG',
        'газогенератор': 'GG',
        'газоход': 'GH',
        'Газоход': 'GH',
        'ГГ': 'GG',
        'горизонтальная': 'y',
        'готов': 'ready',
        'Готов': 'ready',
        'ГПА': 'GPA',
        'греющ': 'heat',
        'грубой': 'grub',
        'Групп': 'Gr',
        'групп': 'Gr',
        'ГТД': 'GTD',
        'давл': 'P',
        'Давл': 'P',
        'Двер': 'Dr',
        'двер': 'Dr',
        'ДГ': 'TRK',
        'диафрагм': 'diaf',
        'Диафрагм': 'diaf',
        'дискретных': 'DI',
        'Дискретных': 'DI',
        'дозатор': 'TRK',
        'дренажный': 'Dren',
        'Дренажный': 'Dren',
        'жалюз': 'Zal',
        'Жалюз': 'Zal',
        'Загазован': 'Gas',
        'загазован': 'Gas',
        'Зажиган': 'Zazh',
        'зажиган': 'Zazh',
        'заземлени': 'Zazem',
        'Заземлени': 'Zazem',
        'открыть / закрыть': 'ON',
        'открыть/закрыть': 'ON',
        'открыть/ закрыть': 'ON',
        'открыть /закрыть': 'ON',
        'закрыть / открыть': 'OF',
        'закрыть/открыть': 'OF',
        'закрыть/ открыть': 'OF',
        'закрыть /открыть': 'OF',
        'Закр': 'OF',
        'закр': 'OF',
        'замкнут': 'ON',
        'Замкнут': 'ON',
        'Заслонк': 'Zs',
        'заслонк': 'Zs',
        'Зацеплен': 'Zac',
        'зацеплен': 'Zac',
        'Защит': 'Zash',
        'защит': 'Zash',
        'Защитной': 'zash',
        'защитной': 'zash',
        'ЗЗО': 'ZZO',
        'ЗОН': 'ZON',
        'ЗПВ': 'ZPV',
        'ЗУ': 'ZU',
        'ИМ': 'IM',
        'импульс': 'Imp',
        'Импульс': 'Imp',
        'Инвертора': 'inv',
        'инвертора': 'inv',
        'инструментальн': 'instr',
        'используется': 'used',
        'исправен': 'Ispr',
        'Исправен': 'Ispr',
        'исправно': 'Ispr',
        'Исправно': 'Ispr',
        'кабел': 'cab',
        'Кабел': 'cab',
        'калорифер': 'Klrf',
        'Калорифер': 'Klrf',
        'Камер': 'kam',
        'камер': 'kam',
        'канал': 'Ch',
        'каналов': 'Ch',
        'КВД': 'KVD',
        'квитирова': 'Ack',
        'Квитирова': 'Ack',
        'КВОУ': 'VOU',
        'КИП': 'KIP',
        'Клапан': 'Kl',
        'клапан': 'Kl',
        'клеммных': 'klem',
        'Кн': 'Btn',
        'кн': 'Btn',
        'кожух': 'Kg',
        'Кожух': 'Kg',
        'количеств': 'Kol',
        'Количеств': 'Kol',
        'компрессор': 'N',
        'конденсат': 'cond',
        'Кондиционер': 'Cool',
        'кондиционер': 'Cool',
        'Конец': 'Finish',
        'конец': 'Finish',
        'Контрол': 'Check',
        'контрол': 'Check',
        'контроллер': 'PLC',
        'Контроллер': 'PLC',
        'конфузор': 'Konf',
        'Конфузор': 'Konf',
        'корпус': 'corp',
        'кПа': 'kPa',
        'КПБВ': 'KPBV',
        'КПВ': 'KPV',
        'КПВ1': 'KPV1',
        'КПВ10': 'KPV10',
        'КПВ2': 'KPV2',
        'КПВ3': 'KPV3',
        'КПВ4': 'KPV4',
        'КПВ5': 'KPV5',
        'КПВ6': 'KPV6',
        'КПВ7': 'KPV7',
        'КПВ8': 'KPV8',
        'КПВ9': 'KPV9',
        'Кран': 'Kr',
        'кран': 'Kr',
        'КС': 'KC',
        'КЦ': 'KC',
        'КЦД': 'KCD',
        'КЦП': 'KCP',
        'КЦУ': 'KCU',
        'КШТ': 'KHST',
        'максимал': 'max',
        'масл': 'm',
        'маслобак': 'MB',
        'маслофильтре': 'f',
        'МБ': 'MB',
        'МБД': 'MBD',
        'МБК': 'MBN',
        'МБН': 'MBN',
        'Между': 'mez',
        'между': 'mez',
        'менее': 'min',
        'минимал': 'min',
        'Момент': 'M',
        'момент': 'M',
        'МСКУ': 'SAU',
        'Муфт': 'Muf',
        'муфт': 'Muf',
        'нагнетания': 'nagn',
        'нагнетател': 'N',
        'нагрев': 'heat',
        'Нагреват': 'TEN',
        'нагреват': 'TEN',
        'нажат': 'ON',
        'Нажат': 'ON',
        'Наличие': 'Nal',
        'наличие': 'Nal',
        'напряжен': 'U',
        'Напряжен': 'U',
        'Наруж': 'nar',
        'наруж': 'nar',
        'Насос': 'Pump',
        'насос': 'Pump',
        'неисправ': 'Fault',
        'Неисправ': 'Fault',
        'Нет': 'not',
        'нет': 'not',
        'Низ': 'Lo',
        'низ': 'Lo',
        'низк': 'Lo',
        'НКПВ': 'NKPV',
        'НО': 'NO',
        'норм': 'norm',
        'НСП': 'NSP',
        'НСЦ': 'NSC',
        'Оборот': 'Obor',
        'оборот': 'Obor',
        'оборудование': 'obor',
        'Оборудование': 'obor',
        'общая': 'Obsh',
        'Общая': 'Obsh',
        'ОГК': 'OGK',
        'ОК': 'OK',
        'ОП': 'OP',
        'операторн': 'Oper',
        'Операторн': 'Oper',
        'опорн': 'op',
        'ОПТ': 'OPT',
        'Освещение': 'Light',
        'освещение': 'Light',
        'Осев': 'Osev',
        'осев': 'Osev',
        'Основн': 'Osn',
        'основн': 'Osn',
        'Останов': 'O',
        'останов': 'O',
        'осушител': 'Osush',
        'Осушител': 'Osush',
        'осушк': 'Osush',
        'Осушк': 'Osush',
        'откачки': 'Otk',
        'Откачки': 'Otk',
        'откл': 'OF',
        'Откл': 'OF',
        'Откр': 'ON',
        'откр': 'ON',
        'отсекател': 'Damper',
        'Отсекател': 'Damper',
        'отсечка': 'Ots',
        'отсечки': 'Ots',
        'отсечной': 'Ots',
        'Отсечной': 'Ots',
        'отсоса': 'Ots',
        'Отсоса': 'Ots',
        'отсутсвие': 'not',
        'Отсутствие': 'not',
        'охлажд': 'Ohl',
        'Охлажд': 'Ohl',
        'ОЭТ': 'OET',
        'ПАЗ': 'PAZ',
        'ПДК': 'PDK',
        'Первичн': 'perv',
        'первичн': 'perv',
        'Перегрев': 'maxT',
        'перегрев': 'maxT',
        'перед': 'do',
        'Перепад': 'd',
        'перепад': 'd',
        'Питан': 'U',
        'питан': 'U',
        'пламя': 'Flame',
        'Пламя': 'Flame',
        'ПЛК': 'PLC',
        'повышен': 'Hi',
        'Повышен': 'Hi',
        'Поглотител': 'pgl',
        'поглотител': 'pgl',
        'подач': 'Pod',
        'Подач': 'Pod',
        'подогрев': 'Podgr',
        'Подогрев': 'Podgr',
        'подшип': 'p',
        'Пожар': 'Fire',
        'пожар': 'Fire',
        'Положение': 'Pos',
        'положение': 'Pos',
        'ПОН': 'PON',
        'понижен': 'Lo',
        'порог': 'lim',
        'ПОС': 'POS',
        'предел': 'lim',
        'предупр': 'Pr',
        'Предупр': 'Pr',
        'Приборного': 'prib',
        'приборного': 'prib',
        'привод': 'Priv',
        'Привод': 'Priv',
        'приточный': 'Prit',
        'Приточный': 'Prit',
        'пробное': 'Prob',
        'Пробное': 'Prob',
        'прокачкa': 'Proc',
        'прокачки': 'Proc',
        'промывк': 'Wash',
        'Промывк': 'Wash',
        'противопожарн': 'PP',
        'ПРУ': 'PRU',
        'ПС': 'PS',
        'пуск': 'Pusk',
        'Пуск': 'Pusk',
        'работ': 'Work',
        'Работ': 'Work',
        'рабоч': 'Work',
        'Рабоч': 'Work',
        'радиал': 'rd',
        'Радиал': 'rd',
        'Разр': 'Razr',
        'разр': 'Razr',
        'Разруш': 'Fault',
        'разруш': 'Fault',
        'распределител': 'Rasp',
        'Распределител': 'Rasp',
        'Расход': 'Q',
        'расход': 'Q',
        'Резерв': 'Reserv',
        'резерв': 'Reserv',
        'Решетке': 'resh',
        'решетке': 'resh',
        'Розетка': 'Roz',
        'розетка': 'Roz',
        'Ротор': 'Rot',
        'ротор': 'Rot',
        'РУ': 'RU',
        'РЧТиН': 'RChTN',
        'САУ': 'SAU',
        'Сверхвысокие': 'UpHi',
        'сверхвысокие': 'UpHi',
        'свечной': 'Sv',
        'Свечной': 'Sv',
        'Сгоран': 'sgor',
        'сгоран': 'sgor',
        'СГУ': 'SGU',
        'СДО': 'SDO',
        'Сигнализация': 'Sig',
        'сигнализация': 'Sig',
        'Силово': 'Pws',
        'силово': 'Pws',
        'Систем': 'Syst',
        'систем': 'Syst',
        'СК': 'SK',
        'смазк': 'sm',
        'Смазк': 'sm',
        'Соплов': 'sopl',
        'соплов': 'sopl',
        'СПВ': 'SPV',
        'срабат': 'trip',
        'Срабатыван': 'Act',
        'срабатыван': 'Act',
        'Сработ': 'trip',
        'СТ': 'ST',
        'Стартер': 'Starter',
        'стартер': 'Starter',
        'Стопорн': 'SK',
        'сторожевого': 'BEO',
        'стравливан': 'Str',
        'Стравливан': 'Str',
        'Стружка': 'Chips',
        'стружка': 'Chips',
        'счетчик': 'Sch',
        'Счетчик': 'Sch',
        'Таймер': 'Tmr',
        'таймер': 'Tmr',
        'ТВД': 'TVD',
        'темпер': 'T',
        'Темпер': 'T',
        'Термостат': 'TEN',
        'термостат': 'TEN',
        'ТК': 'TK',
        'ТО': 'TO',
        'ток': 'I',
        'Ток': 'I',
        'тонкой': 'tonk',
        'Тонкой': 'tonk',
        'топливн': 't',
        'Топливн': 't',
        'Точка': 'pt',
        'точка': 'pt',
        'трансмис': 'Tr',
        'Трансмис': 'Tr',
        'Тревога': 'trev',
        'тревога': 'trev',
        'ТРК': 'TRK',
        'ТРК': 'TRK',
        'Турбины': 'Turb',
        'турбины': 'Turb',
        'ТЭН': 'TEN',
        'Укрыт': 'Ukr',
        'укрыт': 'Ukr',
        'уплотнения': 'upl',
        'Уплотнения': 'upl',
        'упорн': 'up',
        'Упорн': 'up',
        'управл': 'Reg',
        'Управл': 'Reg',
        'Уровен': 'L',
        'уровен': 'L',
        'устройств': 'Ustr',
        'Устройств': 'Ustr',
        'Фильтр': 'Filt',
        'фильтр': 'Filt',
        'фильтре': 'f',
        'форсунок': 'fors',
        'Форсунок': 'fors',
        'ФС': 'FS',
        'центр': 'cntr',
        'цилин': 'Cyl',
        'Цилин': 'Cyl',
        'Частот': 'F',
        'частот': 'F',
        'ШАРМ': 'SHARM',
        'шкаф': 'SHK',
        'ЩУД': 'SHUD',
        'ЩУК': 'SHUK',
        'ЭАО': 'EAO',
        'эквивалент': 'Ekv',
        'Эквивалент': 'Ekv',
        'Электронагреват': 'TEN',
        'электронагреват': 'TEN',
        'ЭО': 'EAO',
        'ЭС': 'ES'
    }


    # Слоаврь с транслитерацией остатков
    dictionary = {
        'а': 'a',
        'б': 'b',
        'в': 'v',
        'г': 'g',
        'д': 'd',
        'е': 'e',
        'ё': 'e',
        'ж': 'zh',
        'з': 'z',
        'и': 'i',
        'й': 'i',
        'к': 'k',
        'л': 'l',
        'м': 'm',
        'н': 'n',
        'о': 'o',
        'п': 'p',
        'р': 'r',
        'с': 's',
        'т': 't',
        'у': 'u',
        'ф': 'f',
        'х': 'h',
        'ц': 'c',
        'ч': 'cz',
        'ш': 'sh',
        'щ': 'scz',
        'ъ': '',
        'ы': 'y',
        'ь': '',
        'э': 'e',
        'ю': 'u',
        'я': 'ja',
        'А': 'A',
        'Б': 'B',
        'В': 'V',
        'Г': 'G',
        'Д': 'D',
        'Е': 'E',
        'Ё': 'E',
        'Ж': 'ZH',
        'З': 'Z',
        'И': 'I',
        'Й': 'I',
        'К': 'K',
        'Л': 'L',
        'М': 'M',
        'Н': 'N',
        'О': 'O',
        'П': 'P',
        'Р': 'R',
        'С': 'S',
        'Т': 'T',
        'У': 'U',
        'Ф': 'F',
        'Х': 'H',
        'Ц': 'C',
        'Ч': 'CZ',
        'Ш': 'SH',
        'Щ': 'SCH',
        'Ъ': '',
        'Ы': 'y',
        'Ь': 'b',
        'Э': 'E',
        'Ю': 'U',
        'Я': 'YA',
        ',': '_',
        '.': '_',
        '?': '_',
        ' ': '_',
        '~': '_',
        '!': '_',
        '@': '_',
        '#': '_',
        '$': '_',
        '%': '_',
        '^': '_',
        '&': '_',
        '*': '_',
        '(': '_',
        ')': '_',
        '-': '_',
        '=': '_',
        '+': '_',
        ':': '_',
        ';': '_',
        '<': 'Lo',
        '>': 'Hi',
        '\'': '_',
        '"': '_',
        '\\': '_',
        '/': '_',
        '№': '',
        '[': '_',
        ']': '_',
        '{': '_',
        '}': '_',
        'ґ': 'r',
        'ї': 'r',
        'є': 'e',
        'Ґ': 'g',
        'Ї': 'i',
        'Є': 'e',
        '—': '_'
    }

    # Слоаврь с исключениями
    exc_dictionary = {
        'T_g': 'Tg',
        'P_g': 'Pg',
        'T_m': 'Tm',
        'P_m': 'Pm',
        'T_vzd': 'Tvzd',
        'P_vzd': 'Pvzd',
        'T_p': 'Tp',
        'P_t_g': 'Ptg',
        'd_P': 'dP',
        'T_br_g': 'Tbrg',
        'T_br_vzd': 'Tbrvzd',
        'P_b_g': 'Pbg',
        'P_b_vzd': 'Pbvzd',
        'T_vg': 'Tvg',
        'P_vg': 'Pvg',
        'T_bf_g': 'Tbfg',
        'T_bf_vzd': 'Tbfvzd',
        'T_vkl': 'Tvkl',
        'dPmez': 'dP_mez',
        'S_T': 'ST',
        'A_O': 'AO',
        '__': '_',
        '___': '_',
        '____': '_',
        '_____': '_',
        '______': '_',
        'CB_OF': 'CB',
        'Rot_O': 'RotStop',
        'VNAON': 'VNA_ON',
        'GPAON': 'GPA_ON',
        'not_AO': 'NotAO',
        '_B_N': '_BN',
        'T_silovogo_cilindra': 'Tsc',
        'T_korennogo_p_№': 'Tkp',
        'Tvg_g_v_levom_kollektore': 'Tvg_lk',
        'Tvg_g_v_pravom_kollektore': 'Tvg_pk',
        'T_vody_na_in_v_dvigatel': 'Tv_inD',
        'T_vody_na_out_iz_dvigatelja': 'Tv_outD',
        'Tvzd_nadduva': 'Tvn',
        'Tm_na_in_v_gmk': 'Tm_inGMK',
        'Tm_na_out_iz_gmk': 'Tm_outGMK',
        'Tg_na_out_N_cilindra': 'Tg_outKC',
        'U_Osn_U_AC_v': 'U_Osn_AC',
        'U_Reserv_U_AC_v': 'U_Res_AC',
        'Pg_na_in_v_gmk': 'Pg_inGMK',
        'Pg_na_out_iz_gmk': 'Pg_outGMK',
        'Ptg_do_TRK': 'Ptg_inTRK',
        'P_Pusk_vzd': 'Ppv',
        'Ptg_posle_TRK': 'Ptg_outTRK',
        'Pvzd_nadduva': 'Pvn',
        'Pm_na_in_v_N': 'Pm_inTK',
        'Pm_na_in_v_dvigatel': 'Pm_inD',
        'dPm_na_Filt': 'dPmf',
        'P_vody_na_out_iz_dvigatelja': 'Pv_outD',
        'L_Vb_gmk_vybroskorost_Ch': 'Vb_Ch',
        'Kl_ESDXV96011_na_prijome_gmk': 'Kr1',
        'Kl_ESDXV96021_na_out_gmk': 'Kr2',
        'Kl_ESDXV96051_na_peremychke': 'Kr5',
        'Kl_ESDXV96131_na_sbrose_prijomnojj_linii': 'Kr13',
        'Kl_ESDXV96061_na_sbrose_N_linii': 'Kr6',
        'Kl_ESDXV96111_na_t_linii': 'Kr11',
        'trehhodovojj_Kl_ESDXV96101_na_t_linii': 'Kr10',
        'Kl_Pusk_vzd_XV96081': 'Kr8',
        'Kl_ESDXV96061_na_sbrose_prijomnojj_linii': 'Kr6',
        'Pusk_Pump_Proc_m': 'Pmp_ppm',
        'sirena_na_Dr': 'Snd',
        'svetovaja_indikator_na_Dr': 'SvetInd',
        'svetovaja_indikacija_Btn_na_Dr': 'SvetInd_Btn',
        'Ispr_PLC_signal_v_buz': 'Meandr',
        'Pump_Proc_m': 'Pmp_ppm',
        'Pmp_ppm_v_CB_Reg': 'Pmp_ppm_AU',
        'ON_Zazh': 'Zazh_ON',
        'Zazh_v_Work': 'Zazh_ON',
        'Check_Osn_pit_shu_gmk_AC_v': 'U_Osn_AC_ON',
        'Check_Reserv_pit_shu_gmk_AC_v': 'U_Res_AC_ON',
        'Check_Ispr_razr': 'RazrGood',
        'CB_U_ON': 'AvtPwr_ON',
        'Dr_shu_gmk_ON': 'DoorOpen',
        'Ispr_osn_ip_DC_v_vnutr_cepejj': 'Ispr_Osn_DC_inC',
        'Ispr_rez_ip_DC_v_vnutr_cepejj': 'Ispr_Res_DC_inC',
        'Ispr_osn_ip_DC_v_AI': 'Ispr_Osn_DC_AI',
        'Ispr_rez_ip_DC_v_AI': 'Ispr_Res_DC_AI',
        'Ispr_osn_ip_DC_v_DI_vnesh': 'Ispr_Osn_DC_DI',
        'Ispr_rez_ip_DC_v_DI_vnesh': 'Ispr_Res_DC_DI',
        'Ispr_osn_ip_DC_v_DO_vnesh': 'Ispr_Osn_DC_DO',
        'Ispr_rez_ip_DC_v_DO_vnesh': 'Ispr_Res_DC_DO',
        'Check_vnesh_U_AC_v_ot_shu_gmk': 'U_AC_outC_ON',
        'Btn_na_Dr_AO': 'Btn_AO',
        'Btn_na_Dr_normalnyjj_O': 'Btn_NO',
        'Btn_na_Dr_lock': 'Btn_Deblock',
        'L_Vb_GMK_vibroskorost': 'Vb',
        '_korennogo_p': 'kp',
        '_Pws_Cyl': 'sc',
        'na_in_v_GMK': 'inGMK',
        'na_out_iz_GMK': 'outGMK',
        'na_out_N_Cyl': 'outKC',
        'Reg_zaporno_reguliruusczim_Kl_na_prieme_GMK_PV4601_1_KC':'RegKr1_KCU',
        'U_Osn_U_AC_V':'U_Osn_AC',
        'U_Reserv_U_AC_V':'U_Res_AC',
        'Pos_TRK_PV9604_1':'Pos_TRK',
        'Pos_zaporno_reguliruusczego_Kl_na_prieme_GMK_PV4601_1':'Pos_RegKr1',
        'Vb__':'Vb_',
        'Reg_zaporno_reguliruusczim_Kl_na_prieme_GMK_PV4601_1':'Set_RegKr1',
        'Kl_ESDV9601_1_na_prieme_GMK':'Kr1',
        'Kl_ESDV9602_1_na_out_GMK':'Kr2',
        'Kl_XV9605_1_na_peremyczke':'Kr5',
        'Kl_XV9613_1_na_sbrose_priemnoi_linii':'Kr13',
        'Trehhodovoi_Kl_XV9610_1_na_t_linii':'Kr10',
        'Kl_Pusk_vzd_XV9608_1':'Kr8',
        'Kl_ESDV9611_1_na_t_linii':'Kr11',
        'Check_Osn_pit_SHU_GMK_AC_V':'U_Osn_AC_ON',
        'Check_Reserv_pit_SHU_GMK_AC_V':'U_Res_AC_ON',
        'Check_Ispr_Razr':'RazrGood',
        'Dr_SHU_GMK_ON':'DoorOpen',
        'Ispr_osn_IP_DC_V_vnutr_cepei':'Ispr_Osn_DC_inC',
        'Ispr_rez_IP_DC_V_vnutr_cepei':'Ispr_Res_DC_inC',
        'Ispr_osn_IP_DC_V_AI':'Ispr_Osn_DC_AI',
        'Ispr_rez_IP_DC_V_AI':'Ispr_Res_DC_AI',
        'Ispr_osn_IP_DC_V_DI_vnesh_':'Ispr_Osn_DC_DI',
        'Ispr_rez_IP_DC_V_DI_vnesh_':'Ispr_Res_DC_DI',
        'Ispr_osn_IP_DC_V_DO_vnesh_':'Ispr_Osn_DC_DO',
        'Ispr_rez_IP_DC_V_DO_vnesh_':'Ispr_Res_DC_DO',
        'Btn_na_Dr_Normalnyi_O':'Btn_NO',
        'Check_vnesh_U_AC_V_ot_SHU_GMK':'U_AC_outC_ON',
        'Sirena_na_Dr_PS':'Snd_PS',
        'Sirena_na_Dr_AS':'Snd_AS',
        'Svetovaja_indikator_na_Dr_PS':'SvetInd_PS',
        'Svetovaja_indikator_na_Dr_AS':'SvetInd_AS',
        'Svetovaja_indikacija_Btn_AO':'SvetInd_Btn_AO',
        'Svetovaja_indikacija_Btn_na_Dr_NO':'SvetInd_Btn_NO',
        'Ispr_Check_LSU':'Meandr'
    }

    # Циклически заменяем все найденые подстроки в строке
    for key in w_dictionary:

        sep_str = name.split()
        for s in sep_str:
            if key in s:
                sep_str[sep_str.index(s)] = w_dictionary[key]
        name = ' '.join(sep_str)

    # Циклически заменяем все буквы и символы в строке на латиницу и знаки подчеркивания
    for key in dictionary:
        name = name.replace(key, dictionary[key])

    # Циклически заменяем все буквы и символы в строке на латиницу и знаки подчеркивания
    for key in exc_dictionary:
        name = name.replace(key, exc_dictionary[key])

    return name


#Отсеивание пустых строк и формирование алгоритмических имен
def validDataMakeAlgName(df):
    #import translit_ru_to_eng as tr #транслятор в латиницу
    out_list = [] #сюда будем складывать данные на выход
    n = 0 # счетчик для резервов
    for i in range(len(df)): #бежим по строкам датафрейма
        param = df.iloc[i] #строчка фрейма
        if str(param[0]) != 'nan' and str(param[1]) != 'nan': #если в канале или в наименовании пусто, то игнорим строку
            AlgName = transliterate(str(param[1])) #делаем из наименования сигнала алгоритмическое имя
            s = param.values.tolist() #преобразуем строчку датафрейма в список
            if AlgName == 'Reserv': # если резерв, то приклеиваем к алгоритмическому имени номер
                AlgName = 'Reserv_' + str(n)
                n += 1 # счетчик резервов
            s.insert(0, AlgName) #добавляем алгоритмическре имя в начало списка
            out_list.append(s) #добавляем в список на выход
    return out_list

#Получаем данные из IO листа
def getDataXls(f_name):
    import pandas as pd
    #df = pd.read_excel(io=f_name, header= None, engine='openpyxl')  # открытие файла xlsx
    df_ai = pd.read_excel(io=f_name, sheet_name = 'AI1', header= 2, usecols = "E,F,G,H,I,J")#открытие файла xls лист AI1
    df_ao = pd.read_excel(io=f_name, sheet_name = 'AO1', header= 2, usecols = "E,F,G,H,I,J,K,L")  # открытие файла xls лист AO1
    df_di = pd.read_excel(io=f_name, sheet_name = 'DI1', header= 2, usecols = "E,F,G")  # открытие файла xls лист DI1
    df_do = pd.read_excel(io=f_name, sheet_name = 'DO1', header= 2, usecols = "E,F,G")  # открытие файла xls лист DO1
    df_fi = pd.read_excel(io=f_name, sheet_name = 'FI1', header= 2, usecols = "E,F,G,H,I,J")  # открытие файла xls лист FI1
    ai = validDataMakeAlgName(df_ai) #Отсеивание пустых строк и формирование алгоритмических имен AI
    ao = validDataMakeAlgName(df_ao) #Отсеивание пустых строк и формирование алгоритмических имен AO
    di = validDataMakeAlgName(df_di) #Отсеивание пустых строк и формирование алгоритмических имен DI
    do = validDataMakeAlgName(df_do) #Отсеивание пустых строк и формирование алгоритмических имен DO
    fi = validDataMakeAlgName(df_fi) #Отсеивание пустых строк и формирование алгоритмических имен FI
    return ai,ao,di,do,fi

#создание скрипта с параметрами для запуска в Epsilon
def MakeStrustContent(list, name, ab):
    f_w = open(f'CreationStructs_{name}.py', 'w', encoding='UTF8')
    f_w.write('#encoding:utf-8' + '\n')
    f_w.write('from __future__ import print_function' + '\n')
    f_w.write(f'STRUCT_CONTENT_{name} = """\\' + '\n')
    for i in range(len(list)):
        out = '	' + list[i][0] + f':str_{name};' + ' //['+ list[i][1] + '] ' + list[i][2] + '\n'
        f_w.write(out)
    f_w.write('"""' + '\n')
    f_w.write('proj = projects.primary' + '\n')
    f_w.write(f"folder = proj.find('Parameter lists {ab}', recursive=True)[0]" + '\n')
    f_w.write(f"struktur = folder.create_dut('{ab}_list_{name}')  # DutType.Structure is the default" + '\n')
    f_w.write(f'struktur.textual_declaration.insert(2, 0, STRUCT_CONTENT_{name})' + '\n')
    f_w.close

# создание скриптов обработчика AI
def MakeCallAI(list, name, ab):
    f_w = open(f'MakeCall_{name}.py', 'w', encoding='UTF8')
    f_w.write('#encoding:utf-8' + '\n')
    f_w.write('from __future__ import print_function' + '\n')
    f_w.write('CONTENT_var = """\\' + '\n')
    f_w.write(' repTime: INT;' + '\n')
    f_w.write('"""' + '\n')
    f_w.write('CONTENT_body = """\\' + '\n')
    f_w.write('repTime := 3600; // время ремонта аналоговых входов' + '\n')
    f_w.write('//================ Инициализация настроек аналоговых входов(вызывается один раз при старте) ================' + '\n')
    f_w.write(f'IF NOT {ab}_GVL.init THEN' + '\n')
    f_w.write('//------------------------------- аргументы функции инициализации --------------------------------' + '\n')
    f_w.write('// 1                                минимум шкалы канала, ед.изм. Не может быть >= max' + '\n')
    f_w.write('// 2                                |   максимум шкалы канала, ед.изм. Не может быть <= min' + '\n')
    f_w.write('// 3                                |   |   значение АЦП, соответствующее минимуму шкалы канала, б.р.' + '\n')
    f_w.write('// 4                                |   |   |   значение АЦП, соотв. макс. шкалы, б.р. Не может быть равно minADC' + '\n')
    f_w.write('// 5                                |   |   |   |     уровень зашкала вниз, ед.изм. Не может быть >= hiLim и < min' + '\n')
    f_w.write('// 6                                |   |   |   |     |    уровень зашкала вверх, ед.изм. Не может быть <= loLim и > max' + '\n')
    f_w.write('// 7                                |   |   |   |     |    |   уровень обрыва вниз, ед.изм. Не может быть >= loLim' + '\n')
    f_w.write('// 8                                |   |   |   |     |    |    |   уровень обрыва вверх, ед.изм. Не может быть <= hiLim' + '\n')
    f_w.write('// 9                                |   |   |   |     |    |    |   |  макс. допустимая скорость роста, ед.изм./сек. Если «0» - скорость роста не анализируется' + '\n')
    f_w.write('//10                                |   |   |   |     |    |    |   |   |   время восстановления после неисправности, сек. Не может быть меньше "0"' + '\n')
    f_w.write('//11                                |   |   |   |     |    |    |   |   |   |   максимальное время в ремонте, сек. Не может быть меньше или равно «0»' + '\n')
    f_w.write('//12                                |   |   |   |     |    |    |   |   |   |   |    тау фильтра, сек. Если «0» - фильтрация отсутствует' + '\n')
    f_w.write('//13                                |   |   |   |     |    |    |   |   |   |   |    |  номер по порядку	' + '\n')
    f_w.write('//AI_init(UPG_AI_Settings.Pg_in_UPG,0.0,6.0,2.0,10.0,-0.5,6.5,-1.0,7.0,0.0,1.0,3600,1.0,0);' + '\n')
    f_w.write('//-------------------------------------------------------------------------------------------' + '\n')
    for i in range(len(list)):
        f_w.write('	// [' + list[i][1] + ']' + list[i][2] + '\n')
        min_PV_s = str(list[i][3])
        max_PV_s = str(list[i][4])
        min_PV_s = min_PV_s.replace(',', '.')
        max_PV_s = max_PV_s.replace(',', '.')
        f_min_PV = float(min_PV_s)
        f_max_PV = float(max_PV_s)
        min_PV = str(f_min_PV)
        max_PV = str(f_max_PV)
        minADC = '4.0'
        maxADC = '20.0'
        span = f_max_PV - f_min_PV
        loLim = str(f_min_PV - span * 0.03)
        hiLim = str(f_max_PV + span * 0.03)
        loBrk = str(f_min_PV - span * 0.06)
        hiBrk = str(f_max_PV + span * 0.06)
        Name = list[i][0]
        f_w.write(f'	VGSig.fnAI_init(setStruct => {ab}_GVL.AI.' + Name + '.Settings, min_PV := ' + min_PV + ', max_PV := ' + max_PV + ', minADC := ' + minADC + ', maxADC := ' + maxADC + ', loLim := ' + loLim + ', hiLim := ' + hiLim + ', loBrk := ' + loBrk + ', hiBrk := ' + hiBrk + ', maxROC := 0.0, recoveryTime := 5.0, repairTime := repTime, tau := 1.0, id := 1, corrADC := 0.0);' + '\n')
    f_w.write('END_IF;' + '\n')
    f_w.write('\n')
    f_w.write('//================ Обработчик аналоговых входов================' + '\n')
    for i in range(len(list)):
        f_w.write('// [' + list[i][1] + '] ' +  list[i][2] + '\n')
        Name = list[i][0]
        f_w.write(f'VGSig.fnAI_Processing(IN := {ab}_GVL.AI.' + Name + f'.DRV, set := {ab}_GVL.AI.' + Name + f'.Settings, btn := {ab}_GVL.AI.' + Name + f'.FromHMI, out := {ab}_GVL.AI.' + Name + f'.ToHMI, my := {ab}_GVL.AI.' + Name + f'.Intern, nOk := {ab}_GVL.AI_FLT);' + '\n')

    f_w.write('"""' + '\n')
    f_w.write('proj = projects.primary' + '\n')
    f_w.write(f"folder = proj.find('{name} {ab}', recursive=True)[0]" + '\n')
    f_w.write(f"struktur = folder.create_pou('{ab}_{name}_Call', type = PouType.Function,language=None, return_type='BOOL', base_type=None, interfaces=None)" + '\n')
    f_w.write('struktur.textual_declaration.insert(4, 0, CONTENT_var)' + '\n')
    f_w.write('struktur.textual_implementation.insert(0, 0, CONTENT_body)' + '\n')
    f_w.close

# создание скриптов обработчика AO
def MakeCallAO(list, name, ab):
    f_w = open(f'MakeCall_{name}.py', 'w', encoding='UTF8')
    f_w.write('#encoding:utf-8' + '\n')
    f_w.write('from __future__ import print_function' + '\n')
    f_w.write('CONTENT_var = """\\' + '\n')
    f_w.write(' repTime: INT;' + '\n')
    f_w.write('"""' + '\n')
    f_w.write('CONTENT_body = """\\' + '\n')
    f_w.write('repTime := 3600; // время ремонта аналоговых входов' + '\n')
    f_w.write('//================ Инициализация настроек аналоговых выходов(вызывается один раз при старте) ================' + '\n')
    f_w.write(f'IF NOT {ab}_GVL.init THEN' + '\n')
    f_w.write('//------------------------------- аргументы функции инициализации --------------------------------' + '\n')
    f_w.write('//                                  минимум шкалы канала, ед.изм. Не может быть >= max' + '\n')
    f_w.write('//                                 |   максимум шкалы канала, ед.изм. Не может быть <= min' + '\n')
    f_w.write('//                                 |   |   значение АЦП, соответствующее минимуму шкалы канала, б.р.' + '\n')
    f_w.write('//                                 |   |   |   значение АЦП, соотв. макс. шкалы, б.р. Не может быть равно minADC' + '\n')
    f_w.write('//                                 |   |   |   |' + '\n')
    f_w.write('//                                 |   |   |   |   номер по порядку' + '\n')
    f_w.write('//AO_init(UPG_AO_Settings.Pg_in_UPG,0.0,6.0,2.0,10.0,0);' + '\n')
    f_w.write('//-------------------------------------------------------------------------------------------' + '\n')
    for i in range(len(list)):
        f_w.write('	// [' + list[i][1] + ']' + list[i][2] + '\n')
        min_PV_s = str(list[i][3])
        max_PV_s = str(list[i][4])
        min_PV_s = min_PV_s.replace(',', '.')
        max_PV_s = max_PV_s.replace(',', '.')
        f_min_PV = int(float(min_PV_s))
        f_max_PV = int(float(max_PV_s))
        min_PV = str(f_min_PV)
        max_PV = str(f_max_PV)
        minDAC_s = str(list[i][6])
        maxDAC_s = str(list[i][7])
        minDAC_s = minDAC_s.replace(',', '.')
        maxDAC_s = maxDAC_s.replace(',', '.')
        f_minDAC = int(float(minDAC_s))
        f_maxDAC = int(float(maxDAC_s))
        minDAC = str(f_minDAC)
        maxDAC = str(f_maxDAC)
        Name = list[i][0]
        f_w.write(f'	VGSig.fnAO_init(setStruct => {ab}_GVL.AO.' + Name + '.Settings, min_PV := ' + min_PV + ', max_PV := ' + max_PV + ', minDAC := ' + minDAC + ', maxDAC := ' + maxDAC +  ', id := ' + str(i+1) + ');' + '\n')
    f_w.write('END_IF;' + '\n')
    f_w.write('\n')
    f_w.write('//================ Обработчик аналоговых входов================' + '\n')
    for i in range(len(list)):
        f_w.write('// [' + list[i][1] + '] ' +  list[i][2] + '\n')
        Name = list[i][0]
        f_w.write(f'VGSig.fnAO_Processing(IN := {ab}_GVL.AO.' + Name + f'.ToHMI.PV, set := {ab}_GVL.AO.' + Name + f'.Settings, hmi := {ab}_GVL.AO.' + Name + f'.FromHMI, plc := {ab}_GVL.AO.' + Name + f'.ToHMI, out => {ab}_GVL.AO.' + Name + f'.DRV);' + '\n')
    f_w.write('"""' + '\n')
    f_w.write('proj = projects.primary' + '\n')
    f_w.write(f"folder = proj.find('{name} {ab}', recursive=True)[0]" + '\n')
    f_w.write(f"struktur = folder.create_pou('{ab}_{name}_Call', type = PouType.Function,language=None, return_type='BOOL', base_type=None, interfaces=None)" + '\n')
    f_w.write('struktur.textual_declaration.insert(4, 0, CONTENT_var)' + '\n')
    f_w.write('struktur.textual_implementation.insert(0, 0, CONTENT_body)' + '\n')
    f_w.close

# создание скриптов обработчика DI
def MakeCallDI(list, name, ab):
    f_w = open(f'MakeCall_{name}.py', 'w', encoding='UTF8')
    f_w.write('#encoding:utf-8' + '\n')
    f_w.write('from __future__ import print_function' + '\n')
    f_w.write('CONTENT_var = """\\' + '\n')
    f_w.write(' repTime: INT;' + '\n')
    f_w.write('"""' + '\n')
    f_w.write('CONTENT_body = """\\' + '\n')
    f_w.write('repTime := 3600; // время ремонта дискретных входов' + '\n')
    f_w.write('//================ Инициализация настроек дискретных входов(вызывается один раз при старте) ================' + '\n')
    f_w.write(f'IF NOT {ab}_GVL.init THEN' + '\n')
    f_w.write('//------------------------------- аргументы функции инициализации --------------------------------' + '\n')
    f_w.write('//                             максимальное время в ремонте, сек. Не может быть меньше или равно «0»' + '\n')
    f_w.write('//                                |       задержка от дребезга' + '\n')
    f_w.write('//                               |       |    признак инверсии' + '\n')
    f_w.write('//                               |       |    |   номер по порядку' + '\n')
    f_w.write('//DI_init(GPA_DI_Settings.BK_OF,repTime,0.0,false,0);' + '\n')
    f_w.write('//-------------------------------------------------------------------------------------------' + '\n')
    for i in range(len(list)):
        f_w.write('	// [' + list[i][1] + ']' + list[i][2] + '\n')
        Name = list[i][0]
        f_w.write(f'VGSig.fnDI_init(setStruct => {ab}_GVL.DGI.' + Name + '.Settings, repairTime := repTime, del := 0.0, inv := FALSE, id := ' + str(i + 1) + ');' + '\n')

    f_w.write('END_IF;' + '\n')
    f_w.write('\n')
    f_w.write('//================ Обработчик дискретных входов================' + '\n')
    for i in range(len(list)):
        f_w.write('// [' + list[i][1] + '] ' +  list[i][2] + '\n')
        Name = list[i][0]
        f_w.write(f'VGSig.fnDI_Processing(IN := {ab}_GVL.DGI.' + Name + f'.DRV, externalFault := FALSE, set := {ab}_GVL.DGI.' + Name + f'.Settings, FromHMI := {ab}_GVL.DGI.' + Name + f'.FromHMI, ToHMI := {ab}_GVL.DGI.' + Name + f'.ToHMI, my := {ab}_GVL.DGI.' + Name + f'.Intern, out := {ab}_GVL.DGI.' + Name + '.PV);' + '\n')

    f_w.write('"""' + '\n')
    f_w.write('proj = projects.primary' + '\n')
    f_w.write(f"folder = proj.find('{name} {ab}', recursive=True)[0]" + '\n')
    f_w.write(f"struktur = folder.create_pou('{ab}_{name}_Call', type = PouType.Function,language=None, return_type='BOOL', base_type=None, interfaces=None)" + '\n')
    f_w.write('struktur.textual_declaration.insert(4, 0, CONTENT_var)' + '\n')
    f_w.write('struktur.textual_implementation.insert(0, 0, CONTENT_body)' + '\n')
    f_w.close

# создание скриптов обработчика DO
def MakeCallDO(list, name, ab):
    f_w = open(f'MakeCall_{name}.py', 'w', encoding='UTF8')
    f_w.write('#encoding:utf-8' + '\n')
    f_w.write('from __future__ import print_function' + '\n')
    f_w.write('CONTENT_var = """\\' + '\n')
    f_w.write('"""' + '\n')
    f_w.write('CONTENT_body = """\\' + '\n')
    f_w.write('//================ Обработчик дискретных выходов================' + '\n')
    for i in range(len(list)):
        f_w.write('// [' + list[i][1] + '] ' +  list[i][2] + '\n')
        Name = list[i][0]
        f_w.write(f'VGSig.fnDO_Processing(algOut := {ab}_GVL.DGO.' + Name + f'.PV, fromHMI := {ab}_GVL.DGO.' + Name + f'.FromHMI, toHMI := {ab}_GVL.DGO.' + Name + f'.ToHMI, drv => {ab}_GVL.DGO.' + Name + '.DRV);' + '\n')
    f_w.write('"""' + '\n')
    f_w.write('proj = projects.primary' + '\n')
    f_w.write(f"folder = proj.find('{name} {ab}', recursive=True)[0]" + '\n')
    f_w.write(f"struktur = folder.create_pou('{ab}_{name}_Call', type = PouType.Function,language=None, return_type='BOOL', base_type=None, interfaces=None)" + '\n')
    f_w.write('struktur.textual_declaration.insert(4, 0, CONTENT_var)' + '\n')
    f_w.write('struktur.textual_implementation.insert(0, 0, CONTENT_body)' + '\n')
    f_w.close

# создание скриптов привязки логики к HW для входных параметров
def MakeBindInput(list, name, ab):
    f_w = open(f'MakeBind_{name}.py', 'w', encoding='UTF8')
    f_w.write('#encoding:utf-8' + '\n')
    f_w.write('from __future__ import print_function' + '\n')
    f_w.write('CONTENT_var = """\\' + '\n')
    f_w.write('"""' + '\n')
    f_w.write('CONTENT_body = """\\' + '\n')
    f_w.write('//================ Привязка входов к HW ================' + '\n')
    for i in list:
        leftPart = f'{ab}_GVL.{name}.{i[0]}.DRV'
        rp = i[1].replace('.','_')
        rp = rp.replace(':', '.in_ch')
        if name == 'DGI':
            strt = (rp.find('ch'))
            chnl = int(rp[strt+2:])
            rp = rp.replace('ch'+str(chnl),'ch.'+str(chnl-1))
        rightPart = f'{ab}_GVL.{rp}'
        comment = i[2]
        if name != 'AI' and name != 'DGI':
            print("Ошибка в наименовании группы параметров! Ожидалось 'AI' или DGI")
            return "Ошибка в наименовании группы параметров! Ожидалось 'AI' или DGI"
        f_w.write((f'{leftPart} := {rightPart}; //{comment}') + '\n')
    f_w.write('"""' + '\n')
    f_w.write('proj = projects.primary' + '\n')
    if name == 'DGI':
        name_i = 'DI'
    else:
        name_i = name
    f_w.write(f"folder = proj.find('{name_i} {ab}', recursive=True)[0]" + '\n')
    f_w.write(f"struktur = folder.create_pou('{ab}_{name_i}_binding_Hw_to_Lg', type = PouType.Function,language=None, return_type='BOOL', base_type=None, interfaces=None)" + '\n')
    f_w.write('struktur.textual_declaration.insert(4, 0, CONTENT_var)' + '\n')
    f_w.write('struktur.textual_implementation.insert(0, 0, CONTENT_body)' + '\n')
    f_w.close

# создание скриптов привязки логики к HW для вЫходных параметров
def MakeBindOutput(list, name, ab):
    f_w = open(f'MakeBind_{name}.py', 'w', encoding='UTF8')
    f_w.write('#encoding:utf-8' + '\n')
    f_w.write('from __future__ import print_function' + '\n')
    f_w.write('CONTENT_var = """\\' + '\n')
    f_w.write('"""' + '\n')
    f_w.write('CONTENT_body = """\\' + '\n')
    f_w.write('//================ Привязка вЫходов к HW ================' + '\n')
    for i in list:
        rightPart = f'{ab}_GVL.{name}.{i[0]}.DRV'
        rp = i[1].replace('.','_')
        rp = rp.replace(':', '.out_ch')
        if name == 'DGO':
            strt = (rp.find('ch'))
            chnl = int(rp[strt+2:])
            rp = rp.replace('ch'+str(chnl),'ch.'+str(chnl-1))
        leftPart = f'{ab}_GVL.{rp}'
        comment = i[2]
        if name != 'AO' and name != 'DGO':
            print("Ошибка в наименовании группы параметров! Ожидалось 'AO' или DGO")
            return "Ошибка в наименовании группы параметров! Ожидалось 'AO' или DGO"
        f_w.write((f'{leftPart} := {rightPart}; //{comment}') + '\n')
    f_w.write('"""' + '\n')
    f_w.write('proj = projects.primary' + '\n')
    if name == 'DGO':
        name_i = 'DO'
    else:
        name_i = name
    f_w.write(f"folder = proj.find('{name_i} {ab}', recursive=True)[0]" + '\n')
    f_w.write(f"struktur = folder.create_pou('{ab}_{name_i}_binding_Lg_to_Hw', type = PouType.Function,language=None, return_type='BOOL', base_type=None, interfaces=None)" + '\n')
    f_w.write('struktur.textual_declaration.insert(4, 0, CONTENT_var)' + '\n')
    f_w.write('struktur.textual_implementation.insert(0, 0, CONTENT_body)' + '\n')
    f_w.close


if __name__ == '__main__':

    #имя файла с IO листом
    io_list = 'IO_Миннибаевский ГПЗ_ШУ_v3_20211026.xls'

    #получаем списки из IO листа
    list_AI,list_AO,list_DI,list_DO,list_FI = getDataXls(io_list)

    #создание скриптов добавления структур параметров для запуска в Epsilon
    MakeStrustContent(list=list_AI, name='AI',ab='SHU')
    MakeStrustContent(list=list_AO, name='AO',ab='SHU')
    MakeStrustContent(list=list_DI, name='DI',ab='SHU')
    MakeStrustContent(list=list_DO, name='DO',ab='SHU')
    MakeStrustContent(list=list_FI, name='FI',ab='SHU')

    #создание скриптов добавления обработчиков параметров для запуска в Epsilon
    MakeCallAI(list=list_AI,name='AI',ab='SHU')
    MakeCallAO(list=list_AO,name='AO',ab='SHU')
    MakeCallDI(list=list_DI,name='DI',ab='SHU')
    MakeCallDO(list=list_DO, name='DO',ab='SHU')

    # создание скриптов привязки логики к HW для запуска в Epsilon
    MakeBindInput(list=list_AI, name='AI', ab='SHU')
    MakeBindOutput(list=list_AO, name='AO', ab='SHU')
    MakeBindInput(list=list_DI, name='DGI', ab='SHU')
    MakeBindOutput(list=list_DO, name='DGO', ab='SHU')
