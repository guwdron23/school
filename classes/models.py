from django.db import models

class Classes(models.Model):
    number = models.IntegerField(verbose_name='Номер класса')
    title = models.CharField(max_length=1, verbose_name='Класс')

