# Generated by Django 3.0.6 on 2020-06-20 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0007_news'),
    ]

    operations = [
        migrations.CreateModel(
            name='learn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.TextField()),
                ('desc', models.TextField()),
                ('col', models.TextField(default=12)),
            ],
        ),
        migrations.AddField(
            model_name='achievementss',
            name='var',
            field=models.TextField(default='left'),
        ),
    ]
