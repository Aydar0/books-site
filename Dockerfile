# Pull the base image
FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install poetry
RUN pip3 install poetry
# Set work directory
WORKDIR /code_django

# Install dependeces
COPY poetry.lock pyproject.toml /code_django/

RUN poetry config virtualenvs.create false && poetry install

# COPY project
COPY . /code_django/
