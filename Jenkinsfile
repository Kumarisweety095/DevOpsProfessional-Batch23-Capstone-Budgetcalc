pipeline {
    agent { label 'master'}
    tools { nodejs "nodejs" }
    stages {
      stage('Stop Privious Containers') {
                   sh "Docker swarm leave --force"
            sh "Docker stop '${docker ps -aq}'"
            echo "Docker container stopped"
            sh "Docker rm '${docker ps -aq}'"
            echo "Docker container removed"
      }
    }
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
      stage('Testing'){
        steps {
          script {
            sh "docker run --name budgetcalc${env.BUILD_ID} -d -p 80:80 sweety1995/budgetcalc:${env.BUILD_ID}"
            sh "google-chrome-stable --headless --disable-gpu"
		        sh "pytest -v -s --html=test_result_${env.BUILD_ID}.html Test/Test.py"
            sh "docker container stop budgetcalc${env.BUILD_ID}"
            echo "Docker container stopped"
            sh "docker container rm budgetcalc${env.BUILD_ID}"
            echo "Docker container removed"
            mail bcc: '', body: 'Testing Successfully', cc: '', from: '', replyTo: '', 
        subject: 'Testing Completed Successfully' , to: 'manojbaradhwaj@gmail.com'
            }
         }
      }
      stage('Push image - Docker Hub') {
          steps {
            script {
                      docker.withRegistry('https://registry.hub.docker.com', 'dockerhub1')
                    {
                          docker.image("sweety1995/budgetcalc:${env.BUILD_ID}").push("latest")
                                          
                    }
                } 
            }
        }
      stage('Deploy-docker-swarm') {
        steps{
           sh 'docker stack deploy --prune --compose-file docker-compose.yml budgetCalc'   
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
