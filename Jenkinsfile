pipeline {
     agent any
     stages {
         stage('Build') {
             steps {
                 sh './run_docker.sh'
                 sh 'echo "Docker setup done"'
                 sh 'docker ps'
             }
         }
         stage('Lint Python App') {
              steps {
                  sudo make install
                  sh 'pylint --disable=C,E app.py'
              }
         }

         stage('master branch as prod, known to work') {
            when {
                  branch 'master' 
              }
              steps {
                  withAWS(region:'us-east-2') {
            		  s3Upload(pathStyleAccessEnabled: true, payloadSigningEnabled: true, path:'P5_Capstone/', includePathPattern:'**/*', bucket:'nathan-udacity-pipeline')
            		  sh 'python3 app.py'
            			}
              }
         }

        stage('Dev') {
            when {
                branch 'dev'
              }                
              steps {
                  withAWS(region:'us-east-2') {
                  sh 'echo "Uploading original html file to S3"'
                  //s3Upload(pathStyleAccessEnabled: true, payloadSigningEnabled: true, path:'P5_Capstone/', file:'index.html', bucket:'nathan-udacity-pipeline')
                  }
              }
         }
     }
}
