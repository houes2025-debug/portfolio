
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Brouillon'),
        ('published', 'Publie'),
    ]
    title = models.CharField(max_length=200, verbose_name='Titre')
    slug = models.SlugField(unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(verbose_name='Contenu')
    excerpt = models.TextField(blank=True, max_length=500)
    image = models.ImageField(upload_to='blog/', blank=True)
    tags = models.CharField(max_length=255, blank=True, help_text='Separes par virgules')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug})
