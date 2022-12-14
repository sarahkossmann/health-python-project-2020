# Generated by Django 3.0.4 on 2020-04-05 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('author', models.CharField(max_length=1000, null=True)),
                ('description', models.CharField(max_length=1000)),
                ('url', models.CharField(max_length=1000)),
                ('image_url', models.ImageField(max_length=1000, upload_to='news_pics')),
                ('published_date', models.CharField(max_length=1000)),
                ('content', models.TextField(max_length=100000, null=True)),
            ],
        ),
    ]
