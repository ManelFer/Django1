
from django.urls import path
from blog import views


urlpatterns = [
    path('blog/', views.blog),
    path('exemplo/', views.exemplo),
]