# Generated by Django 4.1.7 on 2023-04-06 02:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('three', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField()),
                ('comment', models.CharField(max_length=100)),
                ('create_day', models.DateTimeField(auto_now_add=True)),
                ('update_day', models.DateTimeField(auto_now=True)),
                ('res', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='three.food')),
            ],
        ),
    ]
