from django.db import models
from django.urls import reverse



class Product(models.Model):
    title = models.CharField(max_length=150)
    brand = models.CharField(max_length=150, null=True)
    content = models.CharField(max_length=255, null=True)
    color = models.CharField(max_length=150, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='productImgs', null=True)
    url = models.SlugField(max_length=150, unique=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
# price ?????
    def __str__(self):
        return self.title

    class Category(models.Model):
        name = models.CharField(max_length=100, db_index=True)
        # name = models.CharField(max_length=150)
        # url = models.SlugField(max_length=150, unique=True)
        # created_at = models.DateTimeField(auto_now_add=True, null=True)
        # updated_at = models.DateTimeField(auto_now=True, null=True)
        def __str__(self):
            return self.name

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id':self.pk})
