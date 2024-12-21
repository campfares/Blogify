# Generated by Django 5.1.4 on 2024-12-18 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bw', '0005_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('img', models.ImageField(default='static/images/download.jpg', upload_to='about_photos')),
                ('body', models.TextField()),
            ],
        ),
    ]
