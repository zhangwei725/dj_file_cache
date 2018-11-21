# Generated by Django 2.1.3 on 2018-11-21 06:39

from django.db import migrations, models
import django.db.models.deletion
import upload.models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0002_auto_20181121_1429'),
    ]

    operations = [
        migrations.CreateModel(
            name='Img',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(max_length=255, storage=upload.models.ImageFileStorage(), upload_to='shop/img/')),
                ('type', models.SmallIntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='shop',
            name='img',
        ),
        migrations.AddField(
            model_name='img',
            name='shop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='upload.Shop'),
        ),
    ]