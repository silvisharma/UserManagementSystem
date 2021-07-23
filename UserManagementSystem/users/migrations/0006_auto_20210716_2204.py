# Generated by Django 3.2.5 on 2021-07-16 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20210716_1923'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('desc', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
