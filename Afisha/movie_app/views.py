from rest_framework.decorators import api_view
from rest_framework.response import Response
from movie_app.models import Directors, Movie, Review
from movie_app.serializers import DirectorsSerializer, MovieSerializer, ReviewSerializer

@api_view(http_method_names=['GET'])
def Directors_list_api_view(request):
    movie_app = Directors.objects.all()

    data = DirectorsSerializer(instance=movie_app, many=True).data

    return Response(data=data)

@api_view(http_method_names=['GET'])
def Director_detail_api_view(request, id):
    try:
        movie_app = Directors.objects.get(id=id)
    except Directors.DoesNotExist:
        return Response(data={'error': 'Post not found'},
                        status=status.HTTP_404_NOT_FOUND)
    data = DirectorsSerializerSerializer(instance=movie_app, many=False).data

    return Response(data=data)


@api_view(http_method_names=['GET'])
def Movie_list_api_view(request):
    movie_app = Movie.objects.all()

    data = MovieSerializer(instance=movie_app, many=True).data

    return Response(data=data)

@api_view(http_method_names=['GET'])
def Movie_detail_api_view(request, id):
    try:
        movie_app = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(data={'error': 'Post not found'},
                        status=status.HTTP_404_NOT_FOUND)
    data = MovieSerializerSerializer(instance=movie_app, many=False).data

    return Response(data=data)


@api_view(http_method_names=['GET'])
def Review_list_api_view(request):
    movie_app = Movie.objects.all()

    data = ReviewSerializer(instance=movie_app, many=True).data

    return Response(data=data)

@api_view(http_method_names=['GET'])
def Review_detail_api_view(request, id):
    try:
        movie_app = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={'error': 'Post not found'},
                        status=status.HTTP_404_NOT_FOUND)
    data = ReviewSerializerSerializer(instance=movie_app, many=False).data

    return Response(data=data)