FROM python:alpine

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN apk add --no-cache sqlite

COPY . .

# Create static files directory
RUN mkdir -p staticfiles

# Run migrations and collect static files during build
RUN python manage.py migrate
RUN python manage.py collectstatic --noinput

# Expose the application port
EXPOSE 8000

# Run migrations and create a superuser at runtime
CMD ["sh", "-c", "python manage.py migrate && \
    python manage.py shell -c \"from django.contrib.auth.models import User; \
    User.objects.filter(username='admin').exists() or \
    User.objects.create_superuser('admin', 'admin@example.com', 'admin')\" && \
    python manage.py runserver 0.0.0.0:8000"]