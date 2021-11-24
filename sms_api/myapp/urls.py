from django.urls import path
from . import views

urlpatterns = [
    path('unitech-sms-api/<str:number>/<str:message>', views.smsAPI, name='unitech-sms-api'),
]