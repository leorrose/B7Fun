pipeline {
    agent {
		docker {
			image 'leorrose13/python-pillow-alpine:jenkins'
		}
	}
	triggers {
        githubPush()
    }
	options {
		skipDefaultCheckout(true)
        timeout(time: 60, unit: 'MINUTES')
    }
    stages {
        stage('Install Application Dependencies') {
            steps {
				withEnv(["HOME=${env.WORKSPACE}"]) {
					sh 'pip3 install -r requirements.txt --user'
				}
            }
        }
		stage('Run Migrations') {
            steps {
				dir("B7FunDjango") {
					withEnv(["HOME=${env.WORKSPACE}"]) {
						sh 'python manage.py makemigrations'
						sh 'python manage.py migrate'
					}
				}
			}
        }
        stage('Run Tests') {
            steps {
				dir("B7FunDjango") {
					withEnv(["HOME=${env.WORKSPACE}"]) {
						sh 'python manage.py test accounts.tests.test_apps'
						junit 'test-reports/unittest/*.xml'
					}
				}
				deleteDir()
			}
        }
    }
}