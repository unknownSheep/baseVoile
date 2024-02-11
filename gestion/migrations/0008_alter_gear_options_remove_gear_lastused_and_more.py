# Generated by Django 4.2.9 on 2024-02-10 15:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0007_alter_gear_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gear',
            options={'verbose_name': 'Materiel'},
        ),
        migrations.RemoveField(
            model_name='gear',
            name='lastUsed',
        ),
        migrations.RemoveField(
            model_name='gear',
            name='lastUsedDate',
        ),
        migrations.CreateModel(
            name='Rent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('startTime', models.TimeField()),
                ('returnTime', models.TimeField()),
                ('isDamaged', models.BooleanField(default=False)),
                ('adherent', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='gestion.adherent')),
                ('gear', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='gestion.gear')),
            ],
        ),
    ]