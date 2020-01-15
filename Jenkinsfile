pipeline {
 agent { dockerfile {
   filename 'Dockerfile_python'
   //image 'python:3.7.2'
 //  args '--user root'
 } }
  stages {
//     stage('user_creation'){
//         steps{
//         sh 'useradd -r -u 1000 tmpuser'
//         sh 'su - tmpuser'
//         }
//     }

    stage('build') {
      steps {


        withEnv(["HOME=${env.WORKSPACE}"]) {
         sh 'echo $HOME'
         sh 'pip install --user -r requirements.txt'
        }
     }
    }

    stage('test'){
        steps{
            withEnv(["HOME=${env.WORKSPACE}"]) {
                sh '$HOME/.local/bin/pytest'
            }
        }
    }

    stage('ssh_inside_docker') {
        steps{
           sshagent (credentials: ['pegasus-ssh-credentials']) {
              withCredentials([string(credentialsId: 'pegasus-vm', variable: 'host')]) {
                    sh "ssh -o StrictHostKeyChecking=no -v piotr@" + host + " uptime"
              }
           }
        }
    }

    stage('publish') {
     when {
        branch 'master'
     }
     environment {
        GEMFURY_PUSH_URL = credentials('gemfury-access-url')
     }
     steps {
        sh './scripts/publish_to_gemfury.sh'
     }
    }

    stage('deploy-dev') {
     when {
        branch 'master'
     }
     steps {
        sh 'echo deploying to dev'
     }
    }

    stage('deploy-stage') {
     when {
        branch 'stage'
     }
     steps {
        sh 'echo deploying to stage'
     }
    }

    stage('deploy-production') {
     when {
        branch 'production'
     }
     steps {
        sh 'echo deploying to production'
     }
    }

  }
     post {
        always {
            sh "chmod -R 777 ."
            cleanWs()
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
