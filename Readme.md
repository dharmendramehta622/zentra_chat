# Django Project

## Introduction

This is a Django-based web application designed to Attendance Management System. It includes features such as Authentication and Authorization, Clockins, etc.

## Features
- Authentication and Authorization
- Attendance
- Admin Panel

## Prerequisites

- Python 3.x
- Django 3.x or higher
- PostgreSQL/MySQL/SQLite (SQLite)
- Other dependencies (in the requirements.txt)

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://your_username:your_password@github.com/Hamro-Kura-Kani/attendo.git
    or 
    git clone https://your_access_token:your_access_token@github.com/Hamro-Kura-Kani/attendo.git
    cd attendo
    ```

2. **Create and activate a virtual environment:**

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Configure the database:**

    Update the `DATABASES` setting in `attendo/settings.py` to match your database configuration.

5. **Apply migrations,Create a superuser,Run the development server:**

    ```sh
    chmod +x entryPoint.sh
     For Windows - bash entryPoint.sh 
     For Mac or Linux - ./entryPoint.sh
    ```
## Usage

1. **Access the application:**

    Open your web browser and navigate to `http://127.0.0.1:8000/`.

2. **Admin panel:**

    Navigate to `http://127.0.0.1:8000/admin/` and log in with the superuser credentials you created earlier(available in entryPoint.sh).

## Testing

To run the tests for this project:

```sh
python manage.py test
