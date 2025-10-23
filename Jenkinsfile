pipeline {
    agent any
    stages {
        stage("Build Docker image") {
            steps {
                echo "Build Docker image"
                bat "docker build -t  password-generator:v1 ."
            }
        }
        stage("Docker Login") {
            steps {
                bat "docker login -u lakshyabandi25 -p Lakshya.bandi"
            }
        }
        stage("push Docker image to docker hub") {
            steps {
                echo "push Docker image to docker hub"
                bat "docker tag password-generator:v1 lakshyabandi25/case_study:t2"
                bat "docker push lakshyabandi25/case_study:t2"
            }
        }
        stage("Deploy to kubernetes") {
            steps {
                echo "Deploy to kubernetes"
                bat "kubectl apply -f deployment.yaml --validate=false"
                bat "kubectl apply -f service.yaml"
            }
        }
    }
    post {
        success {
            echo "Pipeline executed successfully"
        }
        failure {
            echo "pipeline failed. Please check the logs"
        }
    }
}
