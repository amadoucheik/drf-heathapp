
from django.contrib import admin
from django.urls import include, path

from healthapp import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('data', views.DataViewSet, basename='data')

urlpatterns = [

    path('admin/', admin.site.urls),
    #path('get/', views.getData),
    #path('post/', views.postData),
    #path('viewset/', include(router.urls)),
    path('viewset/', include(router.urls)),
    path('get/', views.getData),
    path('post/', views.postData), 
    path('data/<int:pk>/', views.DataAPIView.as_view()),
    path('data/<int:pk>/', views.dataDetails.as_view()),
    path('generic/data/<int:id>/', views.GenericAPIView.as_view()),

]
