pipeline {
    agent none
    stages {
        stage('Build') {
			agent {
				docker {
					image 'python:3.6-alpine'
				}
			}
            steps {
				sh 'pip install -r requirements.txt'
				sh 'cd B7FunDjango'
				sh 'python manage.py runserver'
            }
        }
        stage('Test') {
			agent {
				docker {
					image 'python:3.6-alpine'
				}
			}
            steps {
				sh 'pip install -r requirements.txt'
				sh 'cd B7FunDjango'
                sh 'python manage.py test'
            }
        }
    }
}