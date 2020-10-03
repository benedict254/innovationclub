from django.db import models
from django.contrib.auth.models import User

"""class Role(models.Model):
    role_name = models.CharField(max_length=55)
    user = models.ManyToManyRel(User,on_delete=models.CASCADE,related_name='role')


class User_roles(models.Model):
    user_id = models.OneToManyRel(User,on_delete=models.CASCADE)

class Permission(models.Model):
    permission_name = models.CharField(max_length=55)
    user = models.ManyToManyRel(User,on_delete=models.CASCADE,related_name='permission_role')"""

class Event(models.Model):
    title = models.CharField(max_length=55)
    description = models.CharField(max_length=55)
    venue = models.CharField(max_length=55)
    facilitator = models.CharField(max_length=55)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(auto_now_add=True)
    #start_time = models.TimeField(auto_now_add=True)
   # end_time = models.TimeFieldField(auto_now_add=False)
    image = models.ImageField(upload_to='events_pics',default='logo.jpg')
    def __str__(self):
        return self.title


class Blogs(models.Model):
    username = models.OneToOneField(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=55)
    description = models.CharField(max_length=55)
    author = models.CharField(max_length=55)
    published = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    #start_time = models.TimeField(auto_now_add=True)
   # end_time = models.TimeFieldField(auto_now_add=False)
    image = models.ImageField(upload_to='blogs_pics')
    def __str__(self):
        return self.title


class Community(models.Model):
    chairperson = models.OneToOneField(User,on_delete=models.PROTECT)
    community_name = models.CharField(max_length=55)
    description = models.CharField(max_length=55)
    def __str__(self):
        return self.community_name


class User_community(models.Model):
    user = models.ManyToManyField(User)


class Project(models.Model):
    community = models.ManyToManyField(Community)
    project_name = models.CharField(max_length=55)
    description = models.TextField()
    image = models.ImageField(upload_to='project_pics')
    def __str__(self):
        return self.project_name



class ImageModel(models.Model):
    image = models.ImageField(upload_to='images')


class Article(models.Model):
    nid = models.IntegerField(default=0)
    headimage = models.ImageField(upload_to='images', blank=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100, blank=True)
    body = models.TextField()
    teaser = models.TextField('teaser', blank=True)



