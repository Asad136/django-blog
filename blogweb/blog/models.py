from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)    


    def __str__(self):
        return self.title
    

class Comment(models.Model):
    blog = models.ForeignKey(Blog,related_name='comments',on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

def __str__(self):
        return f'Comment by {self.user} on {self.blog}'
