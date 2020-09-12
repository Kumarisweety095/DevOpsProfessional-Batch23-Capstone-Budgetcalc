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
  -Dsonar.host.url=http://35.202.8.179:8080 \
  -Dsonar.login=4f605276085c89f9a19a4b10e78aebeb9fc9d148"
                }
            }
        }
       stage('Docker Build') {
            steps {
                script {
                    docker.build("budgetcalc:${env.BUILD_ID}")
                }
            }
        }      
    }
}
