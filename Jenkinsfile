pipeline {
    agent any

    environment {
        IMAGE_NAME = "sanjan2022bcs0194/wine-ml-model:v2"
        CONTAINER_NAME = "wine-lab7-container"
    }

    stages {

        stage('Pull Image') {
            steps {
                sh "docker pull ${IMAGE_NAME}"
            }
        }

        stage('Run Container') {
            steps {
                sh "docker run -d -p 8000:8000 --name ${CONTAINER_NAME} ${IMAGE_NAME}"
            }
        }

        stage('Wait for API Readiness') {
            steps {
                script {
                    timeout(time: 40, unit: 'SECONDS') {
                        waitUntil {
                            def response = sh(
                                script: "curl -s -o /dev/null -w \"%{http_code}\" http://localhost:8000/docs",
                                returnStdout: true
                            ).trim()
                            return response == "200"
                        }
                    }
                }
            }
        }

        stage('Valid Inference Test') {
            steps {
                script {
                    def response = sh(
                        script: '''
                        curl -s -X POST http://localhost:8000/predict \
                        -H "Content-Type: application/json" \
                        -d '{"fixed_acidity":7.4,"volatile_acidity":0.7,"citric_acid":0,"residual_sugar":1.9,"chlorides":0.076,"free_sulfur_dioxide":11,"total_sulfur_dioxide":34,"density":0.9978,"pH":3.51,"sulphates":0.56,"alcohol":9.4}'
                        ''',
                        returnStdout: true
                    )

                    echo "Valid Response: ${response}"

                    if (!response.contains("prediction")) {
                        error("Prediction field missing!")
                    }
                }
            }
        }

        stage('Invalid Inference Test') {
            steps {
                script {
                    def response = sh(
                        script: '''
                        curl -s -X POST http://localhost:8000/predict \
                        -H "Content-Type: application/json" \
                        -d '{"fixed_acidity":7.4}'
                        ''',
                        returnStdout: true
                    )

                    echo "Invalid Response: ${response}"

                    if (!response.contains("error")) {
                        error("Invalid input did not return error!")
                    }
                }
            }
        }

        stage('Stop Container') {
            steps {
                sh "docker rm -f ${CONTAINER_NAME}"
            }
        }
    }

    post {
        failure {
            echo "Pipeline FAILED - Model validation unsuccessful."
        }
        success {
            echo "Pipeline SUCCESS - Model validation passed."
        }
    }
}