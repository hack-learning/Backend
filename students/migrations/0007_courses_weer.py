# Generated by Django 3.1.4 on 2020-12-18 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0006_auto_20201218_2239'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='weer',
            field=models.CharField(default=0, max_length=80),
            preserve_default=False,
        ),
    ]
