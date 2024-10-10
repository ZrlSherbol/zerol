from movie_app import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/directors/', views.directors_list_create_api_view),
    path('/api/v1/directors/<int:id', views.Director_detail_api_view),
    path('api/v1/movies/', views.movie_list_create_api_view),
    path('/api/v1/movies/<int:id', views.Movie_detail_api_view),
    path('api/v1/reviews/', views.review_list_create_api_view),
    path('/api/v1/reviews/<int:id', views.Review_detail_api_view),
    path('/api/v1/movies/reviews/', views.Movie_Review_list_api_view)
]
