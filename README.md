# YT_Highlight_Finder
## file説明
- get_funnytime.py
    - 草、wといった盛り上がりのタイミングで現れる文字列を含むコメントのみを抽出
- plot_chatdata.py
    - get_funnttime.pyで取得したデータから、最も瞬間該当コメント数が多かったタイミングの一分前から再生が開始される動画URLを生成する
- yt_highlight_finder/master.py
    - データをデータベースのテーブルに挿入する
- 
- yt_highlight_finder/Template/App_Folder_HTML/video-list.html
    - http://127.0.0.1:8000/hello/video-list で表示されるhtml

## 準備
- install
```
pip install pytchat
pip install Django
pip install django-filter
```
- databaseのsetup
```
cd yt_highlight_finder
python manage.py migrate
python manage.py makemigrations hello
python manage.py sqlmigrate hello 0001
python manage.py migrate
python master.py
```

## サーバー起動
```
cd yt_highlight_finder
python manage.py runserver
```

## 使い方
- http://127.0.0.1:8000/hello/
  - このurlがメインページ
- http://127.0.0.1:8000/hello/video-list
  - このページに動画一覧が表示される。サムネイルをクリックすると、その動画の最も盛り上がった可能性の高いタイミングの少し前から再生が開始される。