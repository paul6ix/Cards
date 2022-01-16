from django.db import models
from io import BytesIO
from PIL import Image
from django.core.files import File
from django.conf import settings


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.slug}/'


class Card(models.Model):
    category = models.ForeignKey(Category, related_name='cards', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = models.SlugField
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='uploads', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads', blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_created',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'{self.category.slug}/{self.slug}/'

    def get_image(self):
        if self.image:
            return settings.LOCAL_HOST_URL + self.image.url
        return ''

    def get_thumbnail(self):
        if self.thumbnail:
            return settings.LOCAL_HOST_URL + self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()
                return settings.LOCAL_HOST_URL + self.thumbnail.url
            else:
                return ''

    # Function to create thumbnail
    def make_thumbnail(self, image, size=(300, 200)):
        # Open the image
        img = Image.open(image)
        # converted it to RGB color mode
        img.convert('RGB')
        # Gave it a default size
        img.thumbnail(size)
        # Stream to locally
        thumb_io = BytesIO
        # saving the image
        img.save(thumb_io, 'JPEG', quality=85)
        # updating the thumbnail
        thumbnail = File(thumb_io, name=image.name)
        return thumbnail
