# Django Server Setup and Run Guide

This repository contains a Django project. Follow the steps below to set up and run the Django server locally.

## Prerequisites

- [Python](https://www.python.org/downloads/) (version 3.x)
- [Pip](https://pip.pypa.io/en/stable/installation/)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/your-django-project.git
    ```

2. Navigate to the project directory:

    ```bash
    cd your-django-project
    ```

3. Create a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:

    - On Windows:

        ```bash
        venv\Scripts\activate
        ```

    - On macOS/Linux:

        ```bash
        source venv/bin/activate
        ```

5. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Database Setup

1. Apply migrations:

    ```bash
    python manage.py migrate
    ```

2. (Optional) Create a superuser for the admin interface:

    ```bash
    python manage.py createsuperuser
    ```

## Run the Django Server

Start the Django development server:

```bash
python manage.py runserver
