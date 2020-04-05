pipeline {
    agent {
		docker {
			image 'python:3.6-alpine'
		}
	}
	triggers {
        githubPush()
    }
	options {
        timeout(time: 30, unit: 'MINUTES')
    }
    stages {
        stage('Install Application Dependencies') {
            steps {
				sh """
				pip install virtualenv
				virtualenv env
				virtualenv env
				.env/Scripts/activate
				pip install -r requirements.txt
				"""
            }
        }
        stage('Run Tests') {
            steps {
				dir("B7FunDjango") {
					withEnv(["HOME=${env.WORKSPACE}"]) {
						sh 'python manage.py test'
					}
				}
			}
        }
    }
	post {
		always {
			deleteDir()
		}
		success {
			sh 'echo Test ${BUILD_NUMBER} SUCCESS'
		}
		failure {
			sh 'echo Test ${BUILD_NUMBER} FAILURE'
		}
	}
}