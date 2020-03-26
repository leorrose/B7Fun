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
}