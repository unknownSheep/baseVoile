# Generated by Django 4.2.9 on 2024-02-25 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adherent',
            name='adhesion',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='adherent',
            name='email',
            field=models.EmailField(blank=True, default=None, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='adherent',
            name='phone',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]