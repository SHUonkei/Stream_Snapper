import requests
#env
import os
from dotenv import load_dotenv

# .envファイルの内容を読み込見込む
load_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env'))

def post_test(data):
    url = os.environ['API_URL']
    response = requests.post(url, json=data)
    print("statuscode: ",response.status_code)
    
    return response.json()


data = {'url': 'https://www.youtube.com/watch?v=L2y7a_zMi20'}
response = post_test(data)
print(response)