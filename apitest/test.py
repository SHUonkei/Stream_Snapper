import requests

def post_test(data):
    url = "http://127.0.0.1:5000/process_video"
    response = requests.post(url, json=data)
    print("statuscode: ",response.status_code)
    
    return response.json()


data = {'url': 'https://www.youtube.com/watch?v=L2y7a_zMi20'}
response = post_test(data)
print(response)