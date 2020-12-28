from django.contrib import admin
from django.urls import path

import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.index, name='index'),
    path('design', mainapp.design, name='design'),
    path('mobile_development', mainapp.mobile_development, name='mobile_development'),
    path('web_development', mainapp.web_development, name='web_development'),
    path('help_page', mainapp.help_page, name='help_page'),
]
