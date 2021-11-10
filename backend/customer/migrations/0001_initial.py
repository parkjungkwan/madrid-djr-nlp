# Generated by Django 3.2.5 on 2021-11-10 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=10)),
                ('name', models.TextField()),
                ('phone', models.TextField()),
                ('email', models.TextField()),
                ('city', models.TextField()),
                ('state', models.TextField()),
                ('address', models.TextField()),
                ('date_of_birth', models.DateField()),
            ],
            options={
                'db_table': 'customers',
            },
        ),
    ]