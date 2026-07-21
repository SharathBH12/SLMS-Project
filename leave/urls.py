from django.urls import path
from leave import views


urlpatterns=[
    path('apply_leave/',views.apply_leave,name='apply_leave'),
    path('my_leaves/',views.my_leaves,name='my_leaves'),
    path('view_leave/',views.view_leave,name='view_leave'),
    path('approve_leave/<int:id>/',views.approve_leave,name='approve_leave'),
    path('reject_leave/<int:id>/',views.reject_leave,name='reject_leave')
]