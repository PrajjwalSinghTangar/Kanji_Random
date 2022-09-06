from django.db import models

# Create your models here.
class Kanji(models.Model):
    kanji = models.CharField(max_length=12,null=True)
    meaning = models.CharField(max_length=48,null=True)
    story = models.CharField(max_length=256,null=True, blank=True)

    def __str__(self):
        return self.kanji