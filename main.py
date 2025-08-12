from src.processing import filter_by_state, sort_by_date
from src.utils import get_transactions
from src.generators import filter_by_currency
from src.search_dict import process_bank_search
from src.widget import get_date
from src.masks import get_mask_account, get_mask_card_number
from src.read_csv_excel import get_from_csv, get_from_excel
import json

"Доделать работу с csv и работу с excel"

print('Привет! Добро пожаловать в программу работы с банковскими транзакциями\n'
'Выберите необходимый пункт меню:')

answer = input(
'1. Получить информацию о транзакциях из JSON-файла\n'
'2. Получить информацию о транзакциях из CSV-файла\n'
'3. Получить информацию о транзакциях из XLSX-файла\n')


if answer == '1':
    print('Для обработки выбран JSON-файл.')
    answer = input('1. Ввести путь до файла\n'
             '2. Выбрать файл data/operations.json\n')

    if answer == '1':
        while True:
            answer = input('Введите путь до файла\n')
            dict_list = get_transactions(answer)
            if dict_list == []:
                continue

            file_format = 'json'
            break

    elif answer == '2':
        dict_list = get_transactions('data/operations.json')
        file_format = 'json'
elif answer == '2':
    print('Для обработки выбран CSV-файл.')
    answer = input('1. Ввести путь до файла\n'
             '2. Выбрать файл data/transactions.csv\n')

    if answer == '1':
        while True:
            answer = input('Введите путь до файла\n')
            dict_list = get_from_csv(answer)
            if dict_list == []:
                continue
            file_format = 'csv'
            break
    elif answer == '2':
        dict_list = get_from_csv('data/transactions.csv')
        file_format = 'csv'
elif answer == '3':
    print('Для обработки выбран XLSX-файл.')
    answer = input('1. Ввести путь до файла\n'
             '2. Выбрать файл data/transactions_excel.xlsx\n')
    if answer == '1':
        while True:
            answer = input('Введите путь до файла\n')
            dict_list = get_from_excel(answer)
            if dict_list == []:
                continue
            file_format = 'excel'
            break
    elif answer == '2':
        dict_list = get_from_excel('data/transactions_excel.xlsx')
        file_format = 'excel'

while True:
    answer = input('Введите статус, по которому необходимо выполнить фильтрацию.\n'
    'Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n')
    if answer.upper() == 'EXECUTED':
        filter = 'EXECUTED'
    elif answer.upper() == 'CANCELED':
        filter = 'CANCELED'
    elif answer.upper() == 'PENDING':
        filter = 'PENDING'
    else:
        print(f'Статус операции "{answer}" недоступен')
        continue

    dict_list = filter_by_state(dict_list, filter)
    print(f'Операции отфильтрованы по статусу "{filter}"')

    with open('data/test.json', 'w', encoding='utf-8') as file:
        json.dump(dict_list, file)
    break

answer = input('Отсортировать операции по дате? Да/Нет\n')
if answer.upper() == 'ДА':
    answer = input('Отсортировать по возрастанию или убыванию?\n')
    if answer.upper() == 'ПО ВОЗРАСТАНИЮ':
        dict_list = sort_by_date(dict_list)
        with open('data/test.json', 'w') as file:
            json.dump(dict_list, file)
    if answer.upper() == 'ПО УБЫВАНИЮ':
        dict_list = sort_by_date(dict_list, sort_by='increasing')
        with open('data/test.json', 'w') as file:
            json.dump(dict_list, file)

answer = input('Выводить только рублевые транзакции? Да/Нет\n')

dict_list = filter_by_currency(dict_list, 'RUB', file_format)
dict_list = list(dict_list)

with open('data/test.json', 'w') as file:
    json.dump(dict_list, file)

answer = input('Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n')

if answer.upper() == 'ДА':
    answer = input('Введите определенное слово:\n')

    dict_list = process_bank_search(dict_list, answer)
    with open('data/test.json', 'w') as file:
        json.dump(dict_list, file)


print('Распечатываю итоговый список транзакций')

count_description = len(dict_list)
print('Всего банковских операций в выборке:', count_description)

for i in dict_list:
    if i['description'] == 'Открытие вклада':

        date = get_date(i['date'])
        print(date, i['description'])

        mask_account = get_mask_account(i['to'])
        print('Счет', mask_account)

        if file_format == 'json':
            print('Сумма:', i['operationAmount']['amount'], i['operationAmount']['currency']['name'])
        elif file_format == 'csv':
            print('Сумма:', i['amount'], i['currency_code'])
        elif file_format == 'excel':
            print('Сумма:', i['amount'], i['currency_code'])
    elif i['description'] == 'Перевод с карты на карту':
        date = get_date(i['date'])
        print(date, i['description'])

        from_card_number = get_mask_card_number(i['from'])
        to_card_number = get_mask_card_number(i['to'])
        from_card_name = i['from'].split()
        to_card_name = i['to'].split()

        print(*from_card_name[:-1], from_card_number, '->', *to_card_name[:-1], to_card_number)
        if file_format == 'json':
            print('Сумма:', i['operationAmount']['amount'], i['operationAmount']['currency']['name'])
        elif file_format == 'csv':
            print('Сумма:', i['amount'], i['currency_code'])
        elif file_format == 'excel':
            print('Сумма:', i['amount'], i['currency_code'])
    elif i['description'] == 'Перевод организации':
        date = get_date(i['date'])
        print(date, i['description'])

        from_card_number = get_mask_card_number(i['from'])
        from_card_name = i['from'].split()
        to_mask_account = get_mask_account(i['to'])
        to_account_name = i['to'].split()

        print(*from_card_name[:-1], from_card_number, '->', *to_account_name[:-1], to_mask_account)
        if file_format == 'json':
            print('Сумма:', i['operationAmount']['amount'], i['operationAmount']['currency']['name'])
        elif file_format == 'csv':
            print('Сумма:', i['amount'], i['currency_code'])
        elif file_format == 'excel':
            print('Сумма:', i['amount'], i['currency_code'])
    elif i['description'] == 'Перевод со счета на счет':
        date = get_date(i['date'])
        print(date, i['description'])

        from_mask_account = get_mask_account(i['from'])
        from_account_name = i['from'].split()
        to_mask_account = get_mask_account(i['to'])
        to_account_name = i['to'].split()

        print(*from_account_name[:-1], from_mask_account, '->', *to_account_name[:-1], to_mask_account)

        if file_format == 'json':
            print('Сумма:', i['operationAmount']['amount'], i['operationAmount']['currency']['name'])
        elif file_format == 'csv':
            print('Сумма:', i['amount'], i['currency_code'])
        elif file_format == 'excel':
            print('Сумма:', i['amount'], i['currency_code'])
