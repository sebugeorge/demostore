# Generated by Django 4.2.3 on 2023-11-19 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('dob', models.DateField()),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField()),
                ('department', models.CharField(max_length=200)),
                ('topic', models.CharField(max_length=200)),
                ('purpose', models.CharField(max_length=200)),
                ('materials', models.TextField()),
            ],
        ),
    ]
