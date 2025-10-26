from django.db import models
from django.core.validators import MinLengthValidator
# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}: {self.email}"

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.name
    
class Post(models.Model):
    title = models.CharField(max_length=80)
    excerpt = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True , related_name="posts")
    slug = models.SlugField(default="", null=False, db_index=True)
    content = models.TextField(validators=[MinLengthValidator(20)])
    date = models.DateField(auto_now=True)
    image_name = models.CharField(max_length=100)
    tag = models.ManyToManyField(Tag , related_name="posts")
    
    