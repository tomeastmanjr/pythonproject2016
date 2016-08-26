from django.conf.urls import url
from . import views
import re
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^add$', views.add, name="add"),
    url(r'^create_loan/(?P<id>\d+)$', views.create, name="create"),
    url(r'^show$', views.show, name="show"),
    url(r'^update$', views.update, name="update"),
    url(r'^test$', views.test, name="test"),
    url(r'^about$', views.about, name="about"),
    url(r'^logout$', views.logout, name="logout"),
    url(r'^ryan_test$', views.ryan_test, name = "ryan_test")
    ]
