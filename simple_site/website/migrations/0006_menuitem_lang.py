# Generated by Django 2.0.6 on 2018-06-15 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_auto_20180615_2116'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='lang',
            field=models.CharField(choices=[('en', 'EN'), ('es', 'ES')], default='en', max_length=20),
        ),
    ]