# chatbot

# Requirements

Python 2.7

Make sure you have pip (pip --version)

pip install virtualenv to install virtual environment

Postgresql

# What to do
To get this running, you need the following. First install dependencies

Step 0 : Clone the Repository

git clone https://github.com/nebeedtp/chatbot

Step 1 : Install dependencies

pip install -r requirements.txt

Step 2 : Run migrations

It's suppose to use the postgresql database system, for this in the settings, in the DATABASE section specify the following parameters:

'NAME ': 'smyt_careers' # real database name

'USER': 'smyt',  # database username

'PASSWORD': 'password', # database user password

'HOST': 'localhost', # database host

'PORT': '5432', # database port

To run migrations

 python manage.py migrate

Step 3 : Start the local server

python manage.py runserver

Step 4 : The main page is the login window

http://127.0.0.1:8000

it will be redirected to http://127.0.0.1:8000/chat  once logged in

Step 5 : We can register new users From admin panel

http://127.0.0.1:8000/admin

Step 6 : To see all the users and the number of calls they have made.

http://127.0.0.1:8000/user_list

