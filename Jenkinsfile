pipeline {
    agent any
    stages {
        stage('Running Unit Tests') {
            steps {
                sh "bash test.sh"
            }
        }
        // stage('Build and push images') {
        //     environment {
        //         DOCKER_UNAME = credentials('docker_uname')
        //         DOCKER_PWORD = credentials('docker_pword')
        //     }
        //     steps {
        //         sh "docker-compose build --parallel"
        //         sh "docker login -u $DOCKER_UNAME -p $DOCKER_PWORD"
        //         sh "docker-compose push"
        //     }
        // }
    }
}