from django.conf.urls import url
from . import views

app_name = 'didnotguess'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login, name='login'),
    url(r'^loginuser/$', views.loginuser, name='loginuser'),
    url(r'^registration/$', views.registration, name='registration'),
    url(r'^registrationuser/$', views.registrationuser, name='registrationuser'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^random_number/$', views.gen_random_number, name='gen_random_number'),
    url(r'^random_number_list/$', views.gen_random_number_list, name='gen_random_number_list'),
    url(r'^random_word_from_text/$', views.get_random_word_from_text, name='get_random_word_from_text'),
    url(r'^random_password/$', views.gen_random_password, name="gen_random_password"),
    url(r'^random_password_list/$', views.gen_random_password_list, name="gen_random_password_list"),
    url(r'^execution/$', views.execution, name="execution"),
]