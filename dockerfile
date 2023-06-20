FROM python:3.11.4-slim-bullseye

WORKDIR /smbirch

COPY Pipfile Pipfile.lock ./

RUN pip install pipenv && pipenv install --system

COPY . .

CMD ["gunicorn", "-b", "0.0.0.0:8000", "wsgi:app"]