# Smart Village

**Smart Village** is a web application designed to empower village communities by providing centralized access to village information, events, user profiles, and complaint management. The platform allows villagers to interact, participate in events, submit complaints, and view profession-wise profiles securely using **Djoser authentication**.

---

## Features

### 1. Village Information
- Displays detailed information about the village, including population, area, facilities, schools, health centers, and more.
- Users can view all relevant village data in a structured format.

### 2. Complaints & Responses
- Authenticated users can submit complaints regarding local issues.
- Admin can respond to complaints and mark them as resolved.
- Users can track the status of their complaints.

### 3. Events Management
- Admin can create, update, and delete events.
- Users can view upcoming events and join them.
- Users can leave events they previously joined.

### 4. User Profiles
- Profession-wise profiles to showcase villagers' skills and occupations.
- Each user has a profile automatically created upon registration.

### 5. Authentication
- **Djoser** provides secure registration, login, password reset, and token management.
- JWT authentication ensures API security.

---

## Tech Stack

| Layer       | Technology                       |
|------------|----------------------------------|
| Backend     | Django, Django REST Framework    |
| Authentication | Djoser, JWT                   |
| Frontend    | React, Axios                     |
| Database    | PostgreSQL / SQLite              |
| Media      | Cloudinary / Local Storage       |
| Deployment  | Docker / Heroku / AWS            |

---

## Installation

### Backend Setup
```bash
git clone https://github.com/yourusername/smart-village.git
cd smart-village/backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

