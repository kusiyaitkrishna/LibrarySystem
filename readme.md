# LibrarySystem

A Django-based Library Management System for handling users, books, members, and dispatch workflows.

**Repository:** `kusiyaitkrishna/LibrarySystem`

---

## 📖 About the Project

This is a **Django 4.2** project structured into multiple apps:

- `accounts` – user and authentication-related logic (includes custom user model)
- `books` – book records and related operations
- `members` – member management
- `dispatch` – issue/return or dispatch-related flows

The project currently uses **SQLite** (`db.sqlite3`) as the default database.

---

## 🧰 Tech Stack

- Python 3.x
- Django 4.2.x
- SQLite (default, for development)

---

## 📁 Project Structure

```text
LibrarySystem/
│
├── LibrarySystem/          # Main Django project package (settings, urls, wsgi/asgi)
├── accounts/               # Accounts app
├── books/                  # Books app
├── members/                # Members app
├── dispatch/               # Dispatch app
├── templates/              # Global templates folder
├── manage.py               # Django management entry point
├── db.sqlite3              # SQLite database (local/dev)
└── readme.md               # Project documentation
```

---

## ⚙️ Local Setup

### 1) Clone the repository

```bash
git clone https://github.com/kusiyaitkrishna/LibrarySystem.git
cd LibrarySystem
```

### 2) Create and activate virtual environment

**Windows (PowerShell):**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3) Install dependencies

If `requirements.txt` exists:
```bash
pip install -r requirements.txt
```

If not, install Django manually:
```bash
pip install "Django>=4.2,<5"
```

### 4) Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5) Create superuser (optional)

```bash
python manage.py createsuperuser
```

### 6) Run development server

```bash
python manage.py runserver
```

Open: `http://127.0.0.1:8000/`

---

## 🔧 Important Django Configuration

From current settings:

- `INSTALLED_APPS` includes:
  - `accounts`
  - `books`
  - `members`
  - `dispatch`
- `AUTH_USER_MODEL = 'accounts.User'`
- Templates directory configured to use root `templates/`
- Database: SQLite (`db.sqlite3`)

---

## 🤝 Contribution Guide (Fork + Branch by Your Name)

If another user wants to contribute:

### 1) Fork this repository

Click **Fork** on:
`https://github.com/kusiyaitkrishna/LibrarySystem`

### 2) Clone your fork

```bash
git clone https://github.com/<your-username>/LibrarySystem.git
cd LibrarySystem
```

### 3) Add upstream remote

```bash
git remote add upstream https://github.com/kusiyaitkrishna/LibrarySystem.git
git remote -v
```

### 4) Create branch using your name/username

Use this format:
- `feature/<your-name>`
- `fix/<your-name>`
- `docs/<your-name>`

Example:
```bash
git checkout -b feature/krishna
```

or
```bash
git checkout -b feature/<your-github-username>
```

### 5) Commit and push

```bash
git add .
git commit -m "Add: short description of changes"
git push origin feature/<your-name>
```

### 6) Create Pull Request

Open your fork on GitHub and create a PR to:

- **base repo:** `kusiyaitkrishna/LibrarySystem`
- **base branch:** `main`

---

## ✅ Branch Naming Rule for Contributors

All contributors must create personal branches, such as:

- `feature/diksha`
- `feature/kusum`
- `feature/puja`

---

## 📝 Notes

- Do not commit secret keys or sensitive settings.
- Prefer adding `.env` and environment-based config for production.
- Avoid committing updated `db.sqlite3` unless intentionally required.

---

