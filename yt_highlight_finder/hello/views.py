from django.shortcuts import render

#HttpResponseというクラスをimport
#クライアントに送り返す内容を管理するクラス
from django.http import HttpResponse

from . import forms
from django.views.generic import TemplateView
from . import get_funnytime
from . import plot_chatdata
from asgiref.sync import sync_to_async

class FormView(TemplateView):
    # 初期変数定義
    def __init__(self):
        self.params = {"Message":"情報を入力してください。",
                       "form":forms.Contact_Form(),#forms ファイルから 'form'という値にインスタンスが設定される
                       }

    # GET時の処理を記載
    async def get(self,request):
        return render(request, "hello/formpage.html",context=self.params)

    # POST時の処理を記載
    async def post(self,request):
        if request.method == "POST":
            self.params["form"] = forms.Contact_Form(request.POST)
            
            
            
            # フォーム入力が有効な場合
            if self.params["form"].is_valid():
                self.params["Message"] = "入力情報が送信されました。"
                #urlが無効なとき（youtubeとかじゃないときの例外処理必要
                video_id = request.POST['Website'].split('/')[-1].split("=")[-1]
                
                await sync_to_async(get_funnytime.get_chatdata)(video_id)
                
                url_data = plot_chatdata.most_funnest_time(video_id)
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
    
