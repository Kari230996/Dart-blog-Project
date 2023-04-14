from django.db import models
from django.urls import reverse
from django_ckeditor_5.fields import CKEditor5Field

# Create your models here.




class Article(models.Model):
    title=models.CharField('Title', max_length=200)
    text=CKEditor5Field('Text', config_name='extends')




class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, verbose_name='Url', unique=True)

    def __str__(self): 
        return self.title
    
    def get_absolute_url(self):
        return reverse('category', kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['title']



class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.CharField(max_length=50, verbose_name='Url', unique=True)

    def __str__(self): 
        return self.title
    
    def get_absolute_url(self):
        return reverse('tag', kwargs={"slug": self.slug})
    
    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
        ordering = ['title']

    

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, verbose_name='Url', unique=True)
    author = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Published')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    views = models.IntegerField(default=0, verbose_name='Views')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='posts')
    tags = models.ManyToManyField(Tag, blank=True, related_name='posts')


    def __str__(self): 
        return self.title

    
    def get_absolute_url(self):
        return reverse('post', kwargs={"slug": self.slug})
    
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['-created_at']


