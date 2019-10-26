from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class Reviewer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(blank=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self):
        return f'Reviewer: {self.first_name}   {self.last_name}'


class Company(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    about_info = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'

    def __str__(self):
        return f'Company: {self.name}'


class Review(models.Model):
    title = models.CharField(max_length=64)
    rating = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])
    summary = models.CharField(max_length=10000)
    ip_address = models.GenericIPAddressField(auto_created=True)
    date = models.DateField(auto_now_add=True)
    reviewer = models.ForeignKey(Reviewer, on_delete=models.CASCADE, related_name='reviewer')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='company')

    class Meta:
        ordering = ('rating',)
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'

    def __str__(self):
        return f'Review: {self.title}  {self.reviewer}'

