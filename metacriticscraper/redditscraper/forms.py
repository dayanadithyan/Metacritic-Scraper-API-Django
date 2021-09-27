from django import forms


class RedditSearch(forms.Form):
    subreddits = forms.CharField(label='subreddits', max_length=10000000)
    queries = forms.CharField(label='queries', max_length=10000000)
