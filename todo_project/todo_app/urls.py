from django.contrib.admin import views
from django.urls import path
from.import views

urlpatterns = [

    path('',views.funct,name='funct'),
    # path('details',views.details,name='details'),
    path('delete<int:taskid>/',views.delete,name='delete'),
    path('edit<int:id>/',views.edit,name='edit'),
    path('list/',views.tasklistview.as_view(),name='list'),
    path('d/<int:pk>/',views.detail.as_view(),name='d'),
    path('up/<int:pk>/', views.update.as_view(), name='up'),
    path('dt/<int:pk>/', views.delet.as_view(), name='dt'),

]
