from django.db import models

class BlogPost(models.Model):
    name = models.TextField(null=True)
    image = models.TextField(null=True)
    category = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)

    class Meta:
        db_table = 'posts'
# Create your models here.
