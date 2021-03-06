# Интерактивная карта Москвы

<img src="static_src/readme_map.gif"/>

Проект представляет собой интерактивную карту, на которой отмечены интересные места с подробным описанием и фотографиями.

Пример работы проекта можно посмотреть [по ссылке](http://http://cok263.pythonanywhere.com/)

### Как запустить

Для запуска сайта вам понадобится Python третьей версии.

Скачайте код с GitHub. Затем установите зависимости

```sh
pip install -r requirements.txt
```
Разместите базу данных в каталоге с проектом рядом с manage.py. 
В случае отсутствия базы данных [создайте ее](#Создание-базы-данных).

Запустите разработческий сервер

```sh
python3 manage.py runserver
```
Для перехода на сайт воспользуйтесь следущей ссылкой [http://127.0.0.1:8000](http://127.0.0.1:8000)

Для управления базой данных перейдите по ссылке [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

### Создание базы данных
Для создания базы данных выполните

```sh
python3 manage.py migrate
```

Создайте суперпользователя для управления базой данных

```sh
python3 manage.py createsuperuser
```

### Переменные окружения

Часть настроек проекта берётся из переменных окружения. Чтобы их определить, 
создайте файл `.env` рядом с `manage.py` и запишите туда данные в таком формате: `ПЕРЕМЕННАЯ=значение`.

Доступны 2 переменные:
- `DEBUG` — дебаг-режим. Поставьте True, чтобы увидеть отладочную информацию в случае ошибки.
- `SECRET_KEY` — секретный ключ проекта

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
