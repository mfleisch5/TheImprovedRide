pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'echo Build'
            }
        }
        stage('Test') {
            steps {
                sh 'echo Test'
		sh 'pip3 install -r TheImprovedRide/requirements.txt'
                sh 'python3 -m unittest -v TheImprovedRide/tests/testsParser.py'
		sh 'python3 -m unittest -v TheImprovedRide/tests//testRoutingCalculator.py'
            }
        }
    }
}
