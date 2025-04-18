pipeline {
    agent any

    environment {
        DOCKER_COMPOSE_FILE = 'docker-compose.yml'
    }

    stages {
        stage('Checkout Code') {
            steps {
                echo 'Checking out code...'
                checkout scm
            }
        }

        stage('Build Docker Images') {
            steps {
                echo 'Building Docker images...'
                sh 'docker-compose build'
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running tests...'
                // Run Django tests
                sh 'docker-compose run --rm django_app python manage.py test'
            }
        }

        stage('Deploy Containers') {
            steps {
                echo 'Deploying containers...'
                sh 'docker-compose up -d'
            }
        }
    }

    post {
        always {
            echo 'Cleaning up...'
            sh 'docker-compose down'
        }
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}