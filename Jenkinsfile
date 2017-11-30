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
                sh 'python -m unittest -v PythonTheRide/testsParser.py'
		sh 'python -m unittest -v PythonTheRide/testsRoutingCalculator.py'
            }
        }
    }
}
