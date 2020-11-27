from django.db import models


class User(models.Model):
    first_name = models.CharField("Ім'я", max_length=25)
    last_name = models.CharField('Прізвище', max_length=25)
    date_of_birth = models.DateField('Дата народження')
    registration_date = models.DateField('Дата реєстрації', auto_now_add=True)

    class Meta:
        verbose_name = 'Користувач'
        verbose_name_plural = 'Користувачі'
        ordering = ('-registration_date',)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Order(models.Model):
    user = models.OneToOneField(User, verbose_name='Користувач', on_delete=models.CASCADE, blank=True, null=True)
    created = models.DateTimeField('Дата створення замовлення', auto_now_add=True)
    product = models.CharField('Товар', max_length=50)

    class Meta:
        verbose_name = 'Замовлення'
        verbose_name_plural = 'Замовлення'
        ordering = ('-created',)

    def __str__(self):
        return self.product
