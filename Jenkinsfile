pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        sh 'echo "Building"'
        sh './jenkins/build.sh'
      }
    }

    stage('Test') {
      steps {
        sh 'echo "Testing"'
        sh 'ls'
        sh 'ls module'
        sh 'ls module/KicadParser'
        sh './jenkins/test.sh'
      }
    }

  }
}
