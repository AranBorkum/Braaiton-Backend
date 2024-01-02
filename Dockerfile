FROM python:3.11-slim-bullseye

ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY poetry.lock pyproject.toml ./

RUN pip3 install poetry

RUN poetry install

COPY . .

EXPOSE 8000
