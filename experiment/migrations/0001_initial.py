# Generated by Django 2.2.4 on 2019-08-03 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerSubscriptionUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('time_stamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]