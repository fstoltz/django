from django.db import models
from tinymce.models import HTMLField
# Create your models here.

LANG_CHOICES = (
	('en', 'EN'),
	('es', 'ES'),
)

class Article(models.Model):
	title = models.CharField(max_length=300)
	content = HTMLField()
	lang = models.CharField(max_length=20, choices=LANG_CHOICES, default='en')

	def __str__(self):
		return self.title


class MenuItem(models.Model):
	name = models.CharField(max_length=300)
	article_id = models.ForeignKey(Article, on_delete=models.CASCADE)
	display_order = models.IntegerField()
	lang = models.CharField(max_length=20, choices=LANG_CHOICES, default='en')

	def __str__(self):
		return self.name