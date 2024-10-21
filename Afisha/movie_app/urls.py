from django.urls import path
from movie_app import views
urlpatterns = [
    path('', views.movie_list_create_api_view),
    path('<int:id>/', views.Movie_detail_api_view),

    path('', views.directors_list_create_api_view),
    path('<int:id>/', views.Director_detail_api_view),

    path('directors/', views.DirectorsListAPIView()),
    path('directors/<int:id>', views.DirectorsDatailAPIView.as_view()),

    path('Review/', views.ReviewViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('Review/<int:id>', views.ReviewViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                         'delete': 'destroy'})),
]