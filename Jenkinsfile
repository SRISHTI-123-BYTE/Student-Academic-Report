pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Checking out Student Academic Report project from GitHub...'
            }
        }

        stage('Generate Academic Report') {
            steps {
                bat 'python app.py'
            }
        }

        stage('Archive Report') {
            steps {
                archiveArtifacts artifacts: 'academic_report.txt',
                                  fingerprint: true
            }
        }

    }
}