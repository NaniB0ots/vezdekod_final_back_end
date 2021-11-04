# Запуск проекта 

## Без docker
Требуется 
- python 3.9

Рабочая папка `app`


1. Установить зависимости
`$ pip install -r requirements.txt`
2. Создать файл `.env` и указать адрес базы данных (пример файл `.env.example`). Можно пропустить, тогда будет использоваться sqlite:
   - `DATABASE_URL=mysql://user:password@127.0.0.1:3306/db_name`
3. Выполнить миграции
`$ python manage.py migrate`

_Проект запускается на порту 8000_

## C использованием docker и docker-compose
`$ docker-compose up -d --build`

_Проект запускается на порту 8080_

# Демонстрация работы
##  Задание 1
Требуется: 
- python 3.9
- Установленные библиотеки: `requests` и `Pillow`:
  1. `$ pip install requests`
  2. `$ pip install Pillow`

Запуск скрипта: `python demonstration_task_1.py`

##  Задание 2
Требуется: 
- python 3.9
- Установленные библиотеки: `requests` и `Pillow`:
  1. `$ pip install requests`
  2. `$ pip install Pillow`

Запуск скрипта: `python demonstration_task_2.py`