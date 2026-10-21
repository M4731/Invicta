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

### Current prerequisites

The original source references Django 3.2.5, and committed bytecode was generated with Python 3.10. These are historical clues, not a verified compatibility matrix. The dependency file contains packages pinned in 2022 and **does not explicitly list Django**. Dependency restoration and version alignment are required before a reproducible installation can be claimed.

Use an isolated environment. The following PowerShell steps outline the original setup; they have not yet been verified end to end:

```powershell
cd invicta
py -3.10 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Install a Django version compatible with the restored dependencies before proceeding. The original framework version should be used only to investigate the historical application in isolation; the portfolio refresh should establish and verify an updated dependency set.

### Environment variables

Create `invicta/.env`, next to `manage.py`, with your own values:

```dotenv
SECRET_KEY=replace-with-a-random-local-development-secret
DEBUG=1
EMAIL_MAIL=your-smtp-mailbox
EMAIL_PASSWORD=your-smtp-credential
```

`manage.py` loads this file through `django-dotenv`. WSGI and ASGI entry points do not load it themselves, so those processes need environment variables supplied separately.

The current email settings use Gmail SMTP on port 587 with TLS. Request creation, lesson acceptance, and the contact form send real email when configured. For a local demonstration, configure Django's console email backend before exercising these flows if you want to inspect messages locally.

### Database and server

For a clean setup, preserve the supplied `db.sqlite3` outside the working copy before replacing it with a new database. The repository currently includes an existing populated database; do not assume its records are suitable public demo data.

Once dependencies and environment variables are configured:

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

Static inspection on October 20, 2026 confirmed valid Python syntax in all 52 Python source files. The default local Python environment did not contain Django, so application startup, migrations, rendered pages, and user flows have not yet been verified. All four app test modules are placeholders with no implemented tests.

Issues identified during source review:

- Several account/profile/review update and lesson management views lack ownership restrictions on the server. Hiding an edit form in a template does not protect a POST request.
- Lesson acceptance reads date and time directly from POST data without a validating Django form or scheduling conflict checks.
- Duplicate review database errors are caught and logged in the model without a useful validation message to the user.
- `Profile.get_absolute_url()` references a route name that does not exist.
- Pagination contains misspelled fallback template attributes and relies on JavaScript to repair links.
- The default profile image is missing, and the shared layout lacks a mobile viewport declaration.
- Generated Python bytecode and the populated SQLite database are tracked; there is no `.gitignore`.
- The dependency set and local/demo configuration need restoration and verification.

See [the Romanian project analysis](docs/PROJECT_ANALYSIS_RO.md) for the detailed assessment and proposed portfolio work. Resolve the authorization issues and validate the setup before exposing this application publicly.
