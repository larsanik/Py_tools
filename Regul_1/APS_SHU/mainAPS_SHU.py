# translit Name to AlgName
def transliterate(name):
    # Dictionary with substitutions of words for symbols
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

    # Dictionary with transliterated residuals
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
        '(': '',
        ')': '',
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

    # Dictionary with exceptions
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
        'Reg_zaporno_reguliruusczim_Kl_na_prieme_GMK_PV4601_1_KC': 'RegKr1_KCU',
        'U_Osn_U_AC_V': 'U_Osn_AC',
        'U_Reserv_U_AC_V': 'U_Res_AC',
        'Pos_TRK_PV9604_1': 'Pos_TRK',
        'Pos_zaporno_reguliruusczego_Kl_na_prieme_GMK_PV4601_1': 'Pos_RegKr1',
        'Vb__': 'Vb_',
        'Reg_zaporno_reguliruusczim_Kl_na_prieme_GMK_PV4601_1': 'Set_RegKr1',
        'Kl_ESDV9601_1_na_prieme_GMK': 'Kr1',
        'Kl_ESDV9602_1_na_out_GMK': 'Kr2',
        'Kl_XV9605_1_na_peremyczke': 'Kr5',
        'Kl_XV9613_1_na_sbrose_priemnoi_linii': 'Kr13',
        'Trehhodovoi_Kl_XV9610_1_na_t_linii': 'Kr10',
        'Kl_Pusk_vzd_XV9608_1': 'Kr8',
        'Kl_ESDV9611_1_na_t_linii': 'Kr11',
        'Check_Osn_pit_SHU_GMK_AC_V': 'U_Osn_AC_ON',
        'Check_Reserv_pit_SHU_GMK_AC_V': 'U_Res_AC_ON',
        'Check_Ispr_Razr': 'RazrGood',
        'Dr_SHU_GMK_ON': 'DoorOpen',
        'Ispr_osn_IP_DC_V_vnutr_cepei': 'Ispr_Osn_DC_inC',
        'Ispr_rez_IP_DC_V_vnutr_cepei': 'Ispr_Res_DC_inC',
        'Ispr_osn_IP_DC_V_AI': 'Ispr_Osn_DC_AI',
        'Ispr_rez_IP_DC_V_AI': 'Ispr_Res_DC_AI',
        'Ispr_osn_IP_DC_V_DI_vnesh_': 'Ispr_Osn_DC_DI',
        'Ispr_rez_IP_DC_V_DI_vnesh_': 'Ispr_Res_DC_DI',
        'Ispr_osn_IP_DC_V_DO_vnesh_': 'Ispr_Osn_DC_DO',
        'Ispr_rez_IP_DC_V_DO_vnesh_': 'Ispr_Res_DC_DO',
        'Btn_na_Dr_Normalnyi_O': 'Btn_NO',
        'Check_vnesh_U_AC_V_ot_SHU_GMK': 'U_AC_outC_ON',
        'Sirena_na_Dr_PS': 'Snd_PS',
        'Sirena_na_Dr_AS': 'Snd_AS',
        'Svetovaja_indikator_na_Dr_PS': 'SvetInd_PS',
        'Svetovaja_indikator_na_Dr_AS': 'SvetInd_AS',
        'Svetovaja_indikacija_Btn_AO': 'SvetInd_Btn_AO',
        'Svetovaja_indikacija_Btn_na_Dr_NO': 'SvetInd_Btn_NO',
        'Ispr_Check_LSU': 'Meandr',
        'Detonacija_v_Cyl': 'Det_SC',
        'ASTP': 'ASUTP',
        'vrash_kolenczatogo_vala': 'vkv'
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


