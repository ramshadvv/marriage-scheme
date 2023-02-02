## Deployment

#### To deploy this project run

Clone the github repository:

```bash
  git clone https://github.com/ramshadvv/marriage-scheme.git
```

Go to the project directory:

```bash
  cd marriage-scheme
```

Create virtualenv:

```bash
  python -m venv env
```

Activate environment:

```bash
  env/Scripts/activate
```

install dependencies:

```bash
  pip install -r requirements.txt
```

Add .env file to the folder:

```bash
  Assign values to APP_PASSWORD, EMAIL_HOST for sending email
```

Migarte all models:

```bash
  python manage.py makemigrations
  python manage.py migrate
```

Start the server:

```bash
  python manage.py runserver
```
