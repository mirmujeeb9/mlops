pipeline {
    agent any

    stages {
        stage('Cloning repository') {
            steps {
                git branch: 'main', url: 'https://github.com/faizan2ahmed/MLOPs_Faizan.git'
            }
        }
        
        stage('Installation of dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Execution of test.py') {
            steps {
                bat 'python test.py'
            }
        }

        stage('Deploying') {
            steps {
                script {
                    def branchName = env.GIT_BRANCH.substring(env.GIT_BRANCH.lastIndexOf('/') + 1)
                    echo "Branch name: ${branchName}"
                    if (branchName == 'main') {
                        echo 'Deploying to production'
                    } else {
                        echo 'Deploying to UAT'
                    }
                }
            }
        }
    }
}
