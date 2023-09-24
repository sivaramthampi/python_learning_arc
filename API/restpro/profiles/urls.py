
from django.urls import path
from .views import takeprofile,userpro

urlpatterns = [
    path("ser", takeprofile.as_view()),     ##if views's request is get then it calls get(), if put it calls put()
    path("ser/<str:key>", userpro.as_view())
]


