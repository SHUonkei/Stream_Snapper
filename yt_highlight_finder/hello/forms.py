from django import forms

#フォームクラス作成
class Contact_Form(forms.Form):
    Website = forms.URLField(label="Webサイト")