# get data from file
def getDataXls(f_name):
    import pandas as pd
    df = pd.read_excel(io=f_name, engine='openpyxl', header=3,
                       usecols="B,E,F,G,H,M")  # open first sheet in file and get data from selected columns
    apsList = []  # list for store output data
    for i in range(len(df)):
        param = df.iloc[i]  # selected line in dataframe
        if str(param[0]) != 'nan':  # if name empty
            if str(param[1]) != 'nan' or str(param[2]) != 'nan' or str(param[3]) != 'nan' or str(
                    param[4]) != 'nan':  # if all fields empty, then ignore line
                str1 = param.values.tolist()  # transform dataframe line in list
                str1.insert(0, transliterate(param[0]))  # insert algorithmic name in list first position
                apsList.append(str1)  # add list in oytput data list
    # find double algName
    qu = len(apsList)
    z=1
    for i in range(0, qu):
        for k in range(z, qu):
            if apsList[i][0] == apsList[k][0]:
                apsList[i][0] = f'{apsList[i][0]}_{transliterate(apsList[i][6])}'
                apsList[k][0] = f'{apsList[k][0]}_{transliterate(apsList[k][6])}'
                if apsList[i][6] == apsList[k][6]:
                    print('WARNING! Double algName in abonent. >_<')
        z=z+1

    print('Get data from file')
    return apsList

# Creation ANB data
def CreationANBdata(list, abRUS):
    listANB = []
    listTail = []
    for i in list:
        val = str(i[2]).replace(',', '.')
        # special for this project =)
        val = val.replace('*', '')
        if (val.isdigit() or '.' in val) and abRUS in str(i[6]):
            algName = f'Ps_{i[0]}_n'
            listANB.append([algName, float(val), i[1],i[0],i[6]])

        val = str(i[3]).replace(',', '.')
        # special for this project =)
        val = val.replace('*', '')
        if (val.isdigit() or '.' in val) and abRUS in str(i[6]):
            algName = f'Ps_{i[0]}_v'
            listANB.append([algName, float(val), i[1],i[0],i[6]])

        val = str(i[4]).replace(',', '.')
        # special for this project =)
        val = val.replace('*', '')
        if (val.isdigit() or '.' in val) and abRUS in str(i[6]):
            algName = f'As_{i[0]}_n'
            listANB.append([algName, float(val), i[1],i[0],i[6]])

        val = str(i[5]).replace(',', '.')
        # special for this project =)
        val = val.replace('*', '')
        if (val.isdigit() or '.' in val) and abRUS in str(i[6]):
            algName = f'As_{i[0]}_v'
            listANB.append([algName, float(val), i[1],i[0],i[6]])

        if (str(i[2]) == 'П' or str(i[2]) == 'п') and abRUS in str(i[6]):
            algName = f'Ps_{i[0]}'
            listTail.append([algName, str(i[2]), i[1], i[0],i[6]])
        if (str(i[3]) == 'П' or str(i[3]) == 'п') and abRUS in str(i[6]):
            algName = f'Ps_{i[0]}'
            listTail.append([algName, str(i[3]), i[1], i[0],i[6]])
        if (str(i[4]) == 'А' or str(i[4]) == 'а') and abRUS in str(i[6]):
            algName = f'As_{i[0]}'
            listTail.append([algName, str(i[4]), i[1], i[0],i[6]])
        if (str(i[5]) == 'А' or str(i[5]) == 'а') and abRUS in str(i[6]):
            algName = f'As_{i[0]}'
            listTail.append([algName, str(i[5]), i[1], i[0],i[6]])

    print('Creation ANB data')
    return listANB, listTail

# Creation scrypt ANB for start in Epsilon
def MakeStrustContent(list, name, ab):
    f_w = open(f'CreationStructs_{name}.py', 'w', encoding='UTF8')
    f_w.write('#encoding:utf-8' + '\n')
    f_w.write('from __future__ import print_function' + '\n')
    f_w.write(f'STRUCT_CONTENT_{name} = """\\' + '\n')

    for i in list:
            f_w.write(f'    {i[0]}:str_{name}; //[{i[4]}] {i[2]}' + '\n')

    f_w.write('"""' + '\n')
    f_w.write('proj = projects.primary' + '\n')
    f_w.write(f"folder = proj.find('Parameter lists {ab}', recursive=True)[0]" + '\n')
    f_w.write(f"struktur = folder.create_dut('{ab}_list_{name}')  # DutType.Structure is the default" + '\n')
    f_w.write(f'struktur.textual_declaration.insert(2, 0, STRUCT_CONTENT_{name})' + '\n')
    f_w.close
    print('Creation scrypt ANB for start in Epsilon')

