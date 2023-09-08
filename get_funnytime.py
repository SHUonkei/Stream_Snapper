import pytchat
import time

# PytchatCoreオブジェクトの取得
livechat = pytchat.create(video_id="IW2t52ps27s")
while livechat.is_alive():

    # チャットデータの取得
    chatdata = livechat.get()
    for c in chatdata.items:
        output_string = f"{c.datetime} {c.author.name} {c.message} {c.amountString}"
        # エラーハンドリングを追加
        safe_output = output_string.encode('cp932', errors='replace').decode('cp932')
        if "草" in safe_output or "w" in safe_output or "藁" in safe_output or "笑" in safe_output:
            print(safe_output)

    time.sleep(0.1)
