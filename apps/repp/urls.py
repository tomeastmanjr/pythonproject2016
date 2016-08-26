from django.conf.urls import url
from . import views
import re
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^add_loan$', views.add_loan, name="add_loan"),
    url(r'^show_loan/(?P<loan_id>\d+)$', views.show_loan, name="show_loan"),
    url(r'^create_loan$', views.create, name="create"),
    url(r'^update$', views.update, name="update"),
    url(r'^test$', views.test, name="test"),
    url(r'^about$', views.about, name="about"),
    url(r'^logout$', views.logout, name="logout"),
    url(r'^ryan_test$', views.ryan_test, name = "ryan_test")
    ]
