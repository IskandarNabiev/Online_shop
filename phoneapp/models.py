from django.db import models

from django.core import validators
from django.core.exceptions import ValidationError

from django.contrib.auth.models import User
# Create your models here.
class Bb(models.Model):
    title = models.CharField(max_length=50, verbose_name='Toвap',
                             validators=[validators.RegexValidator(regex='^.{4,}$')],
                             error_messages={'invalid': 'Неправильное название товара'})
    content = models.TextField(null=True, blank=True, verbose_name='Oпиcaниe')
    price = models.FloatField(null=True, blank=True, verbose_name='Цeнa')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')
    rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT, verbose_name='Рубрика')

    class Meta:
        verbose_name_plural = 'Объявления'
        verbose_name = 'Объявление'
        ordering = ['-published']
        # unique_together = ('title', 'published')



class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Рубрики'
        verbose_name = 'Рубрика'
        ordering = ['name']



# class AdvUser(models.Model):
#     is_activated = models.BooleanField(default=True)
#     user = models.OneToOneField(User, on_delete=models.CASCADE)