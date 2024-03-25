# Stream snapper 
## 説明
youtubeライブで盛り上がったシーンを自動抽出するアプリ. また, それらを共有するプラットフォームの開発も行った. 

## 紹介スライド
https://docs.google.com/presentation/d/1-x-z-yi8CvRIRrpr-fjHsA1q0IKzUEhoZpdMp1ldboE/edit#slide=id.g2c56f4f11e4_0_11

## 使い方
.env
init_db.csv
はサンプルを参照して作成してください.

```
pip install -r requirements.txt
```

init db

```
python app/manage.py migrate
```

初期データ
```
python app/init_db.py
```

## 起動

api

```
python RequestProcessor/api_main.py
```

django app

```
python app/manage.py runserver
```
