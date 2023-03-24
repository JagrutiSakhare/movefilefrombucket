pipeline {
    //agent any
	agent {
        docker { image 'hashicorp/terraform:latest' }
    }
    stages {
        stage('Build') {
            steps {
                echo "Running ${env.BUILD_ID} on ${env.JENKINS_URL}"
                 //zip zipFile: 'test.zip', archive: false, exclude: 'Jenkinsfile, README.md'
            }
        }
		stage ('Terraform Execution') {
			steps {
				echo "Terraform Execution start"
				sh ('terraform init')
				echo "Terraform Init Completed"
				sh ('terraform plan')
				echo "Terraform Plan Completed"
				sh ('terraform apply –auto-approve')
				echo "Terraform Apply Completed"
			}
		}
	}
}