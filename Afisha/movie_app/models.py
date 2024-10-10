from django.db import models

class Directors(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name, self.movies

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.IntegerField()
    directors = models.ForeignKey(Directors, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

STARS = (
    (1, '*'),
    (2, '**'),
    (3, '***'),
    (4, '****'),
    (5, '*****'),
)

class Review(models.Model):
    text = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    stars = models.IntegerField(choices=STARS, default=0, null=True, blank=True)