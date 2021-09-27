from . import views
from django.urls import path

app_name = "redditscraper"

urlpatterns = [
    path("",views.index2, name="index2"),
    path("reddit",views.red_scraper, name = "redditscraper"),
    path("get_queries",views.get_queries, name = "get_queries")
    #path('/meta', views.get_url, name = "metaurl")
]
