from database import *

#TODO add output info
@eel.expose
def save_common_info(last_name, first_name, dad_name, dob, doi):
    patients_t = insert_init_data(metadata)
    add_patient(patients_t, last_name, first_name, dad_name, dob, doi)
    return "completed"

# @eel.expose
# def convert_value_py(last_name, first_name, dad_name, dob, doi):
#     return save_common_info(last_name, first_name, dad_name, dob, doi)


# def determine_the_passport_age(dob, doi):
#     age = doi - dob
#     return age
