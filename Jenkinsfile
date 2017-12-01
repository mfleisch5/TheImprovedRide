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
		sh 'pip3 install -r PythonTheRide/requirements.txt'    
                sh 'python -m unittest -v testsParser'
		sh 'python -m unittest -v testsRoutingCalculator'
            }
        }
    }
}
