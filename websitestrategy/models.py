from django.db import models
from django.urls import reverse

# Create your models here.
class TypeNews(models.Model):
    typeNews = models.CharField(max_length=100,blank=True,null=True)

    def __str__(self):
        return self.typeNews

class Tags(models.Model):
    tag = models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.tag

class News(models.Model):
    typeNews = models.ForeignKey(TypeNews,on_delete=models.PROTECT)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    mainPage = models.BooleanField(blank=True,null=True)
    mainNews = models.BooleanField(blank=True,null=True)
    mainEvent = models.BooleanField(blank=True,null=True)
    header = models.CharField(max_length=255,blank=True,null=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True,null=True)
    photoForSlaider = models.ImageField(upload_to='photos/%Y/%m/%d/slaider/',blank=True,null=True)
    textSlaider = models.CharField(max_length=255,blank=True,null=True)
    shortText = models.TextField(blank=True,null=True)
    longText = models.TextField(blank=True,null=True)
    tag = models.ForeignKey(Tags, on_delete=models.PROTECT, blank=True,null=True)
    placeEvent = models.TextField(blank=True,null=True)
    hidden = models.BooleanField(blank=True,null=True)
    datetime = models.DateField(blank=True,null=True)

    def __str__(self):
        return self.header

    def get_absolute_url(self):
        return reverse('shownews', kwargs={'news_slug':self.slug})

class TagsChronic(models.Model):
    tag = models.CharField(max_length=100,blank=True,null=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.tag

class Chronic(models.Model):
    header = models.CharField(max_length=255,blank=True,null=True)
    shortText = models.TextField(blank=True,null=True)
    tag = models.ForeignKey(TagsChronic, on_delete=models.PROTECT, blank=True,null=True)
    photo = models.ImageField(upload_to='photos/chronic/%Y/%m/%d/',blank=True,null=True)
    datetime = models.DateField(blank=True,null=True)

    def __str__(self):
        return self.header


class TagsArticle(models.Model):
    tag = models.CharField(max_length=100,blank=True,null=True)

    def __str__(self):
        return self.tag

class Article(models.Model):
    header = models.CharField(max_length=255,blank=True,null=True)
    mainArticle = models.BooleanField(blank=True, null=True)
    shortText = models.TextField(blank=True,null=True)
    tag = models.ForeignKey(TagsArticle, on_delete=models.PROTECT, blank=True,null=True)
    photo = models.ImageField(upload_to='photos/article/%Y/%m/%d/',blank=True,null=True)
    datetime = models.DateField(blank=True,null=True)

    def __str__(self):
        return self.header