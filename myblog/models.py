#all lines starting with from and import are pieces of code from other files so we don't have to copy and paste
from django.db import models
from django.utils import timezone
#Class means we are defining an object, Post is the name of our object. models.Model means it's a django model so it knows to save it to the database
class Post(models.Model):
#this defigns authors as a link to another model
  author = models.ForeignKey('auth.User')
#this defines title as a list of characters with a max length of 200
  title = models.CharField(max_length=200)
#This defines texts as a limitless text field for comments and blog posts  
  text = models.TextField()
#this is the date and time
  published_date = models.DateTimeField(
  blank=True, null=True)
#self is referring to the class post. So the published date will equal the current time and then it will save it self. 
  def publish(self):
    self.published_date = timezone.now()
    self.save()
#self is refering to the class post. So it will return the current instance of the post's title
  def __str__(self):
    return self.title
