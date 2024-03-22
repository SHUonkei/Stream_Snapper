#api
import requests

#env
import os
from dotenv import load_dotenv

# .envファイルの内容を読み込見込む
load_dotenv('../../.env')

def urlGetRequest(data):
    #環境変数に変える
    url = os.environ['API_URL']
    response = requests.post(url, json=data)
    print(url," statuscode: ",response.status_code)
    
    return response.json()
