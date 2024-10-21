from collections import OrderedDict
from rest_framework.decorators import api_view
from rest_framework.response import Response
from movie_app.models import Directors, Movie, Review
from movie_app.serializers import DirectorsSerializer, MovieSerializer, ReviewSerializer
from rest_framework import status, viewsets
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    lookup_field = 'id'
    pagination_class = PageNumberPagination


class CustomPagination(PageNumberPagination):
    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('total', self.page.paginator.count),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('results', data)

        ]))


class DirectorsDatailAPIView(ListCreateAPIView):
    queryset = Directors.objects.all()
    serializer_class = DirectorsSerializer
    lookup_field = 'id'


class DirectorsListAPIView(ListCreateAPIView):
    queryset = Directors.objects.all()
    serializer_class = DirectorsSerializer
    pagination_class = CustomPagination


class MoviesDatailAPIView(ListCreateAPIView):
    queryset = (Movie.objects.select_related('directors')
                .prefetch_related('review').all()
    serializer_class = MovieSerializer

    def post(self, request):
        try:
            movie_app = Directors.objects.get(id=id)
        except Directors.DoesNotExist:
            return Response(data={'error': 'Post not found'},
                            status=status.HTTP_404_NOT_FOUND)
        data = DirectorsSerializerSerializer(instance=movie_app, many=False).data

        return Response(data=data)

class MoviesListCreateAPIView(ListCreateAPIView):
    queryset = (Movie.objects.select_related('directors')
                .prefetch_related('review').all()
    serializer_class = MovieSerializer

    def post(self, request):

        if request.method == 'GET':
            print(request.query_params)

            Movies = Movie.objects.all()

            data = MovieSerializer(instance=Movies, many=True).data

            return Response(data=data)

        elif request.method == 'POST':

            title = request.data.get('title')
            text = request.data.get('text')
            description = request.data.get('description')
            duration = request.data.get('duration')
            directors = request.data.get('directors')

            movie = Movie.objects.create(
                title=title,
                text=text,
                description=description,
                duration=duration,
                directors=directors
            )

            return Response(status=status.HTTP_201_CREATED,
                            data={'movie_id': movie.id})



# @api_view(http_method_names=['GET'])
# def Directors_list_api_view(request):
#     movie_app = Directors.objects.all()
#
#     data = DirectorsSerializer(instance=movie_app, many=True).data
#
#     return Response(data=data)

# @api_view(http_method_names=['GET'])
# def Director_detail_api_view(request, id):
#     try:
#         movie_app = Directors.objects.get(id=id)
#     except Directors.DoesNotExist:
#         return Response(data={'error': 'Post not found'},
#                         status=status.HTTP_404_NOT_FOUND)
#     data = DirectorsSerializerSerializer(instance=movie_app, many=False).data
#
#     return Response(data=data)
#
#
# # @api_view(http_method_names=['GET'])
# # def Movie_list_api_view(request):
# #     movie_app = Movie.objects.all()
# #
# #     data = MovieSerializer(instance=movie_app, many=True).data
# #
# #     return Response(data=data)
#
# @api_view(http_method_names=['GET'])
# def Movie_detail_api_view(request, id):
#     try:
#         movie_app = Movie.objects.get(id=id)
#     except Movie.DoesNotExist:
#         return Response(data={'error': 'Post not found'},
#                         status=status.HTTP_404_NOT_FOUND)
#     data = MovieSerializerSerializer(instance=movie_app, many=False).data
#
#     return Response(data=data)
#
#
# # @api_view(http_method_names=['GET'])
# # def Review_list_api_view(request):
# #     movie_app = Review.objects.all()
# #
# #     data = ReviewSerializer(instance=movie_app, many=True).data
# #
# #     return Response(data=data)
#
# @api_view(http_method_names=['GET'])
# def Review_detail_api_view(request, id):
#     try:
#         movie_app = Review.objects.get(id=id)
#     except Review.DoesNotExist:
#         return Response(data={'error': 'Post not found'},
#                         status=status.HTTP_404_NOT_FOUND)
#     data = ReviewSerializerSerializer(instance=movie_app, many=False).data
#
#     return Response(data=data)
#
# @api_view(http_method_names=['GET'])
# def Movie_Review_list_api_view(request):
#     movie_app = Review.objects.all()
#
#     data = Movie_Review_list_api_view_Sterializater(instance=movie_app, many=True).data
#
#     return Response(data=data)
#
# @api_view(http_method_names=['GET', 'POST'])
# def movie_list_create_api_view(request):
#
#     if request.method == 'GET':
#         print(request.query_params)
#
#         Movies = Movie.objects.all()
#
#         data = MovieSerializer(instance=Movies, many=True).data
#
#         return Response(data=data)
#
#     elif request.method == 'POST':
#
#         title = request.data.get('title')
#         text = request.data.get('text')
#         description = request.data.get('description')
#         duration = request.data.get('duration')
#         directors = request.data.get('directors')
#
#         movie = Movie.objects.create(
#             title=title,
#             text=text,
#             description=description,
#             duration=duration,
#             directors=directors
#         )
#
#         return Response(status=status.HTTP_201_CREATED,
#                         data={'movie_id': movie.id})


# @api_view(http_method_names=['GET', 'POST'])
# def directors_list_create_api_view(request):
#
#     if request.method == 'GET':
#         print(request.query_params)
#
#         Director = Directors.objects.all()
#
#         data = MovieSerializer(instance=Director, many=True).data
#
#         return Response(data=data)
#
#     elif request.method == 'POST':
#
#         name = request.data.get('name')
#
#         director = Movie.objects.create(
#             name=name
#         )
#
#         return Response(status=status.HTTP_201_CREATED,
#                         data={'director_id': director.id})
#
#
# @api_view(http_method_names=['GET', 'POST'])
# def review_list_create_api_view(request):
#
#     if request.method == 'GET':
#         print(request.query_params)
#
#         Review = Review.objects.all()
#
#         data = MovieSerializer(instance=Review, many=True).data
#
#         return Response(data=data)
#
#     elif request.method == 'POST':
#
#         text = request.data.get('text')
#         movie = request.data.get('movie')
#         stars = request.data.get('stars')
#
#         Review = Review.objects.create(
#             text=text,
#             movie=movie,
#             stars=stars
#         )
#
#         return Response(status=status.HTTP_201_CREATED,
#                         data={'review_id': Review.id})