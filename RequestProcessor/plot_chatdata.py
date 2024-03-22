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
    
def get_graph_data(minutes_since_start, counts_sorted):
    
    fig, ax = plt.subplots()
    ax.figure(figsize=(10, 6))
    ax.plot(minutes_since_start, counts_sorted, marker='o', linestyle='-')
    ax.title("Number of Messages/min")
    ax.xlabel("Min")
    ax.ylabel("Message Count")
    ax.grid(True)

    ax.tight_layout()
    
    fig.canvas.draw()
    im = np.array(fig.canvas.renderer.buffer_rgba())
    # im = np.array(fig.canvas.renderer._renderer) # matplotlibが3.1より前の場合

    img = Image.fromarray(im)
    img.save("./image.jpg")


