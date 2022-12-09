from django.db import models
from django.forms import ValidationError
from .utils import validate_phone_namber


class Zavuch(models.Model):
    first_name = models.CharField(max_length=55, verbose_name='Имя')
    last_name = models.CharField(max_length=55, verbose_name='Фамилия')
    image = models.ImageField(upload_to='media/', blank=True, null=True, verbose_name='Фото завуча')
    phone = models.CharField(max_length=12, unique=True, validators=[validate_phone_namber], verbose_name='Номер телефона',
                             help_text='Номер должен быть на международном формате!')

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def save(self, *args, **kwargs):
        self.phone = self.phone.replace(' ', '')
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.first_name) + " " + str(self.last_name)

    class Meta:
        verbose_name = 'Завуч'
        verbose_name_plural = 'Завучи'