# база пациентов
list_of_patient = [1]*200


patient_status = {
        0: "Тяжело болен",
        1: "Болен",
        2: "Слегка болен",
        3: "Готов к выписке"
    }


list_command_stop = ['стоп', 'stop']


list_command_work_with_patient_status = ['узнать статус пациента',
                'повысить статус пациента',
                'понизить статус пациента',
                'выписать пациента',
                'get status',
                'status up',
                'status down',
                'discharge']


# функция возвращающая статус пациента
def return_patient_status(patient_status_id):
    return patient_status[patient_status_id]


# функция выводящая статус пациента
def print_patient_status(patient_status_id):
    status_patient = patient_status[patient_status_id]
    status_patient = f"""Cтатус пациента: "{status_patient}" """
    print(status_patient)


# функция получения id статуса пациента
def get_id_patient_status(id_patient):
    # идем в базу пациентов (list_of_patient) и смотрим, какой у пациента id статуса его состояния
    patient_status_id = list_of_patient[id_patient]
    return patient_status_id


# вывод статуса пациента (ок)
def get_patient_status(id_patient):
    patient_status_id = get_id_patient_status(id_patient)
    print_patient_status(patient_status_id)


def print_new_status_patient(new_patient_status_id):
    status = return_patient_status(new_patient_status_id)
    new_status_patient = f"""Новый статус пациента: "{status}" """
    print(new_status_patient)


# выписываем пациента из больницы
def discharge(id_patient):
    del list_of_patient[id_patient]
    print('Пациент выписан из больницы')


# увеличиваем статус пациента на +1
def up_patient_status(id_patient):
    patient_status_id = get_id_patient_status(id_patient)
    new_patient_status_id = patient_status_id + 1 #увеличиваем статус пациента на 1
    if new_patient_status_id == 4:
        new_patient_status_id = input('Желаете этого пациента выписать? (да/нет):')
        if new_patient_status_id == 'да':
            discharge(id_patient)
        print('Пациент остался в статусе "Готов к выписке"')
    else:
        list_of_patient[id_patient] = new_patient_status_id #меняем статус пациенца в списке
        print_new_status_patient(new_patient_status_id)


def down_patient_status(id_patient):
    patient_status_id = get_id_patient_status(id_patient)
    new_patient_status_id = patient_status_id - 1 #уменьшаем статус пациента на 1
    if new_patient_status_id == -1:
        print('Ошибка. Нельзя понизить самый низкий статус (наши пациенты не умирают)')
    else:
        list_of_patient[id_patient] = new_patient_status_id #меняем статус пациенца в списке
        print_new_status_patient(new_patient_status_id)


def calculate_statistic(list_of_patient):
    count_patient = len(list_of_patient)
    print_count_patient = f"""В больнице на данный момент находятся {count_patient} чел., из них:"""
    print(print_count_patient)
    patient_status_keys = patient_status.keys()
    for key in patient_status_keys:
        status = list_of_patient.count(key)
        if status != 0:
            print_status = f"""- в статусе "{patient_status[key]}": {status} чел."""
            print(print_status)


def check_patient_in_list(id_patient):
    if id_patient <= len(list_of_patient):
        return id_patient
    print("Ошибка. В больнице нет пациента с таким ID")


def check_correct_patient_id(id_patient):
    if id_patient.isdigit():
        id_patient = int(id_patient)
        return check_patient_in_list(id_patient)
    else:
        print("Ошибка. ID пациента должно быть числом (целым, положительным)")


def good_command(enter_command):
    if enter_command == 'calculate statistics' or enter_command == 'рассчитать статистику':
        calculate_statistic(list_of_patient)
    elif enter_command in list_command_work_with_patient_status:
        id_patient = input('Введите ID пациента:')
        if check_correct_patient_id(id_patient):
            id_patient = int(id_patient) - 1
            if enter_command == 'get status' or enter_command == 'узнать статус пациента':
                get_patient_status(id_patient)
            elif enter_command == 'status up' or enter_command == 'повысить статус пациента':
                up_patient_status(id_patient)
            elif enter_command == 'status down' or enter_command == 'понизить статус пациента':
                down_patient_status(id_patient)
            elif enter_command == 'discharge' or enter_command == 'выписать пациента':
                discharge(id_patient)
    else:
        print('Неизвестная команда! Попробуте еще раз')


def enter_command():
    enter_command = input('Введите команду:')
    while enter_command not in list_command_stop:
        good_command(enter_command)
        enter_command = input('Введите команду:')
    print('Сеанс завершён')


enter_command()

