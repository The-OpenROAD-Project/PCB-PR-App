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
        sh 'ls module'
        sh 'ls module/KicadParser'
      }
    }

  }
}
