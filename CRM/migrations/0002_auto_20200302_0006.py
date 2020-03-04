# Generated by Django 2.1.5 on 2020-03-02 00:06

from django.db import migrations, models
import django_countries.fields
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('CRM', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='Date_naissance',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='Email',
            field=models.EmailField(blank=True, max_length=200, unique=True),
        ),
        migrations.AddField(
            model_name='client',
            name='Nationality',
            field=models.CharField(blank=True, max_length=200, unique=True),
        ),
        migrations.AddField(
            model_name='client',
            name='Nom',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='Prenom',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='Sexe',
            field=models.CharField(choices=[('Male', 'MALE'), ('Female', 'FEMALE')], default=None, max_length=20),
        ),
        migrations.AddField(
            model_name='client',
            name='archive',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='client',
            name='pays',
            field=django_countries.fields.CountryField(blank=True, max_length=2, unique=True),
        ),
        migrations.AddField(
            model_name='client',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
        migrations.AddField(
            model_name='client',
            name='tel_f',
            field=models.IntegerField(default=123456),
        ),
        migrations.AddField(
            model_name='client',
            name='tel_p',
            field=models.IntegerField(default=123456),
        ),
        migrations.AlterField(
            model_name='training',
            name='all_trainee',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[(1, 'BrugKe'), (2, 'gs1'), (4, 'low'), (5, 'team'), (6, 'uvs')], max_length=3, null=True),
        ),
    ]
