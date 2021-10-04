# Generated by Django 3.2.7 on 2021-10-04 18:23

from django.db import migrations, models
import images.validators


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='url',
            field=models.FileField(upload_to='images/', validators=[images.validators.validate_file_type]),
        ),
    ]
