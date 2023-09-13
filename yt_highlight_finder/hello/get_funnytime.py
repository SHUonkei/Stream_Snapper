import pytchat
import time
import threading

def run_in_thread(function, *args, **kwargs):
    result = []
    exception = []

    def wrapper():
        try:
            result.append(function(*args, **kwargs))
        except Exception as e:
            exception.append(e)

    thread = threading.Thread(target=wrapper)
    thread.start()
    thread.join()

    if exception:
        raise exception[0]
    return result[0]

# 使用例
# result = run_in_thread(pytchat.create, video_id=get_video_id)
def get_chatdata(get_video_id):
#    get_video_id="IW2t52ps27s"
    # PytchatCoreオブジェクトの取得
#    livechat = pytchat.create(video_id=get_video_id)
    livechat = run_in_thread(pytchat.create, video_id=get_video_id)
    f = open("./data/"+get_video_id+'.txt', 'x', encoding='utf-16')
    while livechat.is_alive():

        # チャットデータの取得
        chatdata = livechat.get()
        for c in chatdata.items:
            output_string = f"{c.datetime} {c.author.name} {c.message} {c.amountString}"
            # エラーハンドリングを追加
            safe_output = output_string.encode('cp932', errors='replace').decode('cp932')
            if "草" in safe_output or "w" in safe_output or "藁" in safe_output or "笑" in safe_output:
                f.write(safe_output+"\n")

        time.sleep(0.1)

    f.close()
