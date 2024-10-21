from django.urls import path
from movie_app import views
urlpatterns = [
    path('Movies/', views.MoviesListCreateAPIView.as_view()),
    path('Movies/<int:id>', views.MoviesDatailAPIView.as_view()),

    path('directors/', views.DirectorsListAPIView.as_view()),
    path('directors/<int:id>', views.DirectorsDatailAPIView.as_view()),

    path('Review/', views.ReviewViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('Review/<int:id>', views.ReviewViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                         'delete': 'destroy'})),
]