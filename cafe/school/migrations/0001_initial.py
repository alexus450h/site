# Generated by Django 3.2.5 on 2021-07-22 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d')),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('time_change', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]
