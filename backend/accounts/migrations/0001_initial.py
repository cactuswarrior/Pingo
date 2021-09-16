# Generated by Django 3.2.7 on 2021-09-09 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accounts',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(blank=True, max_length=50, null=True)),
                ('time_to_expire', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]