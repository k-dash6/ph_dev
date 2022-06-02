from sqlalchemy.exc import NoSuchColumnError

from database import *
from variables import *

@eel.expose
def calculate_centiles(last_name, first_name, dad_name, gender, dob, doi, body_length, body_weight, ind_ketle,
                       lungs_capacity, d_r_wrist, d_l_wrist, systolic_pressure, diastolic_pressure, heart_rate,
                       teeth, biological_params):
    missing_fields = ["Длина тела", "Масса тела", "Жизненная ёмкость легких", "Динамометрия правой кисти",
                      "Динамометрия левой кисти", "Систолическое артериальное давление",
                      "Диастолическое артериальное давление", "Частота сердечных сокращений",
                      "Количество постоянных зубов"]

    missing_output=[]
    for i, value in enumerate([body_length, body_weight, lungs_capacity, d_r_wrist, d_l_wrist, systolic_pressure,
              diastolic_pressure, heart_rate, teeth]):
        if not value.isdigit():
            missing_output.append(missing_fields[i])
    if missing_output != []:
        return f'Некорректное значение в полях: {", ".join(map(str, missing_output))}'

    # Определение паспортного возраста и выбор нужной таблицы
    dob = datetime.strptime(dob, "%Y-%m-%d")
    doi = datetime.strptime(doi, "%Y-%m-%d")
    age = determine_the_passport_age(dob, doi)
    table, table_age_num = choose_table(age, gender)

    result = f'{last_name} {first_name} {dad_name}, {table_age_num} лет'

    # Определение группы физического развития
    length_centile = get_centiles(table, 'Длина тела', body_length)
    ind_ketle_centile = get_centiles(table, 'Индекс Кетле', ind_ketle)

    result += '<br/>Группа физического развития: '
    
    if 2 <= length_centile <= 7 and 3 <= ind_ketle_centile <= 6:
        result += "Нормальное физическое развитие."
    elif 2 <= length_centile <= 7 and 7 <= ind_ketle_centile <= 8:
        result += "Отклонения в развитии: Повышенная и высокая масса тела."
    elif 2 <= length_centile <= 7 and 1 <= ind_ketle_centile <= 2:
        result += "Отклонения в развитии: Сниженная и низкая масса тела."
    elif length_centile == 8:
        result += "Отклонения в развитии: Высокая длина."
    elif length_centile == 1:
        result += "Отклонения в развитии: Низкая длина тела."

    # Определение гармоничности развития
    if 3 <= ind_ketle_centile <= 6:
        imt_garm = True
    else:
        imt_garm = False

    lungs_capacity_centile = get_centiles(table, 'Жизненная ёмкость лёгких', lungs_capacity)
    d_r_wrist_centile = get_centiles(table, 'Динамометрия правой кисти', d_r_wrist)
    d_l_wrist_centile = get_centiles(table, 'Динамометрия левой кисти', d_l_wrist)

    if lungs_capacity_centile <= 2 or d_l_wrist_centile <= 2 or d_r_wrist_centile <= 2:
        jel_garm = False
    else:
        jel_garm = True

    systolic_pressure_centile = get_centiles(table, 'Сист. артериальное давление', systolic_pressure)
    diastolic_pressure_centile = get_centiles(table, 'Диаст. артериальное давление', diastolic_pressure)
    heart_rate_centile = get_centiles(table, 'Частота сердечных сокращений', heart_rate)

    if 2 <= systolic_pressure_centile <= 7 and 2 <= diastolic_pressure_centile <= 7 and 2 <= heart_rate_centile <= 7:
        gemo_garm = True
    else:
        gemo_garm = False

    if all([imt_garm, jel_garm, gemo_garm]):
        result += '<br/>Гармоничное развитие'
    elif not imt_garm and jel_garm and gemo_garm:
        result += '<br/>Дисгармоничное развитие за счёт показателя пропорциональности развития по ИМТ'
    elif imt_garm and not jel_garm and gemo_garm:
        result += '<br/>Дисгармоничное развитие за счёт показателей жизненной ёмкости лёгких и динамометрии'
    elif imt_garm and jel_garm and not gemo_garm:
        result += '<br/>Дисгармоничное развитие за счёт гемодинамических показателей'
    elif not imt_garm and not jel_garm and gemo_garm:
        result += '<br/>Дисгармоничное развитие за счёт показателей жизненной ёмкости лёгких, динамометрии и показателя пропорциональности развития по ИМТ'
    elif not imt_garm and jel_garm and not gemo_garm:
        result += '<br/>Дисгармоничное развитие за счёт гемодинамических показателей и показателя пропорциональности развития по ИМТ'
    elif imt_garm and not jel_garm and not gemo_garm:
        result += '<br/>Дисгармоничное развитие за счёт показателей жизненной ёмкости лёгких, динамометрии и гемодинамических показателей'
    elif not imt_garm and not jel_garm and not gemo_garm:
        result += '<br/>Дисгармоничное развитие за счёт показателей жизненной ёмкости лёгких, динамометрии, гемодинамических показателей и показателя пропорциональности развития по ИМТ'

    # Зубы
    if 7 <= int(table_age_num) <= 10 and gender == 'F' or 7 <= int(table_age_num) <= 12 and gender == 'M':
        teeth_dev_str = teeth_development(int(teeth), int(table_age_num), gender)
        result += teeth_dev_str
    # Половое развитие
    if 10 <= int(table_age_num) and gender == 'F' or 12 <= int(table_age_num) and gender == 'M':
        for param in biological_params:
            if param is None:
                return 'Вы не ввели данные о биологическом развитии'
        bio_dev_str = biological_development(biological_params, int(table_age_num), gender)
        result += bio_dev_str
    return result


