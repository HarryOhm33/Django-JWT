# Django JWT Auth API 🔐

This is a simple authentication system built using Django, MongoEngine, and JWT (JSON Web Tokens). It supports user registration with OTP email verification, login, session management, and logout functionality.

## 🚀 Features

- Signup with OTP email verification
- Secure password hashing
- JWT token authentication (7-day expiry)
- Session tracking using MongoDB
- Logout and session invalidation
- Cookie & Header-based token handling

## 🛠️ Tech Stack

- Python & Django
- MongoDB (with MongoEngine)
- JWT (PyJWT)
- `python-decouple` for `.env` config
- REST API with Django REST Framework

## 🗂️ Project Structure
```

Jwt-Auth/
├── core/ # Django project folder
│ ├── main_project/ # Contains `urls.py`, `settings.py`, etc.
│ ├── user_auth/ # App with auth logic
│ └── env/ # .env file for secret keys
├── jwtenv/ # Virtual environment (should be in .gitignore)
├── requirements.txt
├── .env
├── .gitignore
└── README.md

```

## 🔐 Environment Variables

Create a `.env` file inside `core/env/` with:

```

SECRET_KEY=your_secret_key_here
EMAIL_HOST_USER=[your_email@example.com](mailto:your_email@example.com)
EMAIL_HOST_PASSWORD=your_email_password

````

Make sure it's **not committed** by including `env/` in your `.gitignore`.

## 🧪 API Endpoints

### Auth Routes

- `POST /signup` — Register a new user (sends OTP)
- `POST /verify-otp` — Verify OTP and activate user
- `POST /login` — Authenticate and return JWT token (stored in cookie)
- `POST /verify-session` — Validate active session and return user data
- `POST /logout` — Delete session and clear token cookie

## 🧾 Setup Instructions

## 1. Clone the repo

```bash
git clone https://github.com/yourusername/jwt-auth-django.git
cd jwt-auth-django
````

# 2. Create virtual environment
python -m venv jwtenv
source jwtenv/bin/activate  # On Windows: jwtenv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Add your .env file as described above

# 5. Run the server
python manage.py runserver

## 📦 Dependencies

Installed via `requirements.txt`:

- `Django`
- `djangorestframework`
- `mongoengine`
- `pyjwt`
- `bcrypt`
- `python-decouple`

## ⚠️ Note

- Make sure MongoDB is running locally or connect to a remote cluster.
- Sessions (tokens) are auto-expired using MongoDB TTL index.
- OTPs also expire in 5 minutes via TTL.

---

## 📄 License

This project is open source and free to use.

---

## 👨‍💻 Author

Developed by [Your Name](https://github.com/yourusername)

