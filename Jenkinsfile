pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                bat '"C:\\Users\\nagra\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m pip install -r requirements.txt'
            }
        }

        stage('Install Playwright Browsers') {
            steps {
                bat '"C:\\Users\\nagra\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m playwright install'
            }
        }

        stage('Run Reporting Tests') {
            steps {
                bat '"C:\\Users\\nagra\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m pytest P2_ModuleWise_Tests/Test_P2.py -v --html=report.html --self-contained-html'
            }
        }
    }

    post {
    always {
        archiveArtifacts artifacts: 'report.html', fingerprint: true

        publishHTML([
            reportName: 'Automation Report',
            reportDir: '.',
            reportFiles: 'report.html',
            keepAll: true,
            alwaysLinkToLastBuild: true,
            allowMissing: false
               ])
       }
    }

    post {
    failure {
        mail to: 'golidivya770@gmail.com',
             subject: "Build Failed: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
             body: "Check Jenkins build: ${env.BUILD_URL}"
        }
    }
}