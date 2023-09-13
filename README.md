# YT_Highlight_Finder
## file説明
- get_funnytime.py
    - 草、wといった盛り上がりのタイミングで現れる文字列を含むコメントのみを抽出
- plot_chatdata.py
    - get_funnttime.pyで取得したデータをグラフ化するとともに、最も瞬間該当コメント数が多かったタイミングの一分前から再生が開始される動画URLを生成する
- yt_highlight_finder/Template/App_Folder_HTML/formpage.html
    - 
## 準備
```
pip install pytchat
pip install yt-dlp
pip install Django
```

## サーバー起動
```
cd yt_highlight_finder
python manage.py runserver
```
