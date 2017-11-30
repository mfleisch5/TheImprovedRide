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
		sh 'pip install -r PythonTheRide/requirements.txt'
                sh 'python3 -m unittest -v PythonTheRide/testsParser.py'
		sh 'python3 -m unittest -v PythonTheRide/testsRoutingCalculator.py'
            }
        }
    }
}
