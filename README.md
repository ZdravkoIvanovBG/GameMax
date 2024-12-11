# 🎮 GAMEMAX
### A Django-based application that allows users to browse and buy video games across various franchises. Users can register, login, add to cart, submit reviews, add to wishlist, manage orders and more.

# Project Setup Instructions

## Prerequisites

To run this project, you will need:

- Python 3.10+
- PostgreSQL for the database.

## Setup Guide

### Step 1: Clone the Repository

First, clone the repository to your machine:

```sh
git clone <repository-url>
```

### Step 2: Navigate to the project directory 

```sh
cd <repository-directory>
```

### Step 3: Configure Environment Variables

You need to set up the environment variables to run the project. 
A `.env.template` file is included in the repository to help you through the process.

1. Copy the `.env.template` file:
    ```sh
    cp .env.template .env
    ```

2. Edit the `.env` file and fill in the required values, such as:
   - `SECRET_KEY`: A secret key for Django.
       - You can generate a `SECRET_KEY` opening the Terminal and using:
         
        ```sh
        python manage.py shell
        ```
        ```sh
        from django.core.management.utils import get_random_secret_key
        print(get_random_secret_key())
        ```
   - Database connection settings - `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `HOST`, `PORT`.
   - `DEBUG`: Set to True for development, False for production.
   - `ALLOWED_HOSTS`: Add your allowed hosts.
   - `CSRF_TRUSTED_ORIGINS`: Add your allowed hosts with http/https://
   - `MAILJET_API_KEY`, `MAILJET_SECRET_KEY`: Leave Blank


### Step 4: Install Dependencies

Use Pycharm Terminal to Install Dependencies:
```sh
pip install -r requirements.txt
```

### Step 5: Set Up the Database

Ensure `PostgreSQL` is running and set up your database using the credentials provided in the `.env `file.

Next, run the following commands to apply database migrations:
```sh
python manage.py migrate
```

### Step 6: Import data.json Fixture

Run the following command to load the data into the database:

```sh
python manage.py loaddata GameMax/shop/fixtures/data.json
```

### Step 7: Create a Superuser
To access the admin panel, create a superuser account:

```sh
  python manage.py createsuperuser
```

Follow the prompts to set up the superuser.

### Step 8: Run the Server
Run the server with the following command:

```shell
python manage.py runserver
```

---

### Running Tests
Tests are located in the `tests/` directory.

To run the tests:
```shell
python manage.py test
```
