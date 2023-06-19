def SPACE = "/var/jenkins_home/workspace/submission-cicd-pipeline-anthonymax2000/.detaspace/bin/space"

docker.image('python:3.9').inside("-p 3000:3000"){
    stage("Checkout"){
        checkout scm
    }
    stage('Build'){
        withEnv(["HOME=${env.WORKSPACE}"]) {
            sh """
                python -m pip install --user -r ./app/requirements.txt
            """
            sh 'curl -fsSL https://deta.space/assets/space-cli.sh | sh'
        }
    }
    stage('Test'){
        withEnv(["HOME=${env.WORKSPACE}"]) {
            sh 'python -m unittest discover'
        }
    }
    stage('Manual Approval'){
        withEnv(["HOME=${env.WORKSPACE}"]) {
            sh """
                cd app
                chmod +x ./local_deploy.sh
                ./local_deploy.sh
                cd ..
            """
            input message: 'Lanjutkan ke tahap Deploy?'
        }
    }
    stage('Deploy'){
        withEnv(["HOME=${env.WORKSPACE}"]){
            sh """
                ${SPACE} link --id <<INSERT PROJECT ID HERE>>
                cd app
                cat <<INSERT TOKEN HERE>> | ${SPACE} login --with-token
                ls -la
                ${SPACE} push
            """
            sleep(time:1, unit:"MINUTES")
        }
    }
}