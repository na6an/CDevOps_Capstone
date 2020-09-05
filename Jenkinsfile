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
                  sh 'sudo apt-get -y install pylint'
                  //sh 'curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py'
                  //sh 'python3 get-pip.py'
                  //sh 'pip install python3-distutils'
                  //sh 'pip install pylint'
                  sh 'pylint --disable=C,E app.py'
              }
         }


         stage('master branch as dev') {
            when {
                  branch 'master' 
              }
              steps {
                  //withAWS(region:'us-east-2') {
            		  //s3Upload(pathStyleAccessEnabled: true, payloadSigningEnabled: true, path:'P5_Capstone/', includePathPattern:'**/
                  //', bucket:'nathan-udacity-capstone')
                  sh 'export AWS_CREDENTIAL_PROFILES_FILE=~/.aws/credentials'
                  sh './run_docker.sh'
                  //sh './upload_docker.sh'
            			//}
              }
         }

        stage('deployment') {
            when {
                branch 'deploy'
              }                
              steps {
                  //withAWS(region:'us-east-2') {
                  sh 'curl --silent --location "https://github.com/weaveworks/eksctl/releases/latest/download/eksctl_$(uname -s)_amd64.tar.gz" | tar xz -C /tmp' 
                  sh 'sudo mv /tmp/eksctl /usr/local/bin'
                  sh 'curl -LO "https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl"'
                  sh 'chmod +x ./kubectl'
                  sh 'sudo mv ./kubectl /usr/local/bin/kubectl'
                  sh 'kubectl version --client'
                  sh 'kubectl create cluster -f cluster.yaml'
                  sh 'kubectl create secret docker-registry regcred --docker-server="ttps://index.docker.io/v1/"  --docker-username=${username} --docker-password=${password} --docker-email=${email}'
                  sh 'kubectl apply -f stack.yaml'
                  sh 'kubectl delete daemonsets,replicasets,services,deployments,pods,rc,secrets --all'

                  //s3Upload(pathStyleAccessEnabled: true, payloadSigningEnabled: true, path:'P5_Capstone/', file:'index.html', bucket:'nathan-udacity-pipeline')
                  //}
              }
         }


     }
}
