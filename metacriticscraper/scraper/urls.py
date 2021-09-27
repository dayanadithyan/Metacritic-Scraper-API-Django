from django.urls import path

from . import views

app_name  = "scraper"

urlpatterns = [
    path("",views.index,name="index"),
    path("meta",views.scraper, name = "scraper"),
    path("get_url",views.get_url, name = "get_url")
    #path('/meta', views.get_url, name = "metaurl")
]
