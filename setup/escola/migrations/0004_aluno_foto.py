# Generated by Django 3.2.14 on 2022-07-13 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0003_aluno_celular'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluno',
            name='foto',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]