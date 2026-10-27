# Invicta

Invicta is a Django web application that connects students with private tutors. Students can browse teachers by subject, request lessons, and leave reviews. Teachers can manage their profiles and accept lesson requests with a proposed date and time.

This repository contains the original application, with migrations generated in August 2022. It is being prepared for a portfolio; the setup and known limitations below describe the current code, rather than a production-ready release.

## Features

- Separate student and teacher registration, with session-based authentication.
- Teacher profiles with an uploaded photo, description, subject, and price in RON.
- Teacher directory with subject filtering and pagination.
- Lesson requests containing learning requirements and availability notes.
- Teacher acceptance of requests with a scheduled date and time, or rejection by deleting the request.
- Email notifications for new requests and accepted lessons.
- Teacher reviews with ratings from 1 to 10 and an average rating on profiles.
- Student review creation, editing, and deletion, with one review per student and teacher at database level.
- Contact form that sends email to the configured application mailbox.
- Django administration for users, subjects, teachers, profiles, lessons, and reviews.

The application coordinates requests. It does not implement payments, video lessons, calendar conflict detection, or a requirement to complete a lesson before reviewing a teacher.

## Technology and structure

Python, Django, SQLite, Django templates, custom CSS and JavaScript, Bootstrap, django-filter, and SMTP email.

```text
invicta/
  manage.py
  requirements.txt
  invicta/       # Settings, main routes, home, teacher directory, contact form
  accounts/      # Custom user, student/teacher signup, subjects and prices
  profiles/      # Teacher profiles and automatic profile creation via signals
  lessons/       # Lesson requests, acceptance, rejection, notifications
  reviews/       # Ratings and review management
  templates/     # Shared layout and general pages
  static/        # Styles, scripts and images
  media/         # Uploaded profile images
```

The custom `User` extends Django's `AbstractUser`. A `Teacher` belongs to one user and one subject, and has one `Profile`. Each `Lesson` and `Review` links a student user to a teacher. Pages are rendered on the server using Django class-based views.

## Local development setup

### Windows quick start

Install Python **3.14** with the `py` launcher or `python` available in PATH, then clone this repository. Internet access is required to download dependencies.

1. Double-click `setup.bat` in the repository root. It runs `setup.ps1`, creates `.venv` if needed, checks Python 3.14, installs `invicta/requirements.txt`, prepares `invicta/.env`, and runs Django's configuration check. The window stays open so errors can be read.
2. Open `invicta/.env` in a text editor and fill in `EMAIL_MAIL` (the Gmail test account) and `EMAIL_PASSWORD` (its Google app password). These are needed for contact and lesson emails, not for the home page.
3. Double-click `run.bat`, wait for the server to start, and open http://127.0.0.1:8000/ in your browser. Keep the console open; stop the server with Ctrl+C.

No virtual environment activation or typed startup commands are needed. From PowerShell, setup can also be run with `.\setup.ps1`.

Setup preserves an existing `.venv` and `.env`; an environment with a different Python version is reported rather than deleted. Re-running setup installs the declared dependencies again. Failures stop setup and display an error; fix the reported problem and rerun it.

### Environment variables

`invicta/.env.example` is the shared template with empty credentials. On first setup, the script creates `invicta/.env` from it and fills `SECRET_KEY` with a cryptographically random value. `DEBUG=1` enables local development mode. An existing `.env` is never overwritten, even if incomplete; edit it manually when needed.

The private `.env` and `.venv` are excluded from Git. Each new computer builds its own environment and secret key; transfer email credentials separately or use another test account. Never commit actual passwords to `.env.example`.

Django settings load `invicta/.env` through `python-dotenv`. Existing process environment variables take precedence. Email uses Gmail SMTP on port 587 with TLS and sends real messages when configured. Restart the server after changing `.env`.

### Database and server

For a clean setup, preserve the supplied `db.sqlite3` outside the working copy before replacing it with a new database. The repository currently includes an existing populated database; do not assume its records are suitable public demo data.

Setup does not migrate, reset, or seed the database. Database preparation is a separate step. For a fresh database, once dependencies and environment variables are configured (run these from `invicta/` using the virtual environment):

```powershell
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver 127.0.0.1:8000
```

Open `http://127.0.0.1:8000/`. The current host configuration includes `127.0.0.1`, but does not include `localhost`.

On a fresh database, create subjects through `/admin/` before registering teachers. Teachers select an existing subject during registration. New teacher profiles currently reference `media/profile_images/default.jpg`, which is missing from this repository; upload an image or add a default image as part of setup.

## Suggested demonstration

1. Add a subject using the administrator account.
2. Register a teacher, set a price, and edit the profile description and image.
3. Register a student and filter the teacher directory by subject.
4. Request a lesson, including requirements and availability.
5. Sign in as the teacher and accept the request with a date and time.
6. Sign in as the student to view the accepted request and submit a review.

Configure email before steps 4 and 5. The current application does not isolate email delivery failures from the user-facing request flow.

## Verification and known limitations

Local startup with Python 3.14 and Django 5.2.18 and test email delivery were confirmed during local setup on October 21, 2026. This does not verify every user flow. All four app test modules are placeholders with no implemented tests.

Issues identified during source review:

- Several account/profile/review update and lesson management views lack ownership restrictions on the server. Hiding an edit form in a template does not protect a POST request.
- Lesson acceptance reads date and time directly from POST data without a validating Django form or scheduling conflict checks.
- Duplicate review database errors are caught and logged in the model without a useful validation message to the user.
- `Profile.get_absolute_url()` references a route name that does not exist.
- Pagination contains misspelled fallback template attributes and relies on JavaScript to repair links.
- The default profile image is missing, and the shared layout lacks a mobile viewport declaration.
- Historical generated Python bytecode and the populated SQLite database are tracked. `.gitignore` excludes new bytecode, the local environment, and private configuration; it does not untrack existing files.
- The dependency file pins direct dependencies; it is not a complete lock file. A clean installation on another device still needs verification.

See [the Romanian project analysis](docs/PROJECT_ANALYSIS_RO.md) for the detailed assessment and proposed portfolio work. Resolve the authorization issues and validate the setup before exposing this application publicly.
