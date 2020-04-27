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
		stage('Repository Fetch') {
			steps {
				checkout scm
			}
		}
        stage('Application Setup') {
            steps {
				withEnv(["HOME=${env.WORKSPACE}"]) {
					sh 'pip3 install -r requirements.txt --user'
					dir("B7FunDjango") {
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
						sh 'python manage.py '
					}
				}
			}
        }
    }
	post {
		always {
			dir("B7FunDjango") {
				junit 'test-reports/unittest/*.xml'
			}
		}
		failure{
			mail to: 'B7FunService@gmail.com',
			subject: "STARTED: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]'",
			body: """<p>STARTED: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]':</p>
              <p>Check console output at &QUOT;<a href='${env.BUILD_URL}'>${env.JOB_NAME} [${env.BUILD_NUMBER}]</a>&QUOT;</p>"""
		}
	}
}