def determine_the_passport_age(dob, doi):
    age = relativedelta(doi, dob)
    return age


def choose_table(age, gender):
    if gender == "M":
        first = "Мальчики"
    else:
        first = "Девочки"

    # массив временных меток, между которыми меняется возраст
    years_steps = [[6,9,0],[7,5,29],[7,6,0],[8,5,29],[8,6,0],[9,5,29],[9,6,0],[10,5,29],[10,6,0],[11,5,29],[11,6,0],[12,5,29],[12,6,0],[13,5,29],[13,6,0],[14,5,29],[14,6,0],[15,5,29],[15,6,0],[16,5,29],[16,6,0],[17,5,29]]
    years = ["7","8","9","10","11","12","13","14","15","16","17"]  # массив возможных значений для имени таблицы (па размеру совпадает с предыдущим массивом)

    second = None
    converted_age = age.years*10000 + age.months*100 + age.days  # для кодировки в формате yymmdd

    for i in range(0, len(years_steps), 2):
        left_border = years_steps[i][0]*10000 + years_steps[i][1]*100 + years_steps[i][2]
        right_border = years_steps[i+1][0]*10000 + years_steps[i+1][1]*100 + years_steps[i+1][2]
        if left_border <= converted_age <= right_border:
            second = years[int(i/2)]
            break

    if second is None:  # если возраст не попал в границы, то кидаем exception
        raise RuntimeError('bad age')

    return metadata.tables[f"{first}, {second} лет"], second


def get_centiles(table, col_name, value):
    all_rows = table.select().execute().fetchall()
    for num, row in enumerate(all_rows):
        try:
            if row[col_name] > int(value):
                return num + 1
        except NoSuchColumnError:
            return 0
    return 8


def teeth_development(teeth, table_age_num, gender):
    if teeth in teeth_dict[gender][table_age_num]:
        return '<br/> Уровень биологического развития (развитие постоянных зубов) соответствует паспортному возрасту'
    elif teeth < teeth_dict[gender][table_age_num][0]:
        return '<br/> Уровень биологического развития (развитие постоянных зубов) отстает от паспортного возраста'
    elif teeth > teeth_dict[gender][table_age_num][-1]:
        return '<br/> Уровень биологического развития (развитие постоянных зубов) опережает паспортный возраст'


def biological_development(biological_params, table_age_num, gender):
    if gender == 'F':
        points = 0
        for i in range(4):
            stage = biological_params[i]
            points += bio_points_girls[stage]

        if points in bio_scale_girls[table_age_num]:
            return '<br/> Уровень биологического развития (половое развитие) соответствует паспортному возрасту'
        elif points < bio_scale_girls[table_age_num][0]:
            return '<br/> Уровень биологического развития (рполовое развитие) отстает от паспортного возраста'
        elif points > bio_scale_girls[table_age_num][-1]:
            return '<br/> Уровень биологического развития (половое развитие) опережает паспортный возраст'

    if gender == 'M':
        points = 0
        for i in range(5):
            stage = biological_params[i]
            points += bio_points_boys[stage]

        if points in bio_scale_boys[table_age_num]:
            return '<br/> Уровень биологического развития (половое развитие) соответствует паспортному возрасту'
        elif points < bio_scale_boys[table_age_num][0]:
            return '<br/> Уровень биологического развития (рполовое развитие) отстает от паспортного возраста'
        elif points > bio_scale_boys[table_age_num][-1]:
            return '<br/> Уровень биологического развития (половое развитие) опережает паспортный возраст'




