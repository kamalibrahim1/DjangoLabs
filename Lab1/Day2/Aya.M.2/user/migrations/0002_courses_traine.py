# Generated by Django 4.0.5 on 2022-06-18 18:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('Course_id', models.AutoField(primary_key=True, serialize=False)),
                ('Cours_Name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Traine',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100)),
                ('national', models.CharField(max_length=50)),
                ('fk_course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.courses')),
            ],
        ),
    ]
