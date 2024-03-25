# Домашнее задание к лекции «Python и БД. ORM»
___
## Структура 
```shell
│    models.py         # модели ORM
│    data_from_json.py # загрузка данных из json
│    run.py            # запуск программы
└─── fixtures
       tests_data.json  # тестовые данные
```
## Подготовка 
#### 1. В корневом каталоге нужно создать файл ```.env``` с переменными
```
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_HOST=
POSTGRES_PORT=
POSTGRES_DB=
```
#### 2. Установить необходимые библиотеки
Команда: ```pip install -r requirements.txt```

## Запуск
#### 1. Для загрузки тестовых данных нужно запустить файл ```data_from_json.py``` 
#### 2. Для работы программы нужно запустить ```run.py```