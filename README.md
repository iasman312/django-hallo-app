# django-hallo-app

Учебный проект группы python-7


# Установка и запуск проекта
Для запуска проекта установите python версии 3.7 и выше, pip и virualenv

После клонирования перейдите в склонированную папку и вывполните следующие команды:

--- 
###### Виртуальное окружение
Создайте виртуальное окружение:
```bash
python3 -m virtualenv -p python3 venv
```

Активируйте виртуальное окружение:
```bash
source venv/bin/activate
```
---
Перейдите в папку hello:
```bash
cd hello
```
---
###### Зависимости
Установите зависимости командой

```bash
pip install -r requirements.txt
```

Обратите внимание, что среди зависимостей есть библиотека [psycopg2](https://pypi.org/project/psycopg2/). Данная библиотека предназначена для работы с базой данных [PostgreSQL](https://www.postgresql.org) и для её установки требуется установить [PostgreSQL](https://www.postgresql.org), но поскольку мы используем [binary версию](https://pypi.org/project/psycopg2-binary/) - делать это необязательно. Однако если вы хотите работать с [PostgreSQL](https://www.postgresql.org) - сделать это всё-таки придётся. 

---
###### База данных

В данный момент приложение настроено на работу с базой данных [PostgreSQL](https://www.postgresql.org). В случае, если для локальной работы требуется использовать другую базу данных, например, [SQLite](https://www.sqlite.org/index.html) - создайте на одном уровне с `settings.py` модуль `local_settings.py`, если его нет. В данном модуле переопределите конфигурацию для базы данных.

Так например, чтобы использовать [SQLite](https://www.sqlite.org/index.html) выполните следующие действия:

Создайте модуль локальных настроек проекта:
```bash
touch hello/local_settings.py
```

Добавьте конфигурацию для работы с базой данных [SQLite](https://www.sqlite.org/index.html):

```python

from django.conf import settings


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': settings.BASE_DIR / 'db.sqlite3',
    }
}
```

---
###### Миграции
Примените миграции командой
```bash
./manage.py migrate
```

---
###### Фикстурные данные

Выполните следующие действия для загрузки фикстурных данных:

___важно соблюдать очерёдность выполнения команд___


```bash
./manage.py loaddata fixtures/auth.json
```
```bash
./manage.py loaddata fixtures/dump.json
```

___
###### Запуск сервера для локальной разработки

Чтобы запустить сервер выполните:

```bash
./manage.py runserver
```

___
###### Переменное окружение

Добавил пример заполнения env файла:
SECRET_KEY=django-insecure-$bw-@604nr@!ljl##b*v+0!aahu-bw^k0+zp1--0l&g2@*lu5j
ALLOWED_HOSTS=*
DB_HOST=localhost
DB_PORT=5432

___
###### Доступ

Для доступа в панель администратора перейдите по ссылке http://localhost:8000/admin


Username для администратора из фикстур: `admin`, пароль: `admin` (пользователь иммет доступ к панели администратора)
