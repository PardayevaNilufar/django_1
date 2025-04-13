from django.db import models

class Article(models.Model):
    title=models.CharField(max_length=250,null=False,blank=False)
    description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title