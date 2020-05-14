pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        sh 'echo "Building"'
      }
    }

    stage('Test') {
      steps {
        sh 'echo "Testing"'
        sh 'ls'
        sh 'ls modules'
        sh 'ls modules/KicadParser'
      }
    }

  }
}
