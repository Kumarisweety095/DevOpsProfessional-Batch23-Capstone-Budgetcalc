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
                    sh "${scannerHome}/bin/sonar-scanner \
  -Dsonar.projectKey=BudgetCalc \
  -Dsonar.sources=. \
  -Dsonar.host.url=http://34.125.103.99 \
  -Dsonar.login=f73447f452aa401f0b2874e789432571d60ff751"
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
      stage('Remove Unused docker image') 
        {
          steps
          {
              sh "docker image prune -a -f"
          }
     	}
      stage('Deploy-docker-swarm') {
        steps{
           sh 'sudo docker service create sweety1995/budgetcalc:latest'        }
        }
   }
}
