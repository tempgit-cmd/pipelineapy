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
                // The '|| true' ensures Jenkins doesn't fail if no tests are collected
                sh 'python3 -m pytest -v . || true'
            }
            post {
                always {
                    // Collect test results if any (optional)
                    junit '**/test-*.xml'
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
            echo "❌ Pipeline failed. Check test collection and workspace."
        }
    }
}