# Creation analog parameter settings for emergency and warning messages
def CreationANB(list, name, ab):
    f_w = open(f'MakeCall_{name}.py', 'w', encoding='UTF8')
    f_w.write('#encoding:utf-8' + '\n')
    f_w.write('from __future__ import print_function' + '\n')
    f_w.write('CONTENT_var = """\\' + '\n')
    # f_w.write(' repTime: INT;' + '\n')
    f_w.write('"""' + '\n')
    f_w.write('CONTENT_body = """\\' + '\n')
    # f_w.write('repTime := 3600; // время ремонта аналоговых входов' + '\n')
    f_w.write(f'IF NOT {ab}_GVL.init THEN' + '\n')
    f_w.write('// -----------------------------------------' + '\n')
    f_w.write('// ----------Инициализация уставок ----------' + '\n')
    f_w.write('// -----------------------------------------' + '\n')
    for i in list:
        f_w.write(f'    {ab}_GVL.{name}.{i[0]}.Ust := {i[1]}; //{i[2]}' + '\n')

    f_w.write('    // ------------------------------- функция инициализации --------------------------------' + '\n')
    f_w.write('    // 1.                     уставка(BOOL)' + '\n')
    f_w.write('    // 2.                     |                          направление срабатывания.TRUE - верхняя, FALSE - нижняя(BOOL)' + '\n')
    f_w.write('    // 3.                     |                          |    значение, записываемое в ANB при неисправности канала: 0 - FALSE, 1 - TRUE, 2 - оставить то что было(INT)' + '\n')
    f_w.write('    // 4.                     |                          |    |    задержка на срабатывание(REAL)' + '\n')
    f_w.write('    //                        |                          |    |    |' + '\n')
    f_w.write('    // algGVL.ANB.As_Nst_v.Settings := VGALG.fnANB_init(TRUE, 0, 10.5);' + '\n')
    for i in list:
        dir='ERROR'
        if i[0].endswith('_v'):
            dir = 'TRUE'
        if i[0].endswith('_n'):
            dir = 'FALSE'
        f_w.write(f'    {ab}_GVL.{name}.{i[0]}.ANB_Settings := VGALG.fnANB_init({dir}, 0, 0); // {i[2]}' + '\n')
    f_w.write('END_IF;' + '\n')

    f_w.write('// -------------------------------------------' + '\n')
    f_w.write('// -------------Формирование уставок----------' + '\n')
    f_w.write('// -------------------------------------------' + '\n')
    for i in list:
        f_w.write(f'// {i[2]}' + '\n')
        proc=f'{ab}_GVL.{name}.{i[0]}.ANB := VGALG.fnANB_Processing({ab}_GVL.{name}.{i[0]}.ANB_Settings,' \
             f' {ab}_GVL.AI.{i[3]}.ToHMI.PV, ' \
             f'{ab}_GVL.AI.{i[3]}.ToHMI.fault_common, ' \
             f'{ab}_GVL.{name}.{i[0]}.Ust, ' \
             f'{ab}_GVL.{name}.{i[0]}.ANB_Internal);'
        f_w.write(f'{proc}' + '\n')
        st = 'ERROR'
        if i[0].startswith('As_'):
            st='as'
        if i[0].startswith('Ps_'):
            st='ps'
        f_w.write(f'{ab}_GVL.AI.{i[3]}.ToHMI.{st} := {ab}_GVL.{name}.{i[0]}.ANB;' + '\n')

    f_w.write('"""' + '\n')
    f_w.write('proj = projects.primary' + '\n')
    f_w.write(f"folder = proj.find('{name} {ab}', recursive=True)[0]" + '\n')
    f_w.write(f"struktur = folder.create_pou('{ab}_{name}_Call', type = PouType.Function,language=None, return_type='BOOL', base_type=None, interfaces=None)" + '\n')
    f_w.write('struktur.textual_declaration.insert(4, 0, CONTENT_var)' + '\n')
    f_w.write('struktur.textual_implementation.insert(0, 0, CONTENT_body)' + '\n')
    f_w.close
    print('Creation analog parameter settings ANB for emergency and warning messages')
    # return 0

