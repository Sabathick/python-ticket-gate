# Generated by Django 4.2.7 on 2023-11-23 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AllowList',
            fields=[
                ('ip_address', models.GenericIPAddressField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='RejectList',
            fields=[
                ('ip_address', models.GenericIPAddressField(primary_key=True, serialize=False)),
            ],
        ),
    ]