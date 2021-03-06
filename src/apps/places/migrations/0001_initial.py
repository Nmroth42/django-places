# Generated by Django 3.1.3 on 2020-11-24 09:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Memory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55, verbose_name='Название места')),
                ('comment', models.TextField(max_length=55, verbose_name='Комментарий')),
                ('latitude', models.DecimalField(decimal_places=5, default=0.0, max_digits=10, verbose_name='Широта')),
                ('longitude', models.DecimalField(decimal_places=5, default=0.0, max_digits=10, verbose_name='Долгота')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='memories', to=settings.AUTH_USER_MODEL, verbose_name='Владелец')),
            ],
            options={
                'verbose_name': 'Воспоминание',
                'verbose_name_plural': 'Воспоминания',
                'ordering': ['-id'],
            },
        ),
    ]
