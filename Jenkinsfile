pipeline {
    agent {
		docker {
			image 'python:3.6-alpine'
		}
	}
    stages {
        stage('Install Application Dependencies') {
            steps {
				withEnv(["HOME=${env.WORKSPACE}"]) {
					sh 'pip install -r requirements.txt'
				}
            }
        }
        stage('Run Tests') {
            steps {
				dir("B7FunDjango") {
					sh 'python manage.py test'
				}
			}
        }
    }
}