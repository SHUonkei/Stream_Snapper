from django import forms

#フォームクラス作成
class Contact_Form(forms.Form):
    Name = forms.CharField(label="名前")                    
    Tell = forms.IntegerField(label="電話番号")
    Mail = forms.EmailField(label="メールアドレス")
    Birthday = forms.DateField(label="生年月日")
    Website = forms.URLField(label="Webサイト")
    FreeText = forms.CharField(widget=forms.Textarea,label="備考")