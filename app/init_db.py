import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "yt_highlight_finder.settings")  # プロジェクト名に応じて変更
import django
django.setup()
from stream_snapper.models import StreamSnapper  # アプリ名に応じて変更
import csv

import gspread
import json
from oauth2client.service_account import ServiceAccountCredentials 

#env
import os
from dotenv import load_dotenv

#api
import requests

import utils
from youtubesearchpython import *
from tqdm import tqdm

from pathlib import Path

def __init_db__():
    # 空のリストを作成
    stream_snapper_list = []
    INIT_DB_CSV_PATH = Path(__file__).resolve().parent / 'init_db.csv'
    is_file = os.path.isfile(INIT_DB_CSV_PATH)
    if not is_file:
        INIT_DB_CSV_PATH = Path(__file__).resolve().parent / 'sample.init_db.csv'
    with open(INIT_DB_CSV_PATH, encoding='utf-8') as f:
        reader = csv.reader(f)
        id_num = 1000
        for row in tqdm(reader):
            new_stream_snapper = StreamSnapper()
            new_stream_snapper.videoid = id_num
            id_num += 1
            new_stream_snapper.title = row[1]
            new_stream_snapper.author = row[0]
            new_stream_snapper.url = row[3]
            print(row[3])
            new_stream_snapper.video = row[4]        
            new_stream_snapper.tag = row[-1]
            print(row)
            stream_snapper_list.append(new_stream_snapper)

    # bulk_createを使用して一括保存
    StreamSnapper.objects.bulk_create(stream_snapper_list)
    
__init_db__()