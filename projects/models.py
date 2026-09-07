
from django.db import models
from django.urls import reverse

class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name='Titre')
    slug = models.SlugField(unique=True)
    description = models.TextField(verbose_name='Description')
    short_description = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='projects/', blank=True)
    tech_stack = models.CharField(max_length=255, help_text='Ex: Django, React, PostgreSQL')
    github_url = models.URLField(blank=True, verbose_name='GitHub')
    live_url = models.URLField(blank=True, verbose_name='Demo en ligne')
    featured = models.BooleanField(default=False, verbose_name='Mis en avant')
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-created_at']
        verbose_name = 'Projet'
        verbose_name_plural = 'Projets'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('project_detail', kwargs={'slug': self.slug})

