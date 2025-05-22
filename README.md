
# 🗓️ Event Management API

A Django REST Framework-based backend for managing user accounts and events, with JWT authentication and interactive API documentation.

---

## 🚀 Features

- User registration and login
- JWT authentication with access/refresh tokens
- Secure token refresh endpoint
- Full CRUD for events
- Swagger & ReDoc API documentation
- Django admin panel

---

## 🛠️ Tech Stack

- Python 3.10+
- Django 4+
- Django REST Framework
- SimpleJWT (for token-based authentication)
- drf-yasg (for Swagger docs)

---

## 📦 Installation

1. **Clone the repository**

```
git clone https://github.com/your-username/event_management_api.git
cd event_management_api
```

2. **Create virtual environment & activate it**
```

python -m venv venv
source venv/bin/activate  # On Windows use venv\Scripts\activate
```

3. **Install dependencies**
```

pip install -r requirements.txt
```

4. **Run migrations**
```

python manage.py migrate
```

5. **Create a superuser (optional)**
```

python manage.py createsuperuser
```

6. **Start the development server**
```

python manage.py runserver
```

## Authentication Endpoints

| Endpoint              | Method | Description              |
| --------------------- | ------ | ------------------------ |
| `/api/auth/register/` | POST   | Register a new user      |
| `/api/auth/login/`    | POST   | Login and receive tokens |
| `/api/auth/refresh/`  | POST   | Refresh access token     |


Example login response:
```json
{
  "refresh": "<refresh_token>",
  "access": "<access_token>"
}
```

## Event Endpoints

| Endpoint            | Method | Description        |
| ------------------- | ------ | ------------------ |
| `/api/events/`      | GET    | List all events    |
| `/api/events/`      | POST   | Create a new event |
| `/api/events/<id>/` | GET    | Retrieve an event  |
| `/api/events/<id>/` | PUT    | Update an event    |
| `/api/events/<id>/` | DELETE | Delete an event    |


All event endpoints require JWT Bearer token in the Authorization header:
Authorization: Bearer <access_token>



## API Documentation

Swagger: (https://event-management-api-2djy.onrender.com/swagger/)

## Project Structure

```
project/
├── accounts/        # Handles user registration & login
├── events/          # Handles event CRUD
├── event_manager/   # Project config with root urls.py
├── manage.py
```

## Contributing

Pull requests and stars are welcome!

## License

MIT License. Feel free to use and adapt.







