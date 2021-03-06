from django.conf.urls import url, include
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
    url(r'^random_number_list/$', views.gen_number_list, name='gen_number_list'),
    url(r'^random_word_from_text/$', views.get_random_word_from_text, name='get_random_word_from_text'),
    url(r'^random_password/$', views.gen_random_password, name="gen_random_password"),
    url(r'^random_password_list/$', views.gen_random_password_list, name="gen_random_password_list"),
    url(r'^execution/$', views.execution, name="execution"),
    url(r'^requests/all$', views.requests_story_all, name="requests_all"),
    url(r'^requests/current$', views.requests_story_current, name="requests_current"),
    url(r'^statistics/$', views.statistics, name="statistics"),

    url(r'^oauth/', include('social_django.urls', namespace='social')),  # <--
    url(r'^didnotguess/', views.index, name='index')
]