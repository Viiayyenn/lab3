pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                git branch: 'main', url: 'https://github.com/Viiayyenn/lab3.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    dockerImage = docker.build("game-flask-app")
                }
            }
        }

        stage('Run App') {
            steps {
                // Stop container cũ nếu đang chạy
                sh "docker rm -f game-container || true"

                // Chạy lại container mới
                sh "docker run -d -p 5000:5000 --name game-container game-flask-app"
            }
        }
    }
}
