# Generated by Django 3.0.6 on 2020-06-20 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0005_acphoto'),
    ]

    operations = [
        migrations.CreateModel(
            name='suggest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('suggestion', models.TextField()),
            ],
        ),
    ]
