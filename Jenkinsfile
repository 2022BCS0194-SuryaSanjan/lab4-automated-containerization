pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "sanjan2022bcs0194/wine-ml-model"
        DOCKER_TAG = "latest"
        NAME = "<Surya_Sanjan>"
        ROLLNO = "<2022BCS0194>"
    }

    stages {

        stage('Clone Repository') {
            steps {
                git branch: 'main',
                url: 'https://github.com/2022BCS0194-SuryaSanjan/lab4-automated-containerization.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t $DOCKER_IMAGE:$DOCKER_TAG .'
                }
            }
        }

        stage('Train Model') {
            steps {
                sh 'docker run --rm $DOCKER_IMAGE:$DOCKER_TAG python scripts/train.py'
            }
        }

        stage('Print Metrics + Student Info') {
            steps {
                sh '''
                echo "----------------------------------"
                echo "Model Evaluation Completed"
                echo "Student Name: $NAME"
                echo "Roll Number: $ROLLNO"
                echo "----------------------------------"
                '''
            }
        }

        stage('Push to DockerHub') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'USERNAME',
                    passwordVariable: 'PASSWORD'
                )]) {
                    sh '''
                    echo $PASSWORD | docker login -u $USERNAME --password-stdin
                    docker push $DOCKER_IMAGE:$DOCKER_TAG
                    '''
                }
            }
        }
    }
}
