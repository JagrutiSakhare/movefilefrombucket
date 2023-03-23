pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo "Running ${env.BUILD_ID} on ${env.JENKINS_URL}"
                 zip zipFile: 'test.zip', archive: false, exclude: 'Jenkinsfile, README.md'
            }
        }
		stage ('Terraform Execution') {
			steps {
				echo "Terraform Execution start"
				sh ('terraform init')
				sh ('terraform plan')
				sh ('terraform apply –auto-approve')
			}
		}
	}
}