# возможные статусы пациентов
def return_patient_status(x):
    patient_status = {
        0: "Тяжело болен",
        1: "Болен",
        2: "Слегка болен",
        3: "Готов к выписке"
    }
    print(patient_status[x])

return_patient_status(3)


def komanda_norm (command_1):
    list_command = ['узнать статус пациента',
                    'повысить статус пациента',
                    'понизить статус пациента',
                    'выписать пациента',
                    'рассчитать статистику',
                    'стоп',
                    'get status',
                    'status up',
                    'status down',
                    'discharge',
                    'calculate statistics',
                    'stop']

    if command_1 in list_command: print ('Введите ID пациента:')
    else:
        print('Неизвестная команда! Попробуй еще раз')

#def squre(x):
    #print(x**3
     #   )
    #return (x**2)

#a=squre(6)
#print(a)

