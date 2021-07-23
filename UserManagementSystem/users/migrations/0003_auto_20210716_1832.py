# Generated by Django 3.2.5 on 2021-07-16 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_showuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('email', models.EmailField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.RenameField(
            model_name='showuser',
            old_name='uemail',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='showuser',
            old_name='uname',
            new_name='password',
        ),
        migrations.RenameField(
            model_name='showuser',
            old_name='upass',
            new_name='username',
        ),
        migrations.RemoveField(
            model_name='showuser',
            name='uid',
        ),
    ]