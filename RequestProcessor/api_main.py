from flask import Flask, request, jsonify
import get_funnytime  
import plot_chatdata
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import io
from PIL import Image
import numpy as np
import base64
from io import BytesIO
import re

app = Flask(__name__)



@app.route('/process_video', methods=['POST'])
def process_video():
    print("POST REQUEST:", request.json)
    print("now processing...")

    content = request.json
    url = content['url']
    # YouTubeのビデオURLのパターン
    pattern = r'https?://www\.youtube\.com/watch\?v=[\w-]+'
    
    if not re.match(pattern, url):
        return jsonify({'funny_time_url': "Invalid URL"})
    video_id = url.split("=")[-1]
    # Process chat data
    get_funnytime.get_chatdata(video_id)
    # Generate url
    funny_time_url, minutes_since_start, counts_sorted = plot_chatdata.most_funnest_time(video_id)
    
    # Return the funny time URL
    return jsonify({'funny_time_url': funny_time_url})

@app.route('/analyze_video', methods=['POST'])
def analyze_video():
    print("POST REQUEST:", request.json)
    print("accepted analyze_video request")
    print("now processing...")
    # YouTubeのビデオURLのパターン
    pattern = r'https?://www\.youtube\.com/watch\?v=[\w-]+'
    
    if not re.match(pattern, url):
        return jsonify({'funny_time_url': "Invalid URL"})
    content = request.json
    url = content['url']
    video_id = url.split("=")[-1]
    # Process chat data
    get_funnytime.get_chatdata(video_id)
    # Generate url
    funny_time_url, minutes_since_start, counts_sorted = plot_chatdata.most_funnest_time(video_id)
    # Display graph in the future
    plot_chatdata.get_graph_data(minutes_since_start, counts_sorted, video_id)     
    response = {}
    # Encode the saved file
    with open("./image" + video_id + ".png", "rb") as f:
        img_base64 = base64.b64encode(f.read()).decode('utf-8')
    # Response
    response['image'] = img_base64
    
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False, threaded=False)
