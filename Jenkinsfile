pipeline {
    agent none
    stages {
        stage('Build') {
			agent {
				docker {
					image 'python:3.6.0'
				}
			}
            steps {
				sh "start installationWin.bat"
				sh "start runWin.bat"
            }
        }
        stage('Test') {
			agent {
				docker {
					image 'python:3.6.0'
				}
			}
            steps {
				sh "cd B7FunDjango"
                sh "python manage.py test"
            }
        }
    }
}