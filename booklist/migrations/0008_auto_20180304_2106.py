# Generated by Django 2.0.2 on 2018-03-04 13:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booklist', '0007_auto_20180304_1938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='xianchangduilie',
            name='id_s_qianghao',
            field=models.ForeignKey(blank=True, max_length=20, null=True, on_delete=django.db.models.deletion.CASCADE, to='booklist.QiangHao'),
        ),
    ]
