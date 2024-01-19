# adsAPI
API with Django Rest Framework (DRF) for a classified ads site

## Technologies
- Python 3.11
- Django 5.0.1
- Django REST Framework 3.14.0

## Installation
- Clone the repository:
```bash
git clone https://github.com/<repo_url>
```
- Navigate into the project directory:
```bash
cd ads-api
```
- Create a virtual environment:
```bash
python -m venv env
``` 
- Activate the virtual environment:
```bash
source env/bin/activate (Linux/MacOS)
env\Scripts\activate (Windows)
```
- Install dependencies:
```bash
pip install -r requirements.txt
```
- Setup database:
```bash
python manage.py makemigrations
python manage.py migrate
```
- Create admin user:
```bash
python manage.py createsuperuser
```
- Run development server:
```bash
python manage.py runserver
```

**The API should now be running at http://127.0.0.1:8000/**


>[!TIP] 
>Authentication is required for protected endpoints. Pass the JWT token in the Authorization header:
>```bash
>Authorization: Bearer <token>
>```

## Endpoints:

### Authentication
- /token/ - Obtain JWT token
- /token/refresh/ - Refresh JWT token
- /register/ - User registration

### Profile:
- /profile/ - Get user profile
- /profile/update/ - Update user profile

### Categories:
- /category/ - List all categories
- /category/<int:pk>/ - Get single category by ID

### Advertisements:
- /advertisement/ - List all published advertisements
- /advertisement/<int:pk>/ - Get advertisement detail
- /advertisement/<int:pk>/comment/ - Create comment on advertisement

### User Advertisements:
- /my-advertisements/ - List user's own advertisements
- /my-advertisements/<int:pk>/ - Get user advertisement detail
- /my-advertisements/<int:pk>/publish/ - Publish user advertisement

### Moderation:
- /pending-advertisement/ - List pending advertisements for moderation
- /pending-advertisement/<int:pk>/ - Get pending advertisement detail
- /pending-advertisement/<int:pk>/approve/ - Approve pending advertisement