from django.db import models

class Teachers(models.Model):
    name = models.CharField(max_length=10, verbose_name='Имя')
    sur_name = models.CharField(max_length=15, verbose_name='Фамилия')
    geo = models.CharField(max_length=255, verbose_name='Место проживание')
    phone = models.CharField(max_length=12,
                             unique=True,
                             help_text='Номер должен содержать только цифры',
                             verbose_name='Телефон')

    @property
    def full_name(self):
        return f'{self.name} {self.sur_name}'

    def save(self, *args, **kwargs):
        self.phone = self.phone.replace(' ', '')
        super().save(*args,**kwargs)

    def __str__(self):
        return str(self.name) + '' + str(self.sur_name)

    class Meta:
        verbose_name = 'Учитель'
        verbose_name_plural = 'Учителя'


