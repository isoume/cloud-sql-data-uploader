pipeline {
    agent any

    stages {
        stage('createEnvironment'){
            steps{
                sh """
                    sudo gcloud compute ssh worker-data-processing-dev --zone=europe-west1-b --project=doctolib-data-dev --command="mkdir -p /home/doctolib_upload_data"
                """
            }
        }
        stage('Deploy') {
            steps {
                sh """
                    echo 'copying the files *.py'
                    sudo gcloud compute scp ./*.py worker-data-processing-dev:/home/doctolib_upload_data --zone=europe-west1-b
                    echo 'copying the Dockerfile'
                    sudo gcloud compute scp Dockerfile worker-data-processing-dev:/home/doctolib_upload_data --zone=europe-west1-b
                    echo 'copying the requirements.txt'
                    sudo gcloud compute scp requirements.txt worker-data-processing-dev:/home/doctolib_upload_data --zone=europe-west1-b        
                    #sudo gcloud compute ssh worker-data-processing-dev --zone=europe-west1-b --project=doctolib-data-dev --command="pip install -r /home/doctolib_upload_data/requirements.txt"
                    #sudo gcloud compute ssh worker-data-processing-dev --zone=europe-west1-b --project=doctolib-data-dev --command="python3 /home/doctolib_upload_data/main.py &"
                """
            }
        }
    }
}