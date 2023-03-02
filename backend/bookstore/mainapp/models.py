from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator

# Create your models here.

class Publisher(models.Model):
    brand_name = models.CharField(max_length=70)
    img_cap = models.ImageField(upload_to='cover',null=True)

    def __str__(self):
        return self.brand_name

class Author(models.Model):
    name = models.CharField(max_length=70)
    pfp = models.ImageField(upload_to='pfp',null=True)
    brief = models.TextField(max_length=200,null=True)
    about = models.TextField(max_length=500)
    rating = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Book(models.Model):
    GENRE_CHOICES = (
        ('Fiction','Fiction'),
        ('Novel','Novel'),
        ('History','History'),
        ('Biography','Biography'),
        ('Autobiography','Autobiography'),
        ('Self-help','Self-help'),
        ('Poetry','Poetry'),
        ('Romance','Romance'),
        ('Religious','Religious'),
    )
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=700)
    cover = models.ImageField(upload_to='cover',null=True)
    genre = models.CharField(max_length=20,choices=GENRE_CHOICES,null=True)
    year = models.IntegerField()
    nbr_pages = models.IntegerField()
    price = models.DecimalField(max_digits=15,decimal_places=2,default=00.00)
    rating = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title