pipeline {
    agent any
    stages {
        stage('Running Unit Tests') {
            steps {
                sh "bash test.sh"
            }
        }
        // stage('Installing dependencies') {
        //     steps {
        //         sh "bash scripts/dependencies.sh"
        //     }
        // }
        stage ('Build and push images') {
            environment {
                DOCKER_UNAME = credentials('docker_uname')
                DOCKER_PWORD = credentials('docker_pword')
            }
            steps {
                sh "docker-compose build --parallel"
                sh "docker login -u $DOCKER_UNAME -p $DOCKER_PWORD"
                sh "docker-compose push"
            }
        // }
        // stage ('Run ansible tasks') {
        //     steps {
        //         sh "ansible-playbook -i ansible/inventory.yaml ansible/playbook.yaml"
        //     }
        // }
        stage ('Deploy') {
            steps {
                // sh "bash scripts/deploy.sh"
                sh "scp -i ~/.ssh/ansible_id_rsa docker-compose.yaml swarm-manager:/home/jenkins/docker-compose.yaml"
                sh "scp -i ~/.ssh/ansible_id_rsa nginx.conf swarm-manager:/home/jenkins/nginx.conf"
                sh "ansible-playbook -i ansible/inventory.yaml ansible/playbook.yaml"
            }
        }
    }
}