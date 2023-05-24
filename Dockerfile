# Use an official Python runtime as a parent image
FROM python:3.8-slim-buster

USER root

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code
RUN chmod +x /code

# Install system dependencies
RUN apt-get update && apt-get install -y gcc

# Install Python dependencies
COPY requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy project
COPY . /code/

COPY entrypoint.sh /code/
RUN chmod +x /code/entrypoint.sh
ENTRYPOINT ["/code/entrypoint.sh"]
# Run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
