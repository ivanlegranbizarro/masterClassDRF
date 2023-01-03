from django.contrib.auth.models import User
from django.core.validators import MaxLengthValidator, MinLengthValidator
from django.db import models
from django.utils.text import slugify

# Create your models here.


class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(TimeStampedModel):
    name = models.CharField(max_length=20, validators=[MinLengthValidator(3)])
    slug = models.SlugField(max_length=20, unique=True, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
            super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Post(TimeStampedModel):
    title = models.CharField(max_length=100, validators=[
                             MinLengthValidator(3)])
    content = models.TextField(
        validators=[MinLengthValidator(10), MaxLengthValidator(1000)])
    files = models.FileField(upload_to='uploads/posts/', blank=True, null=True)
    image = models.ImageField(
        upload_to='uploads/posts/', blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, null=True, blank=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title
