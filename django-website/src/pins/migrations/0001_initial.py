# Generated by Django 2.2.1 on 2019-05-11 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('imgurl', models.TextField()),
                ('website', models.TextField()),
                ('description', models.TextField()),
                ('latitude', models.DecimalField(decimal_places=7, max_digits=10)),
                ('longitude', models.DecimalField(decimal_places=7, max_digits=10)),
            ],
        ),
    ]