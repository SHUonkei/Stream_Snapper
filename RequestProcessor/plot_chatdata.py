import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from collections import defaultdict
import numpy as np
from PIL import Image



def most_funnest_time(video_id):
    #URLの末尾
    textname=video_id+'.txt'
    #data
    with open(textname, 'r', encoding='utf-16') as file:
        data = file.read()
    timestamps = []
    
    
    for line in data.strip().split("\n"):
        #Parse
        date_str = line.split()[0]  # "2023-09-09"
        time_str = line.split()[1]  # "10:30:25"

        # 日付と時間の文字列を結合
        datetime_str = date_str + " " + time_str  # "2023-09-09 10:30:25"

        # datetimeオブジェクトに変換
        dt = datetime.strptime(datetime_str, "%Y-%m-%d %H:%M:%S")
        timestamps.append(dt)
    
    #time -> msg 
    msg_counts = defaultdict(int)
    
    for timestamp in timestamps:
        # Round down to the nearest minute
        rounded_time = timestamp.replace(second=0)
        msg_counts[rounded_time] += 1
        
    times_sorted = sorted(msg_counts.keys())
    counts_sorted = [msg_counts[time] for time in times_sorted]
    start = times_sorted[0]
    print(start)
    
    #日付超えるとやばいのか。。。
    # Calculate minutes since start for each timestamp

    minutes_since_start = [(time - start).seconds / 60 for time in times_sorted]

    max_commet_num = 0
    max_commet_index = 0
    for i in range(len(counts_sorted)):
        if max_commet_num < counts_sorted[i]:
            max_commet_index = i
            max_commet_num = counts_sorted[i]

    #最も盛り上がったタイミング-1分からスタート
    # #t=◯m◯s

    return "https://www.youtube.com/watch?v="+video_id+"#t="+str(int(minutes_since_start[max_commet_index])-1)+"m00s",minutes_since_start,counts_sorted
    
def get_graph_data(minutes_since_start, counts_sorted, video_id):
    # seaborn-poster スタイルを適用
    plt.style.use('seaborn-v0_8-dark')
    # グラフのサイズと解像度を設定
    fig, ax = plt.subplots(figsize=(10, 6), dpi=100)
    
    # プロットする際に線のスタイルと色を指定
    ax.plot(minutes_since_start, counts_sorted, marker='o', linestyle='-', color='royalblue', markersize=5, linewidth=2)
    
    # タイトルと軸ラベルの設定、フォントサイズの調整
    ax.set_title("Number of Messages per Minute", fontsize=14, fontweight='bold')
    ax.set_xlabel("Minutes Since Start", fontsize=12)
    ax.set_ylabel("Message Count", fontsize=12)
    
    # 軸の目盛りのフォントサイズ
    ax.tick_params(axis='both', which='major', labelsize=10)
    
    # グリッドを表示
    ax.grid(True, which='both', linestyle='--', linewidth=0.5, color='gray')
    
    # グラフのレイアウトを整える
    plt.tight_layout()
    
    # グラフを描画してNumPy配列に変換
    fig.canvas.draw()
    im = np.array(fig.canvas.renderer.buffer_rgba())
    
    # PIL.Imageオブジェクトに変換し、ファイルに保存
    img = Image.fromarray(im)
    img.save("./image" + video_id + ".png")

