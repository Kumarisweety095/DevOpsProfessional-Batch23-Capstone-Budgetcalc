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
                      docker.withRegistry('https://registry.hub.docker.com', 'dockerhub1')
                    {
                          docker.image("sweety1995/budgetcalc:${env.BUILD_ID}").push("latest")
                                          
                    }
                } 
            }
        }
      
            stage('Deploy-docker-swarm') {
        steps{
          sh 'docker compose leave'
          sh 'docker stack deploy --prune --compose-file docker-compose.yml budgetcalc'   
          
         
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