#Creation SHU_APS_Init
def Creation_APS_Init(list, name, ab):
   f_w = open(f'MakeAPS_Init_{name}.py', 'w', encoding='UTF8')
   f_w.write('#encoding:utf-8' + '\n')
   f_w.write('from __future__ import print_function' + '\n')
   f_w.write('CONTENT_var = """\\' + '\n')
   # f_w.write(' repTime: INT;' + '\n')
   f_w.write('"""' + '\n')
   f_w.write('CONTENT_body = """\\' + '\n')
   # f_w.write('repTime := 3600; // время ремонта аналоговых входов' + '\n')
   f_w.write(f'IF NOT {ab}_GVL.init THEN' + '\n')
   f_w.write(f'    {ab}_GVL.Alarms.Fire := 1; // Пожар' + '\n')
   f_w.write(f'    {ab}_GVL.Alarms.AOs := 2; // Аварийный останов со стравливанием' + '\n')
   f_w.write(f'    {ab}_GVL.Alarms.AOb := 3; // Аварийный останов без стравливания' + '\n')
   f_w.write(f'    {ab}_GVL.Alarms.VOs := 4; // Вынужденный останов со стравливанием' + '\n')
   f_w.write(f'    {ab}_GVL.Alarms.VOb := 5; // Вынужденный останов без стравливания' + '\n')
   f_w.write(f'    {ab}_GVL.Alarms.AS := 6; // Авариная сигнализация без останова' + '\n')
   f_w.write(f'    {ab}_GVL.Alarms.PS := 7; // Предупредительная сигнализация' + '\n')
   f_w.write(f'    {ab}_GVL.Alarms.OS := 8; // Ограничительная сигнализация' + '\n')
   f_w.write('\n')

   #SHU_GVL.APS_Internal.As_Nst.target := SHU_GVL.Alarms.AOs; // Аварийно высокая частота вращения СТ
   for i in list:
       st = 'ERROR'
       if i[0].startswith('As_'):
          st='AOs'
       if i[0].startswith('Ps_'):
          st='PS'
       f_w.write(f'    {ab}_GVL.APS.{i[0]}.Intern.target := {ab}_GVL.Alarms.{st}; //[{i[4]}] {i[2]}' + '\n')
   f_w.write('END_IF' + '\n')
   f_w.write('"""' + '\n')
   f_w.write('proj = projects.primary' + '\n')
   f_w.write(f"folder = proj.find('{name} {ab}', recursive=True)[0]" + '\n')
   f_w.write(f"struktur = folder.create_pou('{ab}_{name}_Init', type = PouType.Function,language=None, return_type='BOOL', base_type=None, interfaces=None)" + '\n')
   f_w.write('struktur.textual_declaration.insert(4, 0, CONTENT_var)' + '\n')
   f_w.write('struktur.textual_implementation.insert(0, 0, CONTENT_body)' + '\n')
   f_w.close
   print('Creation APS init')

# Creations structure for APS
def CreationsStructsAPS(list,name,ab):
    f_w = open(f'CreationStructs_{name}.py', 'w', encoding='UTF8')
    f_w.write('#encoding:utf-8' + '\n')
    f_w.write('from __future__ import print_function' + '\n')
    f_w.write(f'STRUCT_CONTENT_{name} = """\\' + '\n')
    for i in range(len(list)):
        dir=''
        if list[i][0].endswith('_v'):
            dir = 'высокая'
        if list[i][0].endswith('_n'):
            dir = 'низкая'
        st = ''
        if list[i][0].startswith('As_'):
            st = 'аварийно'
        if list[i][0].startswith('Ps_'):
            st = ''
        out = f'	{list[i][0]}:str_{name}; //[{list[i][4]}] {list[i][2]} {st} {dir}' + '\n'
        f_w.write(out)
    f_w.write('"""' + '\n')
    f_w.write('proj = projects.primary' + '\n')
    f_w.write(f"folder = proj.find('Parameter lists {ab}', recursive=True)[0]" + '\n')
    f_w.write(f"struktur = folder.create_dut('{ab}_list_{name}')  # DutType.Structure is the default" + '\n')
    f_w.write(f'struktur.textual_declaration.insert(2, 0, STRUCT_CONTENT_{name})' + '\n')
    f_w.close
    print('Creations structure for APS')


