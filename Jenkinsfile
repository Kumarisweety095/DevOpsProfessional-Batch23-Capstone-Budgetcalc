pipeline {
    agent { label 'master'}
    tools { nodejs "nodejs" }
    stages {
        stage('Build') {
            steps {
              sh 'npm cache clean --force'
          sh 'rm -rf node_modules package-lock.json'
	        sh 'npm install'
          sh 'npm update'
          sh 'npm install -g @angular/cli'
          sh 'npm install bulma'
          echo "Module installed"
          sh 'npm run build'    
            }
                }
      
       stage('SonarQube analysis') {
            environment {
                  scannerHome = tool 'SonarQube Scanner 2.8';
            }
            steps {
                withSonarQubeEnv('sonarqube') {
                 sh "${scannerHome}/bin/sonar-scanner"
                }
            }
        }
       stage('Docker Build') {
            steps {
                script {
                    docker.build("sweety1995/budgetcalc:${env.BUILD_ID}")
                    
                }
            }
        }
      
    }
  post { 
        always { 
          script{
            sh 'yes | docker image prune'
            cleanWs()
            echo "Dangled Images removed"
          }
        }
    }
}
