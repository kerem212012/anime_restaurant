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

5. Инициализируйте базу данных:


```bash
python manage.py shell
from app import db
db.create_all()
exit()
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

The site was created as ////
