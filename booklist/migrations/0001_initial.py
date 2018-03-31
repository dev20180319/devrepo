# Generated by Django 2.0.2 on 2018-03-02 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headNumber', models.CharField(max_length=200)),
                ('sheduleLoadTime', models.DateTimeField()),
                ('loadPoint', models.CharField(max_length=200)),
                ('driverName', models.CharField(max_length=200)),
                ('convoyName', models.CharField(max_length=200)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weixinhao', models.CharField(max_length=200)),
                ('juse', models.CharField(max_length=200)),
                ('urlcaoz', models.TextField()),
                ('text_beizhu', models.TextField()),
            ],
        ),
    ]