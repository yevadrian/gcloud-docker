### Upload remote files to Google Cloud Storage with Google Cloud SDK on Docker

##### Modify "key.json" according to your Google service account credentials
> nano key.json

##### Create Google Cloud SDK container with Docker Compose
> sudo docker compose up

##### Install required Python packages
> sudo docker exec -it gcloud sh -c "pip install google-cloud-storage && pip install wget"

##### Run the script to upload a remote file
> sudo docker exec -it gcloud sh -c "python3 main.py [URL] [FILENAME] [BUCKET]"

##### Example command
> sudo docker exec -it gcloud sh -c "python3 main.py https://engage.mitre.org/wp-content/uploads/2022/02/EngageHandbook.pdf mitre-engage-handbook.pdf data-fellowship-8-yevadrian"
