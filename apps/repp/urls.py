from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^add_loan$', views.add_loan, name="add_loan"),
    url(r'^create$', views.create, name="create"),
    url(r'^show_loan$', views.show_loan, name="show_loan"),
    url(r'^update$', views.update, name="update"),
    url(r'^test$', views.test, name="test"),
    url(r'^about$', views.about, name="about"),
    url(r'^logout$', views.logout, name="logout")
    ]
