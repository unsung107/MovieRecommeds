# Generated by Django 2.2.7 on 2019-11-28 23:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CommingMovie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('openDt', models.DateField()),
                ('post_url', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('post_url', models.TextField()),
                ('code', models.CharField(max_length=40, unique=True)),
                ('discription', models.TextField()),
                ('audience', models.IntegerField()),
                ('watch_grade', models.IntegerField()),
                ('watch_grade_name', models.CharField(max_length=20)),
                ('score', models.FloatField()),
                ('video_url', models.TextField()),
                ('snapshot_url', models.TextField()),
                ('genres', models.ManyToManyField(related_name='movies', to='movies.Genre')),
            ],
        ),
        migrations.CreateModel(
            name='Recommend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('discription', models.TextField()),
                ('img_file', models.ImageField(upload_to='')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('movies', models.ManyToManyField(related_name='recommends', to='movies.Movie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recommends', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=100)),
                ('score', models.IntegerField()),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='movies.Movie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RecommendReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=100)),
                ('recommend', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recommend_reviews', to='movies.Recommend')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recommend_reviews', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MovieComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='moviecomments', to='movies.Movie')),
                ('recommend', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='moviecomments', to='movies.Recommend')),
            ],
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=40, unique=True)),
                ('image_url', models.TextField()),
                ('movies', models.ManyToManyField(related_name='directors', to='movies.Movie')),
            ],
        ),
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=40, unique=True)),
                ('image_url', models.TextField()),
                ('movies', models.ManyToManyField(related_name='actors', to='movies.Movie')),
            ],
        ),
    ]
