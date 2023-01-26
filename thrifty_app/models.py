from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

    def __str__(self):
        return (self.username)

class Post(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    date_created = models.DateField()
    is_claimed = models.BooleanField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return (self.title, self.description, self.date_created, self.is_claimed)