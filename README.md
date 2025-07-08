# DJ04. Формы и развертывание проекта

### Задание
- Создайте проект с именем **movie_project** и приложение в нем **films**.
- Создайте модель(таблицу) в которой будет поле для названия фильма, поле для описание фильма и поле для отзыва.

- Создайте две **html** страницы
  - на одной из которых нужно заполнить 3 поля и отправить эту информацию в базу данных
  - на второй будет публиковаться информация которую вы записали в базу данных.

```bash
django-admin startproject movie_project
cd movie_project
python manage.py startapp films
```

```bash
python movie_project/manage.py makemigrations
python movie_project/manage.py migrate
python movie_project/manage.py createsuperuser
python movie_project/manage.py runserver
```