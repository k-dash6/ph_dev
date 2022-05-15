from database import *


#TODO add output info
@eel.expose
def save_common_info(last_name, first_name, dad_name, gender, dob, doi):
    insert_init_data(metadata)
    add_patient(last_name, first_name, dad_name, gender, dob, doi)
    dob = datetime.strptime(dob, "%Y-%m-%d")
    doi = datetime.strptime(doi, "%Y-%m-%d")
    age = determine_the_passport_age(dob, doi)
    table = choose_table(age, gender)
    return "completed"

# @eel.expose
# def convert_value_py(last_name, first_name, dad_name, dob, doi):
#     return save_common_info(last_name, first_name, dad_name, dob, doi)


def determine_the_passport_age(dob, doi):
    age = relativedelta(doi, dob)
    # print(age)
    return age

def choose_table(age, gender):
    if gender == "М":
        first = "Мальчики"
    else:
        first = "Девочки"

    # массив временных меток, между которыми меняется возраст
    years_steps = [[2,10,16],[3,2,29],[3,3,0],[3,8,29],[3,9,0],[4,2,29],[4,3,0],[4,8,29],[4,9,0],[5,2,29],[5,3,0],[5,8,29],[5,9,0],[6,2,29],[6,3,0],[6,8,29],[6,9,0],[7,5,29],[7,6,0],[8,5,29],[8,6,0],[9,5,29],[9,6,0],[10,5,29],[10,6,0],[11,5,29],[11,6,0],[12,5,29],[12,6,0],[13,5,29],[13,6,0],[14,5,29],[14,6,0],[15,5,29],[15,6,0],[16,5,29],[16,6,0],[17,5,29]]
    years = ["3","3,5","4","4,5","5","5,5","6","6,5","7","8","9","10","11","12","13","14","15","16","17"] #массив возможных значений для имени таблицы (па размеру совпадает с предыдущим массивом)

    second = None
    third = None
    converted_age = age.years*10000 + age.months*100 + age.days #для кодировки в формате yymmdd

    for i in range(0, len(years_steps), 2):
        left_border = years_steps[i][0]*10000 + years_steps[i][1]*100 + years_steps[i][2]
        right_border = years_steps[i+1][0]*10000 + years_steps[i+1][1]*100 + years_steps[i+1][2]
        if left_border <= converted_age <= right_border:
            second = years[int(i/2)]
            if left_border >= 40900: #перешли порог с года до лет (см названия таблиц после 4,5 года)
                third = "лет"
            else:
                third = "года"
            break

    if second is None: #если возраст не попал в границы, то кидаем exception
        raise RuntimeError('bad age')

    return metadata.tables[f"{first}, {second} {third}"]
