pipeline {
    agent any
    parameters {
        choice(
            name: 'TEST_ENV',
            choices: ['dev', 'test', 'prod'],
            description: '请选择测试环境'
        )
    }
    environment {
        TEST_ENV = "${params.TEST_ENV}"
    }
    stages {
        stage('Install dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run tests') {
            steps {
                sh 'pytest --alluredir=allure-results'
            }
        }
        stage('Allure Report') {
            steps {
                allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
            }
        }
    }
    post {
        always {
            archiveArtifacts artifacts: 'allure-results/**', fingerprint: true
        }
    }
} 