FROM python:3.11-slim AS builder
WORKDIR /app
COPY environment.yml .
RUN pip install pip --upgrade && \
    pip install -r <(conda run -n onboardi pip freeze)

COPY . .
CMD ["gunicorn", "backend.wsgi:application", "--bind", "0.0.0.0:8000"]

EXPOSE 8000