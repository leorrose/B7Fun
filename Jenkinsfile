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
				withEnv(["HOME=${env.WORKSPACE}"]) {
					sh 'sudo apt-get build-dep python-imaging'
					sh 'sudo apt-get install libjpeg62 libjpeg62-dev'
					sh 'pip install PIL'
					sh 'pip install -r requirements.txt'			
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
			sh 'echo Test ${BUILD_NUMBER} FAILURE'
		}
	}
}