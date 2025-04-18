# Web Frameworks Assignment: Flask, Django, and Docker Compose

This project demonstrates the implementation of web applications using Flask and Django frameworks, containerized and deployed with Docker Compose.

## Project Structure

```
web_frameworks_assignment/
├── flask_app/             # Simple Flask application
│   ├── app.py             # Main Flask application file
│   ├── templates/         # HTML templates
│   ├── static/            # Static files
│   ├── requirements.txt   # Python dependencies
│   └── Dockerfile         # Docker configuration for Flask app
├── django_app/            # Django inventory management application
│   ├── manage.py          # Django management script
│   ├── inventory_project/ # Django project settings
│   ├── inventory/         # Django app files
│   ├── templates/         # HTML templates
│   ├── static/            # Static files
│   ├── requirements.txt   # Python dependencies
│   └── Dockerfile         # Docker configuration for Django app
├── docker-compose.yml     # Docker Compose configuration
└── README.md              # Project documentation
```

## Features

### Flask Application

- Homepage with "Hello, World!" message
- Form to accept user's name and age
- Form validation and error handling
- Bootstrap styling for a modern UI

### Django Application

- Product inventory management system
- Database integration with SQLite
- Admin panel for managing products
- Form to add new products directly from the homepage
- Responsive UI with Bootstrap

### Docker Setup

- Containerized Flask and Django applications
- Docker Compose for managing containers
- Network configuration for service communication
- Volume mapping for development

## How to Run the Project

### Prerequisites

- Docker and Docker Compose installed on your system

### Steps to Run

1. Clone the repository

   ```bash
   git clone <repository-url>
   cd web_frameworks_assignment
   ```

2. Build and start the containers

   ```bash
   docker-compose up --build
   ```

3. Access the applications:

   - Flask application: http://localhost:5000
   - Django application: http://localhost:8000
   - Django admin panel: http://localhost:8000/admin (username: admin, password: admin)

4. To stop the containers
   ```bash
   docker-compose down
   ```

## Development

### Flask App

The Flask application demonstrates basic routing, form handling, and error validation.

### Django App

The Django application showcases a product inventory management system with database integration, admin panel customization, and form implementation.

### Docker Configuration

Docker Compose is used to manage both containers, ensuring they're accessible on different ports.

## Credits

Created by Anuj Agrawal for the Web Frameworks Assignment
