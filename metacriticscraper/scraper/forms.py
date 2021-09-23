from django import forms


class metaURL(forms.Form):
    meta_url = forms.CharField(label='metaurl', max_length=100000)
