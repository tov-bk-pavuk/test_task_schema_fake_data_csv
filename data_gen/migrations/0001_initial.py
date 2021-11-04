# Generated by Django 3.2.8 on 2021-11-04 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataSetFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now=True)),
                ('status', models.CharField(choices=[('RD', 'Ready'), ('PR', 'Processing')], default='PR', max_length=2)),
                ('url', models.URLField(default='static/media/default.csv')),
            ],
        ),
    ]
