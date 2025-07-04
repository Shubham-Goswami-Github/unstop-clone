# 🟡 Unstop Clone - Django Based Web App

This project is a functional clone of the Unstop platform built using **Django** and **MySQL**.  
It includes multi-step registration, user dashboards, admin panel, event listings, and more.

---

## ✅ Features

- Candidate & Recruiter Registration (multi-step forms)
- Clean and responsive frontend using Bootstrap
- Admin panel with login authentication
- Profile management for users
- MySQL database integration
- Static and media file handling

---

## 🚀 How to Setup This Project Locally

Follow these steps to run the project on your system:

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Shubham-Goswami-Github/unstop-clone.git
   cd unstop-clone
Create and Activate Virtual Environment

For Windows:

bash
Copy
Edit
python -m venv venv
venv\Scripts\activate
For Mac/Linux:

bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate
Install Project Dependencies

bash
Copy
Edit
pip install -r requirements.txt
If requirements.txt is missing:

bash
Copy
Edit
pip install django mysqlclient
Import MySQL Database

Start your MySQL server

Create a new database (example name: unstopdb)

Import the SQL dump file located at:

pgsql
Copy
Edit
database/unstopdb.sql
Use MySQL Workbench, phpMyAdmin, or MySQL CLI to import.

Update MySQL Settings in settings.py

Open unstop_clone/settings.py and configure your DB settings:

python
Copy
Edit
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'unstopdb',
        'USER': 'your_mysql_username',
        'PASSWORD': 'your_mysql_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
Run Migrations

bash
Copy
Edit
python manage.py makemigrations
python manage.py migrate
Create Superuser (Admin Login)

bash
Copy
Edit
python manage.py createsuperuser
Run the Server

bash
Copy
Edit
python manage.py runserver
Now open browser and visit:
http://127.0.0.1:8000/

🔑 Admin Panel
URL: http://127.0.0.1:8000/admin/

Login using the superuser credentials you created earlier

📁 Folder Structure
php
Copy
Edit
unstop-clone/
│
├── database/
│   └── unstopdb.sql             ← MySQL dump file
│
├── unstop_clone/                ← Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── mainapp/                     ← Core Django app
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── ...
│
├── static/                      ← CSS, JS, assets
├── media/                       ← Uploaded media files
├── templates/                   ← HTML Templates
├── manage.py
└── README.md
