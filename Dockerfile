FROM python:3.12-slim

WORKDIR /app

# Install dependencies first so this layer stays cached while only app code changes.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Then copy the application code.
COPY app/ app/
COPY wsgi.py .

# Run as a non-root user instead of root.
RUN useradd --create-home appuser
USER appuser

EXPOSE 8000

# gunicorn is a production WSGI server; wsgi:app points at the `app` object in wsgi.py.
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "wsgi:app"]
