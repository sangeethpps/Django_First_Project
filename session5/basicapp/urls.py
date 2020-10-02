from django.conf.urls import url
from basicapp import views

app_name = 'basicapp'

urlpatterns = [url(r'^register/$', views.register, name='register'),
               url(r'^login/$', views.user_login, name='login')]
