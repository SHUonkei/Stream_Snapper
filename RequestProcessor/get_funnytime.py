import pytchat
import time
import os

def get_chatdata(get_video_id):

    # PytchatCoreオブジェクトの取得
    livechat = pytchat.create(video_id=get_video_id, interruptable=False)
    
    print(type(livechat))
    print(livechat.is_alive)
    
    if os.path.isfile(get_video_id+'.txt'):
        return
    f = open(get_video_id+'.txt', 'x', encoding='utf-16')
    while livechat.is_alive():

        # チャットデータの取得
        chatdata = livechat.get()
        for c in chatdata.items:
            output_string = f"{c.datetime} {c.author.name} {c.message} {c.amountString}"
            # エラーハンドリングを追加
            safe_output = output_string.encode('cp932', errors='replace').decode('cp932')
            if "草" in safe_output or "w" in safe_output or "藁" in safe_output or "笑" in safe_output:
                f.write(safe_output+"\n")

#        time.sleep(0.01)

    f.close()
