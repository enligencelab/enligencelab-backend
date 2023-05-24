# Enligence Laboratory Website Backend

> **Critical Warning:**<br>
> This guide is only for development environment. If you want to deploy this application into production, please turn
> off the debug mode and set your own select key in `enligencelab_backend\settings.py`. Find more
> at [Django Documentation](https://docs.djangoproject.com/en/4.2/).

## Introduction

This Django application is used as the backend of the Enligence Laboratory Official Website, also used as the
administration system of the laboratory.

## Installation

First, you need to install Python 3.8 or higher, and then install the dependencies.

```shell
pip install -r requirements.txt
```

Secondly, you need to get into the project directory and run the following commands to initialize the database.

```shell
python manage.py makemigrations
python manage.py migrate
```

Finally, you can run the development server. The default port is 8000.

```shell
python manage.py runserver
```

## Usage

Use the following command to create a superuser account.

```shell
python manage.py createsuperuser
```

After the all those steps, you can finally visit the administration website at http://localhost:8000/admin.