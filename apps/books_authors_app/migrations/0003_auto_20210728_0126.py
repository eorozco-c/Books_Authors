# Generated by Django 2.2.4 on 2021-07-28 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_authors_app', '0002_autor_notas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autor',
            name='notas',
            field=models.TextField(blank=True, null=True),
        ),
    ]