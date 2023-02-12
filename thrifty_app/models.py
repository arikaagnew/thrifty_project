from django.db import models

# Create your models here.

def upload_path(instance,filename):
    return '/'.join(['images/',str(instance.title),filename])
class User(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

    def __str__(self):
        return (self.username)

class Post(models.Model):
    title = models.CharField(max_length=30)
    image = models.ImageField(blank=True, null=True, upload_to='images/')
    description = models.TextField()
    date_created = models.DateField(auto_now_add=True)
    is_claimed = models.BooleanField()
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='has_posts')
    
    def __str__(self):
        return (self.title)

    # def image(self):
    #     if self.image:
    #         return u'<img src="%s" width="50" height="50" />' % self.image.image
    #     else:
    #         return '(Sin imagen)'