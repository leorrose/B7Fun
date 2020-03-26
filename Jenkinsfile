pipeline {
    agent {
		docker {
			image 'python:3.6-alpine'
		}
	}
	triggers {
        cron('H * * * *')
    }
	options {
        timeout(time: 30, unit: 'MINUTES')
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
				def testsError = null
				try {
					dir("B7FunDjango") {
						withEnv(["HOME=${env.WORKSPACE}"]) {
							sh 'python manage.py test'
						}
					}
					catch(err) {
						testsError = err
						currentBuild.result = 'FAILURE'
					}
					finally {
						junit 'reports/junit.xml'

						if (testsError) {
							throw testsError
						}
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
			mail to:"B7FunService@gmail.com", subject:"SUCCESS: ${currentBuild.fullDisplayName}", body: "Test ${BUILD_NUMBER} SUCCESS"
		}
		failure {
			mail to:"B7FunService@gmail.com", subject:"FAILURE: ${currentBuild.fullDisplayName}", body: "Test ${BUILD_NUMBER} FAILURE"
		}
	}
}