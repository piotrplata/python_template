pipeline {
 agent { docker {
   image 'python:3.7.2'
   args '--user 0:0'
 } }
  stages {
    stage('build') {
      steps {


     //   withEnv(["HOME=${env.WORKSPACE}"]) {
         sh 'pip install --user -r requirements.txt'
      //  }
     }
    }

    stage('test'){
        steps{
           sh 'pytest'
        }
    }

    stage('deploy') {
     environment {
        GEMFURY_PUSH_URL = credentials('gemfury-access-url')
     }
     steps {
        sh './scripts/publish_to_gemfury.sh'
     }
    }
  }
}

node('master') {
 stage('ssh') {
         sshagent (credentials: ['pegasus-ssh-credentials']) {
           withCredentials([string(credentialsId: 'pegasus-vm', variable: 'host')]) {
                    sh "ssh -v piotr@" + host + " uptime"
           }

         }
    }
}
