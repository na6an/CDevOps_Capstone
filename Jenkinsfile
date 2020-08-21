pipeline {
     agent any
     stages {
         stage('Build & Give Permission') {
             steps {
                 sh './run_docker.sh'
                 sh 'echo "Docker setup done"'
                 sh 'docker ps'
                 //sh "./add_jenkins.sh"
             }
         }


         stage('Lint Python App') {
              steps {
                  //whersh 'sudo -S apt-get -y install pylint'
                  sh 'curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py'
                  sh 'sudo apt install python3-distutils'
                  sh 'python3 get-pip.py'
                  sh 'pip install pylint'
                  sh 'pylint --disable=C,E app.py'
              }
         }

         stage('master branch as prod, known to work') {
            when {
                  branch 'master' 
              }
              steps {
                  withAWS(region:'us-east-2') {
            		  s3Upload(pathStyleAccessEnabled: true, payloadSigningEnabled: true, path:'P5_Capstone/', includePathPattern:'**/*', bucket:'nathan-udacity-capstone')
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
