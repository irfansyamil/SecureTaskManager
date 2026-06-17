# Secure Task Manager

### Project Description

This project is a secure web-based task management system developed for the Secure Software Development course. The system provides secure task management functionalities while implementing secure coding practices and web vulnerability mitigation mechanisms.

### Features

* **User Authentication:** Secure Login & Admin Dashboard verification
* **Task Management (CRUD):** Add, View, Edit, and Delete operational tasks
* **Input Validation:** Strict server-side regex filtering against script injections
* **Session Management:** Hardened browser-close session cookie expiration parameters
* **Protected Routes:** Forced authentication barriers across workspace panels
* **Fail-Safe Error Masking:** Custom error routing pages to hide backend code traces
* **Password Hashing:** Advanced database security encryption using Argon2

### Technologies Used

#### Frontend
* HTML5 / CSS3
* Bootstrap 5.3 (Cyber-Dark Theme layout elements)

#### Backend
* Django Web Framework (Python-based engine architecture)
* WhiteNoise (Production static asset delivery handling)

#### Database
* SQLite3 (Reinforced database core layout)

---
### Installation & Setup

Open Custom Frontend Dashboard: http://127.0.0.1:8000/

Open Admin Panel Backend: http://127.0.0.1:8000/admin/

1. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt

2.Database Initialization
   ```bash
   python manage.py makemigrations
   python manage.py migrate

Start Frontend Server

python manage.py runserver
  
