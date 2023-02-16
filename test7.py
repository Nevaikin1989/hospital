# база пациентов
list_of_patient = [0, 1, 2, 2]


patient_status = {
        0: "Тяжело болен",
        1: "Болен",
        2: "Слегка болен",
        3: "Готов к выписке"
    }

# функция возвращающая статус пациента
def return_patient_status(patient_status_id):
    return patient_status[patient_status_id]


# функция выводящая статус пациента
def print_patient_status(patient_status_id):
    print(patient_status[patient_status_id])


# функция получения id статуса пациента (ок)
def get_id_patient_status(id_patient):
    # получаем id пациента
    id_patient_real = id_patient - 1
    # идем в базу пациентов (list_of_patient) и смотрим, какой у пациента id статуса его состояния
    patient_status_id = list_of_patient[id_patient_real]
    return patient_status_id


# вывод статуса пациента (ок)
def get_patient_status(id_patient):
    patient_status_id = get_id_patient_status(id_patient)
    print_patient_status(patient_status_id)


def print_new_status_patient(new_patient_status_id):
    status = return_patient_status(new_patient_status_id)
    new_status_patient = f"""Новый статус пациента: {status}"""
    print(new_status_patient)


# выписываем пациента из больницы
def discharge(id_patient):
    print('Пациент выписан из больницы')
    id_patient = id_patient - 1
    del list_of_patient[id_patient]


# увеличиваем статус пациента на +1
def up_patient_status(id_patient):
    patient_status_id = get_id_patient_status(id_patient)
    #print(patient_status_id)
    new_patient_status_id = patient_status_id + 1 #увеличиваем статус пациента на 1
    if new_patient_status_id == 4:
        new_patient_status_id = input('Желаете этого пациента выписать?:')
        if new_patient_status_id == 'да':
            discharge(id_patient)
            print(list_of_patient)
    else:
        id_patient = id_patient - 1
        list_of_patient[id_patient] = new_patient_status_id #меняем статус пациенца в списке
        print_new_status_patient(new_patient_status_id)




def down_patient_status(id_patient):
    patient_status_id = get_id_patient_status(id_patient)
    new_patient_status_id = patient_status_id - 1 #уменьшаем статус пациента на 1
    if new_patient_status_id == -1:
        print('В нашей  больнице пациенты не умирают')
    else:
        id_patient = id_patient - 1
        list_of_patient[id_patient] = new_patient_status_id #меняем статус пациенца в списке
        print_new_status_patient(new_patient_status_id)

#up_patient_status(4)

#new_status_patient = f"""Новый статус пациента: {status}"""
def calculate_statistic(list_of_patient):
    count_patient = len(list_of_patient)
    print_count_patient = f"""В больнице на данный момент находятся {count_patient} чел., и них:"""
    print(print_count_patient)

    status_1 = list_of_patient.count(0)
    if status_1 != 0:
        print_status_1 = f"""- в статусе "Тяжело болен": {status_1} чел."""
        print(print_status_1)

    status_2 = list_of_patient.count(1)
    if status_2 != 0:
        print_status_2 = f"""- в статусе "Болен": {status_2} чел."""
        print(print_status_2)

    status_3 = list_of_patient.count(2)
    if status_3 != 0:
        print_status_3 = f"""- в статусе "Слегка болен": {status_3} чел."""
        print(print_status_3)

    status_4 = list_of_patient.count(3)
    if status_4 != 0:
        print_status_4 = f"""- в статусе "Готов к выписке": {status_4} чел."""
        print(print_status_4)


calculate_statistic(list_of_patient)