# Generated by Django 2.0.2 on 2018-03-07 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CSE_Department', '0011_auto_20180305_2134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scijournals',
            name='corresAuthors',
            field=models.CharField(max_length=100, verbose_name='Corresponding Authors'),
        ),
        migrations.AlterField(
            model_name='scijournals',
            name='paperTitle',
            field=models.CharField(max_length=50, verbose_name='Paper Title'),
        ),
    ]