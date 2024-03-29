# Generated by Django 5.0.1 on 2024-02-28 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('desc', models.TextField()),
                ('date', models.DateField(default=True)),
                ('image', models.ImageField(upload_to='images/')),
                ('duration', models.IntegerField()),
                ('rate', models.FloatField()),
                ('author', models.CharField(max_length=64)),
            ],
        ),
    ]
