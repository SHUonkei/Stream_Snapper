import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "yt_highlight_finder.settings")  # プロジェクト名に応じて変更
import django
django.setup()
from hello.models import Hello  # アプリ名に応じて変更
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

def processRequests():
    # .envファイルの内容を読み込見込む
    load_dotenv('./.env')

    #スプシからリクエストを読み取り、apiをたたき、動画一覧に書き込む.

    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

    credentials = ServiceAccountCredentials.from_json_keyfile_name('./app/hello/config.json', scope)
    gc = gspread.authorize(credentials)

    SPREAD_SHEET_KEY= os.environ['API_KEY']
    CSV_FILENAME = "./request.csv"
    SHEET_NAME='request'
    TARGET_SHEET_NAME='動画一覧'
    workbook = gc.open_by_key(SPREAD_SHEET_KEY)
    worksheet = workbook.worksheet(SHEET_NAME)

    data_list = []

    i = 0
    while True:
        i += 1
        #get url
        Val = worksheet.acell('C'+str(i)).value
        if Val == None: break
        data = {'url': Val}
        
        # 行iの1列目から10列目までを空にする
        for j in range(1,6):
            worksheet.update_cell(i, j, "")   
        #apiをたたく
        responsejson = utils.urlGetRequest(data)
        targetUrl = responsejson.get('funny_time_url', 'URLの取得に失敗しました')
        
        #スプシに登録
        ws = workbook.worksheet(TARGET_SHEET_NAME)
        last_row =len(ws.col_values(1))
        next_row = last_row + 1
        videoInfo = Video.getInfo(Val)
        items = [videoInfo["channel"]["name"],videoInfo["title"],Val,targetUrl,videoInfo["id"]]
        ws.append_row(items , table_range='A'+str(next_row))
        
        #sqlight の　databaseに登録
        new_record = Hello()
        total_records = Hello.objects.count()
        new_record.videoid = total_records
        new_record.title = videoInfo["title"]
        new_record.author = videoInfo["channel"]["name"]
        new_record.url = targetUrl
        new_record.video = videoInfo["id"]        
        new_record.tag = ""
        data_list.append(new_record)

    Hello.objects.bulk_create(data_list)

processRequests()





# with open(CSV_FILENAME, 'w', newline='') as csvFile:
#     writer = csv.writer(csvFile)
#     writer.writerows(worksheet.get_all_values())

# # 空のリストを作成
#hello_list = []
# with open('./request.csv',encoding='utf-8') as f:
#     reader = csv.reader(f)
#     id_num = 1000
#     for row in reader:
        # new_hello = Hello()
        # new_hello.videoid = id_num
        # id_num += 1
        # new_hello.title = row[1]
        # new_hello.author = row[0]
        # new_hello.url = row[3]
        # print(row[3])
        # new_hello.video = row[4]        
        # new_hello.tag = row[-1]
        # print(row)
        # hello_list.append(new_hello)

# # bulk_createを使用して一括保存
# Hello.objects.bulk_create(hello_list)