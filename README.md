# DRF Practice Project

This is a practice project built with **Django** and **Django REST Framework (DRF)**.  
It includes basic CRUD APIs and some serializer validations for learning purposes.

## 🚀 Features
- Django REST Framework setup
- Custom serializers with validation
- ModelViewSet with search functionality
- Example API for students (name, roll no, etc.)

## 🛠️ Tech Stack
- Python 3.x
- Django
- Django REST Framework

## ⚡ How to Run Locally
```bash
# clone the repo
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>

# create virtual environment
python -m venv env
source env/bin/activate   # for Mac/Linux
env\Scripts\activate      # for Windows

# install dependencies
pip install -r requirements.txt

# run migrations
python manage.py migrate

# start server
python manage.py runserver
