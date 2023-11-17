
from django.contrib import admin
from django.urls import path

from healthapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('get/', views.getData),
    #path('post/', views.postData),
    path('get/', views.getData),
    path('post/', views.postData), 
    path('data/<int:pk>/', views.DataAPIView.as_view()),
    path('data/<int:pk>/', views.dataDetails.as_view()),
    path('generic/data/<int:id>/', views.GenericAPIView.as_view()),
]
