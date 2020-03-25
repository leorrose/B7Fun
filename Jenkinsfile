pipeline {
    agent none
    stages {
		agent {
			docker {
				image 'python:3'
			}
		}
        stage('Build') {
            steps {
				sh "start installationWin.bat"
				sh "start runWin.bat"
            }
        }
        stage('Test') {
            steps {
				sh "cd B7FunDjango"
                sh "python manage.py test"
            }
        }
    }
}