pipeline {
    agent any
    parameters {
        string(name: 'HOST', defaultValue: '10.38.0.3', description: 'Server')
        string(name: 'API_PASSWORD', description: 'API_PASSWORD')
        string(name: 'DATA_BASE_NAME', description: 'DATA_BASE_NAME')
        string(name: 'PROJECT_ID', description: 'PROJECT_ID')
        string(name: 'VM_NAME', description: 'VM_NAME')
        string(name: 'VM_ZONE', description: 'VM_ZONE')
    }

    stages {
        stage('createEnvironment'){
            steps{
                sh """
                    sudo gcloud compute ssh ${VM_NAME} --zone=${VM_ZONE} --project=${PROJECT_ID} --command="mkdir -p /home/data_folder_upload_data"
                """
            }
        }
        stage('Deploy') {
            steps {
                sh """
                    echo 'copying the files *.py'
                    sudo gcloud compute scp ./*.py ${VM_NAME}:/home/data_folder_upload_data --zone=${VM_ZONE}
                    echo 'copying the Dockerfile'
                    sudo gcloud compute scp Dockerfile ${VM_NAME}:/home/data_folder_upload_data --zone=${VM_ZONE}
                    echo 'copying the requirements.txt'
                    sudo gcloud compute scp requirements.txt ${VM_NAME}:/home/data_folder_upload_data --zone=${VM_ZONE}      
                    #sudo gcloud compute ssh ${VM_NAME} --zone=${VM_ZONE} --project=${PROJECT_ID} --command="pip install -r /home/data_folder_upload_data/requirements.txt"
                    #sudo gcloud compute ssh ${VM_NAME} --zone=${VM_ZONE} --project=${PROJECT_ID} --command="python3 /home/data_folder_upload_data/main.py &"
                """
            }
        }
    }
}