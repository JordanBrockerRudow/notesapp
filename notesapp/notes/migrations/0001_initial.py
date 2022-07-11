# Generated by Django 3.2.6 on 2022-07-11 14:42

from django.db import migrations, models
import versatileimagefield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthorProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('object_id', models.PositiveIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('modified_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('published_at', models.DateTimeField(blank=True, db_index=True, null=True)),
                ('title', models.TextField(max_length=100)),
                ('slug', models.SlugField(unique=True)),
                ('summary', models.TextField(max_length=500)),
                ('content', models.TextField()),
                ('hero_image', versatileimagefield.fields.VersatileImageField(blank=True, null=True, upload_to='hero_images')),
                ('ppoi', versatileimagefield.fields.PPOIField(blank=True, default='0.5x0.5', editable=False, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.TextField(max_length=100, unique=True)),
            ],
            options={
                'ordering': ['value'],
            },
        ),
    ]
