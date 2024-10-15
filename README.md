# **Theatre API Service**

This API, built with Django REST Framework (DRF), helps manage theatre services like plays, performances, halls, reservations, and tickets.


### Usage

- **Play Endpoints**: Manage plays, including details and actors.
- **Performance Endpoints**: Manage performances, including time and halls.
- **Reservation & Ticket Endpoints**: Book and manage reservations and tickets.
- **User Endpoints**: Register, login, and manage user-related actions.

Use http://localhost:8000/api/doc/swagger/ to see all available endpoints.

### Features

- JWT Authentication for secure access.
- Admin panel at /admin/ for managing the theatre system.
- Swagger documentation for easy navigation of API endpoints.
- Features for managing plays, performances, tickets, and theatre halls.
- Docker configuration for easy setup and deployment.


### Run service on your device

#### Clone repository
```
git clone https://github.com/dpiuro/theatre-api-service.git
cd theatre_api_service
```

#### Create and activate .venv environment
```
python -m venv env
source env/bin/activate  # For Unix
env\Scripts\activate     # For Windows
```

#### Install requirements
```
pip install -r requirements.txt
```

#### Migrate database
```
python manage.py migrate
```

#### Create superuser and run server
```
python manage.py createsuperuser
python manage.py runserver  # http://127.0.0.1:8000/
```

### Run with Docker

#### Clone repository
```
git clone git clone https://github.com/dpiuro/theatre-api-service.git
cd theatre_api_service
```
#### Create .env file and set up environment variables
```
POSTGRES_DB=theatre_db
POSTGRES_USER=admin
POSTGRES_PASSWORD=admin12345
POSTGRES_HOST=db
POSTGRES_PORT=5434
```

#### Build and run Docker containers
```
docker-compose up --build

```
