#api
import requests

#env
import os
from dotenv import load_dotenv
import numpy as np
import base64
from PIL import Image

# .envファイルの内容を読み込見込む
#rootの.envファイルを読み込む
load_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env'))

def urlGetRequest(data):
    #環境変数に変える
    print("urlGetRequest")
    url = os.environ['API_URL']
    response = requests.post(url, json=data)
    print(url," statuscode: ",response.status_code)
    
    return response.json()

def analyzeRequest(data):
    print("analyzeRequest")
    #環境変数に変える
    url = os.environ['API_URL_ANALYZE']
    response = requests.post(url, json=data)
    print(url," statuscode: ",response.status_code)
    
    return response.json()

