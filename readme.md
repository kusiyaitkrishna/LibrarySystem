# Library Management System  
**Final Project Assignment – Web Application Programming**  
**Technologies: Django / Django REST Framework**

## 1. Project Overview

This project is a **Library Management System** developed as part of the Final Project Assignment for Web Application Programming.  
It demonstrates core concepts of backend and full-stack web development, including:

- Authentication and authorization
- REST API development
- CRUD operations
- Database modeling and management
- Frontend integration for complete application flow

The system is designed to help manage library operations such as maintaining records and allowing authenticated users to perform protected actions.

---

## 2. Problem Statement

Managing library records manually can be inefficient and error-prone.  
This application solves that by providing a centralized digital system where users can securely log in and perform operations such as creating, viewing, updating, and deleting records through a web interface and backend API.

---

## 3. Key Features

### 3.1 Authentication System
- User login functionality
- Token/JWT-based authentication for protected routes
- Secure access to authenticated API endpoints
- Authorization checks for restricted actions

### 3.2 CRUD Functionality
The application supports complete CRUD functionality for library-related resources:

- **Create**: Add new records  
- **Read**: Retrieve and display existing records  
- **Update**: Modify existing records  
- **Delete**: Remove records from the system  

### 3.3 Complete Application Flow
The project includes both backend and frontend integration:

#### Backend
- Built with **Django** and **Django REST Framework**
- REST API endpoints / Django views
- JWT/Token authentication
- Database models and business logic

#### Frontend / UI
- User interface for:
  - Login
  - Accessing protected features
  - Performing CRUD operations
  - Viewing system results
- Technologies can include:
  - Django Templates
  - HTML, CSS, JavaScript  
  *(and optionally React, if integrated)*

---

## 4. Technology Stack

- **Backend Framework:** Django, Django REST Framework  
- **Programming Language:** Python  
- **Database:** SQLite / PostgreSQL  
- **Frontend:** HTML, CSS, JavaScript, Django Templates  
- **Authentication:** JWT / Token-based authentication  
- **Version Control:** Git + GitHub  

---

## 5. Installation & Local Setup

Follow these steps to run the project locally:

1. **Clone the repository**
   ```bash
   git clone https://github.com/kusiyaitkrishna/LibrarySystem.git
   cd LibrarySystem
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   ```

   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create superuser (optional but recommended)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Start the development server**
   ```bash
   python manage.py runserver
   ```

7. Open in browser:
   ```
   http://127.0.0.1:8000/
   ```

---

## 6. Features Implemented

- User authentication (login-based access)
- Protected routes/endpoints using token/JWT
- Full CRUD operations for library records
- API + UI integration
- Database-backed record management
- End-to-end system workflow for authenticated users

---

## 7. Project Manual / Demonstration

A project walkthrough video is provided below covering:

- Login process
- CRUD operations
- Overall system workflow

🎥 **Loom Video Demo:**  
https://www.loom.com/share/2886c233adca48e2aa81656f22c72edf

---

## 8. Version Control Notes

- The project is maintained using GitHub version control.
- Commits represent incremental development of features and fixes.
- Repository link for submission:  
  https://github.com/kusiyaitkrishna/LibrarySystem

---

## 9. Submission Checklist Mapping

This project includes:

- ✅ Authentication system (login + token/JWT-based protection)  
- ✅ CRUD functionality for main module  
- ✅ Backend + frontend complete flow  
- ✅ Database models and API/views  
- ✅ README documentation with setup and feature details  
- ✅ Video/manual demonstration link  
- ✅ GitHub repository submission  

---

## 10. Author

**GitHub:** [@kusiyaitkrishna](https://github.com/kusiyaitkrishna)
