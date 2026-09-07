
from django.db import models

class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('frontend', 'Frontend'),
        ('backend', 'Backend'),
        ('devops', 'DevOps'),
        ('tools', 'Outils'),
    ]
    name = models.CharField(max_length=100, verbose_name='Competence')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    proficiency = models.PositiveIntegerField(default=80, help_text='0-100')

    class Meta:
        ordering = ['category', '-proficiency']

    def __str__(self):
        return self.name

class Experience(models.Model):
    title = models.CharField(max_length=200, verbose_name='Poste')
    company = models.CharField(max_length=200, verbose_name='Entreprise')
    location = models.CharField(max_length=200, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    current = models.BooleanField(default=False, verbose_name='En cours')
    description = models.TextField()

    class Meta:
        ordering = ['-start_date']

    def __str__(self):
        return f"{self.title} - {self.company}"

