from movie_app import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/directors/', views.Directors_list_api_view),
    path('/api/v1/directors/<int:id', views.Director_detail_api_view),
    path('api/v1/movies/', views.Movie_list_api_view),
    path('/api/v1/movies/<int:id', views.Movie_detail_api_view),
    path('api/v1/reviews/', views.Review_list_api_view),
    path('/api/v1/reviews/<int:id', views.Review_detail_api_view)
]
