# 📝 Django To-Do List App

A simple, responsive to-do list app built with Django and Bootstrap 5.

---

## 🚀 Features

- Add new tasks
- Mark tasks as complete/incomplete
- Delete tasks
- Mobile-friendly UI using Bootstrap

---

## 🛠️ Requirements

- Python 3.8+
- pip

---

## 🔧 Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/Alangsam/django-app-todo.git
cd django-todo-app
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
pip install -r requirements.txt
pip freeze > requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
Then visit: http://127.0.0.1:8000/

## 📁 Project Structure
```text
todo_project/
├── manage.py
├── requirements.txt
├── README.md
│
├── todo_project/               # Project-level settings
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── todo/                       # Main app
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   ├── templates/
│   │   └── todo/
│   │       └── task_list.html
│   └── static/
│       └── todo/
│           ├── css/
│           └── js/
│
├── db.sqlite3                  # SQLite database
└── venv/                       # Python virtual environment

