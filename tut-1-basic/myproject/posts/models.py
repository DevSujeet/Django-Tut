from django.db import models

# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    slug = models.SlugField() # SlugField is a field for storing URL-friendly strings/ (_("slug"), max_length=200, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title