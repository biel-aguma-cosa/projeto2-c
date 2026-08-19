from django.contrib import admin
from django.urls import path, include

import users.views as views

app_name = 'users'

urlpatterns = [
    path('login'        , views.login_view    , name='login'       ),
    path('register'     , views.register_view , name='register'    ),
    path('logout'       , views.logout_view   , name='logout'      ),

    path('list'            , views.list_view     , name='list'        ),
    path('professional'    , views.prof_view     , name='professional'),
    path('edit_pr/<int:id>', views.prof_view     , name='professional'),

    path(''             , views.index_view    , name='index'       ),
]