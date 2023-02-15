import random

#list_of_patient = [random.randint(0,3) for i in range (100)] # создаем список клиентов
#print (len(list_of_patient))
#работа со списком пациентов
#test_list_of_patient=[0, 1, 1, 1, 1, 1, 1, 2, 2, 3]
#list_of_patient=test_list_of_patient*20
#len(list_of_patient) # узнаем длинну списка
#print(list_of_patient.count(1)) # считаем, сколько раз в нашем списке встречается
#print(list_of_patient[190]) # выводим статус пациента по его индексу
#print(list_of_patient)
#print(len(list_of_patient))



x = input('Введите команду:')
while x != 'STOP':
    if x == 'get status': #тут мы должны зайти в класс get status
        y = input('Введите ID пациента:')
        print('Статус пациента вот такой')
    elif x == 'status up':#тут мы должны зайти в класс status down
        y = input('Введите ID пациента ля повышения статуса:')
        print('Статус пациента изменен в лучшую сторону')


    x = input('Введите команду:')
#elif x == 'okk':
    #print('okk, then okk')
else:
    print('Сеанс завершён')


