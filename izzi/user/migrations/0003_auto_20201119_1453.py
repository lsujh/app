# Generated by Django 3.1.3 on 2020-11-19 12:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20201119_1412'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ('-created',), 'verbose_name': 'Замовлення', 'verbose_name_plural': 'Замовлення'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ('-registration_date',), 'verbose_name': 'Користувач', 'verbose_name_plural': 'Користувачі'},
        ),
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.user', verbose_name='Користувач'),
        ),
    ]
