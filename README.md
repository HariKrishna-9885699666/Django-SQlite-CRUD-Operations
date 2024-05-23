# Django-SQLite-CRUD-Operations
Django - SQLite User Management

## Installation

```bash
mkdir storefront
cd storefront
pipenv install django
pipenv shell
django-admin startproject storefront .
python3 manage.py runserver 7000
python3 manage.py startapp storefront
```
- In VSCODE, view > command pallette > Then type Python: Select Interpreter. Then select pipenv related path.
- Update INSTALLED_APPS with "to-do-playground" in settings.py

```bash
python3 manage.py makemigrations users
python3 manage.py migrate
python3 create_superuser.py
python3 create_fakeusers.py
python3 manage.py runserver
```
