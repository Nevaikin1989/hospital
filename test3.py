def command_input():
    command_1 = input('Введите команду:')
    return command_1


def komanda_norm(command_1):
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

    if command_1 not in list_command:
        print('Неизвестная команда! Попробуте еще раз')
        command_input()
    else:
        if command_1 == 'стоп' or command_1 == 'stop':
            print('Сеанс завершён')
        else:
            print('Введите ID пациента')

command_input()
komanda_norm('command_1')