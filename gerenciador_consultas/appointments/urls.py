from django.contrib import admin
from django.urls import path, include

import appointments.views as views

app_name = 'appointments'

urlpatterns = [
    path('list/'         , views.list_view       , name='list'   ),
    path('list/me'       , views.my_list_view    , name='my_list'),
    path('view/<int:id>/', views.view_appointment, name='view'   ),

    path('register/'      , views.add_view       , name='add'   ),
    path('edit/<int:id>/' , views.edit_view      , name='edit'  ),
    path('del/<int:id>/<int:confirm>'  , views.delete_view    , name='delete'),
]