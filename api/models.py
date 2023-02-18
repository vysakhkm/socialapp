from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title
    
    @property
    def post_comments(self):
        return Comments.objects.filter(Comment=self)

class Userprofile(models.Model):
    profile_pic=models.ImageField(upload_to="images",null=True)
    bio=models.CharField(max_length=300)
    time_line_pic=models.ImageField(upload_to="images",null=True)
    user=models.OneToOneField(User,on_delete=models.CASCADE)

class Comments(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    comment=models.CharField(max_length=400)
    post_name=models.ForeignKey(Post,on_delete=models.CASCADE)
    like=models.ManyToManyField(User,related_name="liked")

    @property
    def likes_count(self):
        return self.like.all().count()