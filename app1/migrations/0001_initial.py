# Generated by Django 4.0.5 on 2022-06-05 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Nikki',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_name', models.CharField(max_length=100)),
                ('content_detail', models.TextField()),
                ('create_date', models.DateTimeField()),
            ],
        ),
    ]
