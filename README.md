## Upload remote files to your Google Cloud Storage.

##### Create a json file containing your service account credentials as "key.json" in your current working directory.

##### Save the Python script "main.py" to your current working directory. 
> wget https://raw.githubusercontent.com/yevadrian/gcloud_docker/main/main.py

##### Create Google Cloud SDK container with volume mapping:
> sudo docker run -itd -v ~/key.json:/key.json -v ~/main.py:/main.py --name gcloud google/cloud-sdk

##### Enter the container's terminal:
> sudo docker exec -it gcloud sh

##### Provide service account credentials to the environment variable:
> export GOOGLE_APPLICATION_CREDENTIALS=/key.json

##### Install required Python packages:
> pip install --upgrade google-cloud-storage && pip install wget

##### Run the script to upload a remote file:
> python3 main.py [URL] [FILENAME] [BUCKET]

##### Example:
> python3 main.py https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.04162018.pdf nist-cybersecurity-framework data-fellowship-8-yevadrian
