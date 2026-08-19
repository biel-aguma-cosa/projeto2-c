from django.contrib import admin
from django.urls import path, include

import appointments.views as views

app_name = 'appointments'

urlpatterns = [
    path('list/'         , views.list_view       , name='list' ),
    path('view/<int:id>/', views.view_appointment, name='view' ),
    path(''              , views.index           , name='index'),
]