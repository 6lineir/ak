# Generated by Django 3.0.7 on 2020-06-09 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_auto_20200610_0256'),
    ]

    operations = [
        migrations.CreateModel(
            name='mantg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mntg', models.CharField(max_length=48, verbose_name='ناحیه')),
            ],
        ),
        migrations.AddField(
            model_name='addads',
            name='timepub',
            field=models.DateTimeField(auto_now=True, verbose_name='زمان انتشار'),
        ),
    ]
