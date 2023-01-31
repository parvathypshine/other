from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import Count
# Create your models here.


class MyUser(AbstractUser):
    phone=models.CharField(max_length=200)
    profile_pic=models.ImageField(upload_to="profilepics",null=True)




class Posts(models.Model):
    image=models.ImageField(null=True,upload_to="images",blank=True)
    user=models.ForeignKey(MyUser,on_delete=models.CASCADE)
    caption=models.CharField(max_length=500)
    like=models.ManyToManyField(MyUser,related_name="like")
    posted_date=models.DateTimeField(auto_now_add=True)

    @property
    def fetch_comments(self):
        comments=self.comments_set.all()
        
        return comments

    def __str__(self):
        return self.caption

    # @property
    # def fetch_likes(self):
    #     likes=self.likes_set.all().annotate(u_count=Count("like")).order_by("-u_count")
    #     return likes



class Comments(models.Model):
    comment=models.CharField(max_length=500)
    user=models.ForeignKey(MyUser,on_delete=models.CASCADE)
    post=models.ForeignKey(Posts,on_delete=models.CASCADE)
    posted_date=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.comment