import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from collections import defaultdict

def most_funnest_time(video_id):
    #URLの末尾
#    video_id="IW2t52ps27s"
    textname=video_id+'.txt'
    # Given data
    with open(textname, 'r', encoding='utf-16') as file:
        data = file.read()

    timestamps = []
    for line in data.strip().split("\n"):
        #Parse
        date_str = line.split()[0]  # "2023-09-09"
        time_str = line.split()[1]  # "10:30:25"

        # 日付と時間の文字列を結合します
        datetime_str = date_str + " " + time_str  # "2023-09-09 10:30:25"

        # datetimeオブジェクトに変換します
        dt = datetime.strptime(datetime_str, "%Y-%m-%d %H:%M:%S")
        timestamps.append(dt)
    # Count messages per minute
    msg_counts = defaultdict(int)
    for timestamp in timestamps:
        # Round down to the nearest minute
        rounded_time = timestamp.replace(second=0)
        msg_counts[rounded_time] += 1


    # Sort by time for plotting
    times_sorted = sorted(msg_counts.keys())
    counts_sorted = [msg_counts[time] for time in times_sorted]
    start = times_sorted[0]

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
#    print("https://www.youtube.com/watch?v="+video_id+"#t="+str(int(minutes_since_start[max_commet_index])-1)+"m00s")
    
    return "https://www.youtube.com/watch?v="+video_id+"#t="+str(int(minutes_since_start[max_commet_index])-1)+"m00s"
    
    # Plot the results with adjusted x-axis
    # plt.figure(figsize=(10, 6))
    # plt.plot(minutes_since_start, counts_sorted, marker='o', linestyle='-')
    # plt.title("Number of Messages per Minute")
    # plt.xlabel("Minutes since start")
    # plt.ylabel("Message Count")
    # plt.grid(True)

    # plt.tight_layout()
    # plt.show()

