import pytchat
import time
import threading
import subprocess



# 使用例
# result = run_in_thread(pytchat.create, video_id=get_video_id)
def get_chatdata(get_video_id):
#    get_video_id="IW2t52ps27s"
    # PytchatCoreオブジェクトの取得
#    livechat = pytchat.create(video_id=get_video_id)
    video_id = get_video_id
    print("here is get_chatdata")
    
    result = subprocess.run(['python', 'run_pytchat.py', video_id], capture_output=True, text=True)
    
    time.sleep(500)
    print("end get_chatdata")

    chat_data = result.stdout
    
    print("this is chat_data")
    print(chat_data)
    return chat_data
