from django.db import models

# Create your models here.
class Bb(models.Model):
	title = models.CharField('Буква', max_length=1)
	content = models.TextField('Текст')

	class Meta:
		verbose_name = 'Что'
		verbose_name_plural = 'Чты'