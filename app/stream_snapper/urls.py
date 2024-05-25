from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('next', views.next, name="next"),
    path('formpage', views.FormView.as_view(),name="formpage"),
    path('video-list', views.videoListView, name='videoListView'),
    path('GenerateUrl', views.generateUrlView.as_view(), name='GenerateUrl'),
    path('analyzeUrl', views.analyzeUrlView.as_view(), name='analyzeUrl'),
    ]


"勉強用メモ"
#一個上のディレクトリで、/stream_snapperにアクセスされた場合にこのファイルを読み込むようにurls.pyが設定されている

#以下のような書き方もできる
#結局、urlpatternsで<>でpassに書いたものは、viewsの関数で引き継ぐことができる
#＾ここにおいては＾/に本質的な意味はない
#path('<int:id>_<nickname>_<int:age>', views.index, name='index'),
#    path('<int:id>/<nickname>/', views.index, name='index'),

