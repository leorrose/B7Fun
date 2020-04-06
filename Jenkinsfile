pipeline {
    agent {
		docker {
			image 'leorrose13/python-alpine-pillow:tagname'
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
				withEnv(["HOME=${env.WORKSPACE}"]) {
					sh 'python3 -m pip install --upgrade pip'
					sh 'python3 -m pip install --upgrade Pillow'
					sh 'pip install -r requirements.txt --user'
				}
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
			mail to: 'B7FunService@gmail.com',
			subject: "Failed Pipline: Test ${BUILD_NUMBER} Failure",
			body: "Failed Pipline: Test ${BUILD_NUMBER} Failure"
		}
	}
}