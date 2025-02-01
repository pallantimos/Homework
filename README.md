# Описание проекта
Проект позволяет шифровать номер и счет карты а также отслеживать банковские операции клиента

# Структура проекта
* src/ папка с основным кодом проекта
* tests/ папка для создания тестов проекта

# Установка
1. Клонируйте репозиторий
````
git clone https://github.com/pallantimos/Homework.git
````

2. Установите зависимости
````
poetry install
````
# Использование

1. Создайте файл main.py в корне проекта
2. Импортируйте туда нужные вам модули
3. Используйте необходимые функции

# Пример использования
Код файла main.py

```
from src import processing, masks

print(processing.filter_by_state([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                                  {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                                  {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                                  {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]))
```
# Тестирование
Протестированы модули в директории src



