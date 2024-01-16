# Starts from the Python image
FROM python:3.11-slim

# Sets some environment variables (1=True)
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
RUN mkdir /code
WORKDIR /code

# Copies the dependencies file inside the container / step to avoid depedencies bug
COPY requirements.txt /code

# Upgrades pip and installs all dependencies / step to avoid depedencies bug
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# # Copies the rest of the source code
COPY . /code/

# Starts the Django app
# EXPOSE 8000
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]