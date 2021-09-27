from django.shortcuts import render
from django.http import HttpResponse
from django import forms

import csv
import pandas as pd

from . import RedditScraper

from .forms import RedditSearch


# Create your views here.
def index2(request):
    
    return HttpResponse("Home")

def red_scraper(request):

    return render(request,"redditscraper/index.html")

def get_queries(request):

    # if this is a POST request we need to process the form data

    if request.method == 'POST':

        # create a form instance and populate it with data from the request:

        form = RedditSearch(request.POST)

        # check whether it's valid:

        if form.is_valid():

            subreds = form.cleaned_data['subreddits']
            subqueries = form.cleaned_data['queries']
            
            # process the data in form.cleaned_data as required
            ## the metacritic_scraper will run in here

            puller = RedditScraper.RedditScraper(subred=subreds,queries = subqueries)
            
            puller.run_scraper()

            
            #data = pd.read_csv('MetacriticReviews_.csv')

            #response = HttpResponse("File processed successfully!")

            #response['Content-Disposition'] = 'attachment; MetacriticReviews_.csv'

            #return response
        
        else:
            
            print(form.errors)

            return HttpResponse("Bad Request")