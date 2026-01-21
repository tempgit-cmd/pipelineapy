pipeline {
    agent any

    stages {
        stage('Verify Workspace') {
            steps {
                echo "Current directory:"
                sh 'pwd'
                echo "Listing files:"
                sh 'ls -la'
            }
        }

        stage('Install Dependencies') {
            steps {
                echo "Upgrading pip and installing pytest..."
                sh 'python3 -m pip install --upgrade pip --user'
                sh 'python3 -m pip install pytest --user'
            }
        }

        stage('Run Tests') {
            steps {
                echo "Running pytest from:"
                sh 'pwd'
                // Run pytest with verbose output
                sh 'python3 -m pytest -v'
            }
            post {
                always {
                    // Optional: collect test reports if you generate XML reports
                    echo "Tests completed"
                }
            }
        }
    }

    post {
        always {
            echo "Pipeline finished"
        }
        success {
            echo "✅ All stages completed successfully!"
        }
        failure {
            echo "❌ Pipeline failed. Check test results!"
        }
    }
}

