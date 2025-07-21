pipeline {
    agent any

    environment {
        PYTHON = 'Python3.10'
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/vaishnavipadwal/Python-CI-CD-project.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                dir('backend') {
                    sh '''
                        python3 -m venv venv
                        source venv/bin/activate
                        pip install -r requirements.txt
                    '''
                }
            }
        }

        stage('Run Tests') {
            steps {
                dir('backend') {
                    sh '''
                        source venv/bin/activate
                        python -m unittest || echo "No tests yet"
                    '''
                }
            }
        }

        stage('Lint') {
            steps {
                dir('backend') {
                    sh '''
                        source venv/bin/activate
                        pip install flake8
                        flake8 app.py
                    '''
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                dir('backend') {
                    sh 'docker build -t python-backend-app .'
                }
            }
        }

        stage('Success') {
            steps {
                echo "Pipeline complete!"
            }
        }
    }

    post {
        always {
            echo 'Done.'
        }
    }
}
