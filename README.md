🟡 UNSTOP CLONE - DJANGO BASED WEB APP

This project is a functional clone of the Unstop platform built using Django and MySQL.
It includes multi-step registration, user dashboards, admin panel, event listings, and more.

--------------------------------------------------
✅ FEATURES:
--------------------------------------------------

- Candidate & Recruiter Registration (multi-step forms)
- Responsive frontend using Bootstrap
- Admin panel with authentication
- Profile management
- MySQL database integration
- Static and media file handling

--------------------------------------------------
🚀 HOW TO SET UP THIS PROJECT LOCALLY:
--------------------------------------------------

1. Clone the repository
   git clone https://github.com/Shubham-Goswami-Github/unstop-clone.git
   cd unstop-clone

2. Create and activate virtual environment

   For Windows:
     python -m venv venv
     venv\Scripts\activate

   For Mac/Linux:
     python3 -m venv venv
     source venv/bin/activate

3. Install dependencies
   pip install -r requirements.txt

   (If requirements.txt is not available, run:
    pip install django mysqlclient)

4. Import MySQL database

   - Start your MySQL server
   - Create a new database (e.g. unstopdb)
   - Import the SQL file from:
     database/unstopdb.sql
   (You can use phpMyAdmin, MySQL Workbench, or MySQL CLI)

5. Update database settings in unstop_clone/settings.py

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

6. Run migrations
   python manage.py makemigrations
   python manage.py migrate

7. Create superuser
   python manage.py createsuperuser

8. Run the server
   python manage.py runserver

   Open in browser:
   http://127.0.0.1:8000/

--------------------------------------------------
🔑 ADMIN PANEL:
--------------------------------------------------

URL: http://127.0.0.1:8000/admin/
Login using your superuser credentials

--------------------------------------------------
📁 PROJECT STRUCTURE:
--------------------------------------------------

unstop-clone/
│
├── database/
│   └── unstopdb.sql
│
├── unstop_clone/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── mainapp/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── ...
│
├── static/
├── media/
├── templates/
├── manage.py
└── readme.txt

--------------------------------------------------
👨‍💻 AUTHOR:
--------------------------------------------------

Shubham Goswami  
GitHub: https://github.com/Shubham-Goswami-Github

--------------------------------------------------
📬 CONTRIBUTIONS:
--------------------------------------------------

Pull requests are welcome. For major changes, open an issue first.

--------------------------------------------------
📝 LICENSE:
--------------------------------------------------

This project is for educational and learning purposes only.
