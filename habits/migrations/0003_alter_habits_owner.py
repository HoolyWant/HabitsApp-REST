# Generated by Django 4.2.7 on 2023-11-06 14:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('habits', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habits',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='habits', to=settings.AUTH_USER_MODEL, verbose_name='владелец'),
        ),
    ]
