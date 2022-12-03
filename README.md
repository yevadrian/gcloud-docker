## Upload remote files to your Google Cloud Storage with Google Cloud SDK on Docker.

##### Modify "key.json" according to your Google service account credentials.
> nano key.json

##### Create Google Cloud SDK container with volume and environment.
> sudo docker run -itd -v ~/key.json:/key.json -v ~/main.py:/main.py -e GOOGLE_APPLICATION_CREDENTIALS:/key.json --name gcloud google/cloud-sdk

##### Install required Python packages.
> sudo docker exec -it gcloud sh -c "pip install --upgrade google-cloud-storage && pip install wget"

##### Run the script to upload a remote file.
> sudo docker exec -it gcloud sh -c "python3 main.py [URL] [FILENAME] [BUCKET]"

##### Example.
> sudo docker exec -it gcloud sh -c "python3 main.py https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.04162018.pdf nist-cybersecurity-framework.pdf data-fellowship-8-yevadrian"
