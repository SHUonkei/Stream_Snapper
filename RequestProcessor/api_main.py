from flask import Flask, request, jsonify
import get_funnytime  
import plot_chatdata
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import io
import tqdm

app = Flask(__name__)

@app.route('/process_video', methods=['POST'])
def process_video():
    print("POST REQUEST:", request.json)
    print("now processing...")

    content = request.json
    url = content['url']
    video_id = url.split("=")[-1]
    # Process chat data

    get_funnytime.get_chatdata(video_id)
    
    # Generate url
    funny_time_url,minutes_since_start, counts_sorted = plot_chatdata.most_funnest_time(video_id)
    
    #後々グラフも表示したい
    #graph_data = plot_chatdata.get_graph_data(minutes_since_start, counts_sorted)     

    # Return the funny time URL and the placeholder for graph data
    return jsonify({'funny_time_url': funny_time_url, 'graph_data': "placeholder_for_graph_data"})

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False, threaded=False)
