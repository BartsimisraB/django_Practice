# Generated by Django 4.1.7 on 2023-04-05 02:56

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
                ('name', models.CharField(max_length=20)),
                ('adr', models.CharField(max_length=50)),
                ('create_day', models.DateTimeField(auto_now_add=True)),
                ('update_day', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
