from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Executor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=11)

    def __str__(self):
        return "User: {}, phone: {}".format(self.user, self.phone)
    
class Film(models.Model):
    title = models.CharField(max_length=50)
    ganre = models.CharField(max_length=50)
    description = models.CharField(max_length=2000)
    rating = models.FloatField()
    actors = models.CharField(max_length=300)
    url = models.URLField()
    directors = models.CharField(max_length=100)

    def __str__(self):
        return "title: {}, ganre: {}, description: {}, rating: {}, actors: {}, directors: {}".format(self.title, self.ganre, self.description, self.rating, self.actors, self.directors)



class Authoring(models.Model):
    author = models.CharField(max_length=50)
    password = models.CharField(max_length=50, default=True)
    
    def __str__(self):
        return 'Пользователь: {}'.format(self.author)