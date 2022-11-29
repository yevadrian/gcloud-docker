#!/usr/bin/python3

from google.cloud import storage
import sys
import wget
import os

try:
    client = storage.Client()
    print('Connection to Google Cloud Success')
except:
    print('Connection to Google Cloud Failed')

filename = wget.download(sys.argv[1], sys.argv[2])
bucket = client.get_bucket(sys.argv[3])
blob = bucket.blob(sys.argv[2])
blob.upload_from_filename(os.getcwd()+'/'+sys.argv[2])
os.remove(filename)

print('\nFile Uploaded to Google Cloud')