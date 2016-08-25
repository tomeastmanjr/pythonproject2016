from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^add$', views.add, name="add"),
    url(r'^create$', views.create, name="create"),
    url(r'^show$', views.show, name="show"),
    url(r'^update$', views.update, name="update"),
    url(r'^test$', views.test, name="test"),
    url(r'^about$', views.about, name="about"),
    url(r'^contact$', views.contact, name="contact")
    ]
