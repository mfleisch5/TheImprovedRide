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
		sh 'cd TheImprovedRide'
		sh 'pip3 install -r requirements.txt'
                sh 'python3 -m unittest -v tests/testParser.py'
		sh 'python3 -m unittest -v tests/testRoutingCalculator.py'
            }
        }
    }
}
