from django.shortcuts import render

#HttpResponseというクラスをimport
#クライアントに送り返す内容を管理するクラス
from django.http import HttpResponse

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
    
    