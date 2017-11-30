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
                sh 'python -m unittest -v testsParser'
		sh 'python -m unittest -v testsRoutingCalculator'
            }
        }
    }
}
