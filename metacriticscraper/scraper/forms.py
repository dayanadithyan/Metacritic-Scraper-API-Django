from django import forms


class metaURL(forms.Form):
    metaurl = forms.CharField(label='metaurl', max_length=10000000)
    #meta_url = forms.URLField(label='metaurl', max_length=10000000)
