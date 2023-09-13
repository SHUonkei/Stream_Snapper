from django.shortcuts import render

#HttpResponseというクラスをimport
#クライアントに送り返す内容を管理するクラス
from django.http import HttpResponse

from . import forms
from django.views.generic import TemplateView
from . import get_funnytime
from . import plot_chatdata
#from asgiref.sync import sync_to_async

class FormView(TemplateView):
    # 初期変数定義
    def __init__(self):
        self.params = {"Message":"情報を入力してください。",
                       "form":forms.Contact_Form(),#forms ファイルから 'form'という値にインスタンスが設定される
                       }

    # GET時の処理を記載
    def get(self,request):
        return render(request, "hello/formpage.html",context=self.params)

    # POST時の処理を記載
    def post(self,request):
        if request.method == "POST":
            self.params["form"] = forms.Contact_Form(request.POST)
            
            
            
            # フォーム入力が有効な場合
            if self.params["form"].is_valid():
                self.params["Message"] = "入力情報が送信されました。"
                #urlが無効なとき（youtubeとかじゃないときの例外処理必要
                
                video_id = request.POST['Website'].split('/')[-1].split("=")[-1]
                
                import pytchat
                import time

                livechat = pytchat.create(video_id=video_id)

                print(video_id)
                f = open(video_id+'.txt', 'x', encoding='utf-16')
                while livechat.is_alive():

                    # チャットデータの取得
                    chatdata = livechat.get()
                    for c in chatdata.items:
                        output_string = f"{c.datetime} {c.author.name} {c.message} {c.amountString}"
                        # エラーハンドリングを追加
                        safe_output = output_string.encode('cp932', errors='replace').decode('cp932')
                        if "草" in safe_output or "w" in safe_output or "藁" in safe_output or "笑" in safe_output:
                            f.write(safe_output+"\n")

                    time.sleep(0.1)

                f.close()
                print("----------------------------")
                import matplotlib.pyplot as plt
                from datetime import datetime, timedelta
                from collections import defaultdict

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
                    
                url_data = "https://www.youtube.com/watch?v="+video_id+"#t="+str(int(minutes_since_start[max_commet_index])-1)+"m00s"
                    

                
                
#                url_data = get_funnytime.get_chatdata(video_id)
                
#                url_data = await plot_chatdata.most_funnest_time(video_id)
                self.params["url_data"] = url_data

        return render(request, "hello/formpage.html",context=self.params)

def index(request):
    #render でレンダリングしてる
    #変数とかなんか使う場合はここで置き換えて表示させる
    #render の返り値は TemplateResponseというクラスのインスタンス
    #
    
    params = {
        'title':"this is title parameter",
        'msg':"this is a page for testing",
        'goto':'next',
    }
    
    return render(request, 'hello/index.html',params)


def next(request):
    params = {
        'title':"next"
        ,'msg':"this is next page"
        ,'goto':'index',
    }
    return render(request, 'hello/index.html',params)




#ビュー関数
#クライアントからのHTTPリクエストを受け取り、
#それに対するHTTPレスポンスを返す役割
#ここでのrequestは、クライアントからのリクエスト情報を保持するオブジェクト

#リクエストが来たらする処理をかく
#requestはHttpRequestクラスのインスタンス
#クライアントからサーバーにアクセスする際の様々な情報をまとめて管理している
#対になる概念がHttpResponse
#もちろんクエリパラメータもその中に入っているので、dict形式で取得できる GETが辞書

# def index(request,id,nickname):
    #クエリパラメータをつかう　?id=1&name= みたいなところ 
    # if 'msg' in request.GET:
    #     msg = request.GET['msg']
    #     result = HttpResponse('You Typed: "'+msg+'".')
    # else:
    #     result = "please send msg parameter!"
    # return HttpResponse(result)
    
    # result = 'your id:' + str(id) + ', name: "' + nickname + '".'
    # return HttpResponse(result)
    
