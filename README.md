# 🤞&👊 DOMAIN&PUNCH - ANIME RESTAURANT

The site allows order or come to our restaurant and eat special food. Foods are unique you cant find this in another restaurant.

---

## 📌 Основные возможности

* ✅ User registration and authorization
* ✅ Unique login
* ✅ Menu with categories
* ✅ Saving orders in the database
* ✅ Food and Merch details
* ✅ Footer with information about the author on all pages

---

## ⚙️ Переменные окружения

The project uses the ``environs`` library and reads settings from the ``.env`` file, which must be located in the root of the project.

Пример файла .env:
```
SECRET_KEY=your_secret_key
ALLOWED_HOSTS = [hosts]
DEBUG = True or False
```

### Используемые переменные:

| Variable      | Purpose                                                                               |
|---------------|---------------------------------------------------------------------------------------|
| SECRET_KEY    | Flask Secret Key                                                                      |
| ALLOWED_HOSTS | It ensures your Django app only responds to requests from trusted domains. "*" is all |
| DEBUG         | Controls whether the app is in development or production mode                         |

---

## 🐍 Virtual environment (venv)

It is recommended to use ``venv`` to isolate project dependencies.

### Creating an Environment:
```bash
python -m venv venv
```
### Activation:

* Windows:

```bash
source venv\Scripts\activate
```

* Mac/Linux:

```bash
source venv/bin/activate
```

---

## 🚀 Project launch

1. Clone the repository:


```bash
git clone https://github.com/kerem212012/anime_restaurant.git
cd anime_restaurant
```

2. Create and activate a virtual environment (see above)

3. Install dependencies:


```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the root of the project and specify the variables (`SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS`)

5. Migrate project and create superuser:


```bash
python manage.py makemigration
python manage.py migrate
python manage.py createsuperuser
```

6. Start the server:


```bash
python manage.py runserver
```

7. Go to the browser:

[http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 📄 Project pages

| URL         | name                  |
|-------------|-----------------------|
| /           | Home page             |
| /register   | New user registration |
| /login      | Login                 |
| /logout     | Logout                |
| /contact    | About as              |
| /shop       | Sell food and merch   |
| /product/id | Product details       |

---

## 🎯 Project goal

The site was created for money making(fake)

## 📲 Deploying to internet

### 💳 Buy site

You need buy site from services I prefer [TimeWeb Cloud](https://timeweb.cloud/?utm_source=vh76046&utm_medium=timeweb&utm_campaign=timeweb-bring-a-friend)

### 🚶‍➡️ Enter to your site
You need [git bash](https://git-scm.com/downloads),
open git bash and print ```ssh 'your ip'``` then he asks yes or no say yes.
Then give him password of site.
After enter write ```reboot```.
Open ```.ssh``` file open file ```config``` in notebook.
And write:
```
Host 'name'
    HostName 'your ip'
    User root
```
Now you can enter your server like ```ssh 'name'```.
### 📑 Copying project
In your site(in git bash) you need come to ```opt``` file. For this you need do:
```bash
cd ..
cd opt/
```
After it, you need copy project. Example:
```bash
git clone https://github.com/kerem212012/anime_restaurant.git
```
### 👹 Add Daemon

Install gunicorn to do it enter to your project in bash from ```opt``` add venv:
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
Now installing gunicorn:
```bash
apt update
pip install gunicorn
```
Now to add daemon we need go to ```system``` file:
```bash
cd ..
cd ..
cd /etc/systemd/system
```
We need add file we can do it with ````nano````:
```bash
nano name.service
```
In this file add:
```
[Unit]
Description=Gunicorn instance for project_name
After=network.target

[Service]
WorkingDirectory=/opt/project_name
Environment="PATH=/opt/project_name/venv/bin"
ExecStart=/opt/project_name/venv/bin/gunicorn --workers 3 --bind unix:/opt/project_name/app_name.sock app_name.wsgi:application

[Install]
WantedBy=multi-user.target
```
Then lets start it:
```bash
systemctl start name.service
systemctl status name.service
```
Now let's add ````nginx````:
```bash
apt install nginx
cd /etc/nginx/sites-available
nano deafult
```
Delete all and write this if you want with ip:
```
server {
    listen 80;
    server_name your ip;

    location /static/ {
        root /opt/project_name/staticfiles/;
    }

        location /media/ {
        alias /opt/project_name/media/;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/opt/project_name/app_name.sock;
    }
}
```
If with domain buy domain like ````example.ru````:
```
server {
    listen 80;
    server_name name.ru www.name.ru;

    location /static/ {
        alias /opt/project_name/staticfiles/;
    }

    location /media/ {
        alias /opt/project_name/media/;
    }

    location / {
        proxy_pass http://unix:/opt/project_name/app_name.sock;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```
```bash
apt install certbot python3-certbot-nginx
certbot --nginx -d name.ru -d www.name.ru
```
Add ```CSRF_TRUSTED_ORIGINS = env.list("CSRF_TRUSTED_ORIGINS")``` in ````settings.py```` and add ```CSRF_TRUSTED_ORIGINS = http://name.ru, https://name.ru```to ````.env````.
And for safe site add:
```bash
from django.views.decorators.csrf import csrf_exempt
```

## SUBSCRIBE
[Chipsinka](https://www.youtube.com/channel/UC8WEUnlETWORTIWI4jb339A)
