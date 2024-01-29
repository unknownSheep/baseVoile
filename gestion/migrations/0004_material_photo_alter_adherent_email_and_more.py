# Generated by Django 4.2.9 on 2024-01-28 15:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0003_rename_name_adherent_firstname'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='photos/'),
        ),
        migrations.AlterField(
            model_name='adherent',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='adherent',
            name='phone',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='material',
            name='lastUsed',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='gestion.adherent'),
        ),
        migrations.AlterField(
            model_name='material',
            name='lastUsedDate',
            field=models.DateField(blank=True, null=True),
        ),
    ]
