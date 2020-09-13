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
                    docker.build("sweety1995/budgetcalc:${env.BUILD_ID}")
                }
            }
       }
         stage('Push image - Docker Hub') {
            steps {
                script {
                    docker.withRegistry('https://registry.hub.docker.com', 'dockerhub1') {
                        docker.image("sweety1995/budgetcalc:${env.BUILD_ID}").push()
                        docker.image("sweety1995/budgetcalc:${env.BUILD_ID}").push("latest")
                    }
                }
            }
        }
      stage('Remove Unused docker image') 
        {
          steps
          {
	            sh "docker run --name budgetcalc -d -p 80:80 sweety1995/budgetcalc:${env.BUILD_ID}"
              sh "docker image prune -a -f"
          }
        }
      stage('Pushing artifacts to Artifactory') {
	    steps {
	        sh "zip -r buildArtifact${env.BUILD_ID}.zip dist"
                rtUpload (
                    serverId: 'artifactory',
                    spec: '''{
                        "files": [
                            {
                                "pattern": "buildArtifact*.zip",
                                "target": "budgetcalc/"
                            }
                        ]
                    }''',
                    buildName: "${env.JOB_NAME}",
                    buildNumber: "${env.BUILD_NUMBER}" 
                )
	    }
	}
    }
}
