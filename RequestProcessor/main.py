import get_funnytime as get_funnytime
import plot_chatdata as plot_chatdata
url = "https://www.youtube.com/watch?v=vSm-ug1ss7Y"
videoid = url.split("=")[-1]
get_funnytime.get_chatdata(videoid)
print(plot_chatdata.most_funnest_time(videoid))

