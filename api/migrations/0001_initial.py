# Generated by Django 3.2.16 on 2022-11-25 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('latitude', models.CharField(max_length=200, null=True)),
                ('longitude', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