#Creation SHU_APS_Processing
def Creation_APS_Processing(list, name, ab):
   f_w = open(f'MakeAPS_Processing_{name}.py', 'w', encoding='UTF8')
   f_w.write('#encoding:utf-8' + '\n')
   f_w.write('from __future__ import print_function' + '\n')
   f_w.write('CONTENT_var = """\\' + '\n')
   f_w.write(' unlock:BOOL;' + '\n')
   f_w.write('END_VAR' + '\n')
   f_w.write('VAR_IN_OUT' + '\n')
   f_w.write('    i: INT;' + '\n')
   f_w.write('    FirstOutIndex: INT;' + '\n')
   f_w.write('    new_wrn: BOOL;' + '\n')
   f_w.write('    new_crs: BOOL;' + '\n')
   f_w.write('    AlarmTarget: ARRAY[0..8] OF BOOL;' + '\n')
   f_w.write('"""' + '\n')
   f_w.write('CONTENT_body = """\\' + '\n')

   #SHU_GVL.APS_Internal.As_Nst.target := SHU_GVL.Alarms.AOs; // Аварийно высокая частота вращения СТ
   for i in list:
       '''st = 'ERROR'
       if i[0].startswith('As_'):
          st='AOs'
       if i[0].startswith('Ps_'):
          st='PS'
       f_w.write(f'    {ab}_GVL.APS.{i[0]}.Intern.target := {ab}_GVL.Alarms.{st}; // {i[2]}' + '\n')'''
       f_w.write(f'//[{i[4]}] {i[2]}' + '\n')
       f_w.write(f'VGALG.fnAPS_Processing({ab}_GVL.ANB.{i[0]}.ANB, 0.1, unlock, {ab}_GVL.APS.{i[0]}.Intern, FirstOutIndex,'\
                              f' i, {ab}_GVL.APS.{i[0]}.PV, new_wrn, new_crs, {ab}_GVL.Alarms, AlarmTarget);' + '\n')
   f_w.write('"""' + '\n')
   f_w.write('proj = projects.primary' + '\n')
   f_w.write(f"folder = proj.find('{name} {ab}', recursive=True)[0]" + '\n')
   f_w.write(f"struktur = folder.create_pou('{ab}_{name}_Processing', type = PouType.Function,language=None, return_type='BOOL', base_type=None, interfaces=None)" + '\n')
   f_w.write('struktur.textual_declaration.insert(2, 0, CONTENT_var)' + '\n')
   f_w.write('struktur.textual_implementation.insert(0, 0, CONTENT_body)' + '\n')
   f_w.close
   print('Creation SHU_APS_Processing')






if __name__ == '__main__':
    # get data from file [algName, Name, PSmin, PSmax, ASmin, ASmax, ConnectionPoint]
    apsList = getDataXls('Перечни вх-вых сигналов  v15.xlsx')

    # Creation ANB data [algNameANB, Value, Name, algName]
    listANB, listTail = CreationANBdata(list=apsList, abRUS='ГМК')

    # Creation scrypt ANB for start in Epsilon
    MakeStrustContent(list=listANB, name='ANB', ab='SHU')

    # Creation analog parameter settings ANB for emergency and warning messages
    CreationANB(list=listANB,name='ANB',ab='SHU')

    # Creations listAPS - structure for APS
    ablist = ['ГМК', 'БКД', 'БУЗ']
    listAPS = []
    for i in ablist:
        listANB_fstr, listTail_fstr = CreationANBdata(list=apsList, abRUS=i)
        listAPS = listAPS + listANB_fstr + listTail_fstr

    # Creations structure for APS
    CreationsStructsAPS(list=listAPS, name='APS', ab='SHU')

    # Creation SHU_APS_Init
    Creation_APS_Init(list=listAPS,name='APS',ab='SHU')


    # Creation SHU_APS_Processing
    Creation_APS_Processing(list=listAPS,name='APS',ab='SHU')

    #for i in range(len(listANB)):
    #   print(str(listANB[i]))