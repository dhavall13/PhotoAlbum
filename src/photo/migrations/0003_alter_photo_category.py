# Generated by Django 3.2.4 on 2021-06-21 15:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0002_alter_photo_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='photo.category'),
        ),
    ]