pipeline {
    agent {
    kubernetes {
      yamlFile 'deploy_agent.yaml'
      defaultContainer 'docker'
    }
  }
  stages {
    stage('build docker image') {
      steps {
          sh 'docker buildx create  --driver kubernetes --name builder --node arm64node  --driver-opt replicas=1,nodeselector=kubernetes.io/arch=arm64 --use'
          sh 'docker buildx create --append --driver kubernetes --name builder --node amd64node  --driver-opt replicas=1,nodeselector=kubernetes.io/arch=amd64 --use'
          sh 'docker buildx build --platform linux/arm64,linux/amd64 --push -t ${IMAGEREPO}/arduino-webupdate .'

      }
    }

    stage('deploy on k8s') {
      steps {
        container(name: 'kubectl'){
          sh 'kubectl apply -f k8s/deploy_arduino-webupdate.yaml'
          sh 'kubectl rollout status deployment/arduino-webupdate --namespace=arduino-webupdate'
        }
      }
    }

  }

    environment {
      IMAGEREPO = 'registry.klucsik.fun'
        }
}