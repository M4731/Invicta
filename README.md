# Invicta

**A web application that connects students with private tutors.**

Invicta helps students find a teacher, request a lesson, and share feedback. Teachers can present their experience, set their price, and manage lesson requests in one place.

Originally developed as my bachelor's degree project in 2022, the application is built with Python and Django.

## What you can do

- **Find a tutor:** browse teacher profiles and filter by subject. View descriptions, photos, prices in RON, and student ratings.
- **Request a lesson:** tell a teacher what you want to learn and when you are available.
- **Manage requests:** teachers can accept a request with a date and time or decline it.
- **Receive email notifications:** teachers are notified about new requests, and students receive confirmation when a lesson is accepted.
- **Share feedback:** students can write, edit, and delete reviews, with ratings from 1 to 10.
- **Manage your account:** separate registration for students and teachers, with login and account editing.
- **Contact the application team:** send a message through the contact form.

## How it works

1. **Teachers** register, choose a subject and price, and add a profile description and photo.
2. **Students** register, sign in, and browse the teacher directory to find a suitable tutor.
3. A student sends a lesson request describing their learning goals and availability.
4. The teacher reviews the request and confirms a date and time. The student receives an email confirmation.
5. Students can share their feedback on teacher profiles.

Administrators use Django's built-in admin panel to manage subjects, accounts, profiles, lessons, and reviews.

## Technologies

| Technology | Role |
| --- | --- |
| Python 3.14 & Django 5.2 | Application logic, page rendering, forms, and authentication |
| SQLite | Stores accounts, profiles, lesson requests, and reviews |
| HTML, CSS, JavaScript & Bootstrap | Page layout, styling, and browser interactions |
| django-filter | Filters the teacher directory by subject |
| Pillow | Supports uploaded profile images |
| Gmail SMTP | Sends contact messages and lesson notifications |
| python-dotenv | Loads local configuration from `.env` |
| Argon2 & bcrypt | Support Django's configured password hashing |

## Technical overview

Invicta is a server-rendered Django application: Django handles requests, reads and saves data through its ORM, and renders HTML templates for the browser. Authentication uses Django sessions and a custom user model with student and teacher roles.

The code is organized into four main apps:

| App | Responsibility |
| --- | --- |
| `accounts` | Users, registration, subjects, and teacher pricing |
| `profiles` | Teacher descriptions, photos, and profile pages |
| `lessons` | Lesson requests, scheduling, and email notifications |
| `reviews` | Student feedback and teacher ratings |

Each teacher is linked to a user account and a profile. Django signals create the profile automatically when a teacher is registered. Lessons and reviews connect students to teachers, while shared templates provide a consistent layout across the application.

## Run locally on Windows

### 1. Prepare the project

Install **Python 3.14** with the `py` launcher or `python` available in PATH. Clone this repository, or download and extract it, then open the project folder.

Double-click **`setup.bat`**. It will:

- Create the `.venv` Python environment and install the required packages.
- Create `invicta/.env` with a generated application secret key.
- Run Django's configuration check.

An internet connection is needed to download the packages. Running setup again preserves your existing environment and `.env` configuration. Database preparation is handled separately below.

### 2. Configure email

Open `invicta/.env` in a text editor and complete these values:

```dotenv
EMAIL_MAIL=your-test-account@gmail.com
EMAIL_PASSWORD=your-google-app-password
```

Use a Gmail account with a Google app password. These settings enable contact messages and lesson notifications. Keep your credentials in the private `.env` file, which is excluded from Git.

Setup generates `SECRET_KEY` automatically and sets `DEBUG=1` for local development. The shared `invicta/.env.example` file provides the configuration template.

### 3. Start the application

Double-click **`run.bat`**, then open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

Keep the server window open while using the application. Press **Ctrl+C** to stop it. Restart the server after changing `.env`.

### Database and administration

The application uses `invicta/db.sqlite3`. The setup script preserves this database.

To create the database tables when starting with a fresh database, run this command in PowerShell from the repository root:

```powershell
.\.venv\Scripts\python.exe invicta/manage.py migrate
```

To create your own administrator account:

```powershell
.\.venv\Scripts\python.exe invicta/manage.py createsuperuser
```

With the server running, sign in at [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/). On a fresh database, add at least one subject before registering a teacher.

### Terminal alternative

You can also run setup and start the server from PowerShell, from the repository root:

```powershell
.\setup.ps1
.\.venv\Scripts\python.exe invicta/manage.py runserver 127.0.0.1:8000
```
