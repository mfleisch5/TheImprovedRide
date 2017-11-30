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
		sh 'pip3 install py3-ortools'
		sh 'pip3 install pandas'
		sh 'pip3 install geopy'
		sh 'pip3 install flask'
                sh 'python3 -m unittest -v PythonTheRide/testsParser.py'
		sh 'python3 -m unittest -v PythonTheRide/testsRoutingCalculator.py'
            }
        }
    }
}
