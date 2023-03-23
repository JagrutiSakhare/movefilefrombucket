pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo "Running ${env.BUILD_ID} on ${env.JENKINS_URL}"
                 zip zipFile: 'test.zip', archive: false, exclude: 'Jenkinsfile, README.md'
            }
        }
    }
}
