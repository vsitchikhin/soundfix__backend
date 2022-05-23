# Generated by Django 4.0.4 on 2022-05-19 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_delete_passport_delete_user_data_delete_users'),
    ]

    operations = [
        migrations.CreateModel(
            name='Passport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passport_numbers', models.IntegerField()),
                ('passport_organ', models.CharField(max_length=255)),
                ('issue_date', models.DateField()),
                ('subdivision_code', models.CharField(max_length=10)),
                ('birth_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User_Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=255)),
                ('account_type', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('surname', models.CharField(max_length=255)),
                ('patronymic', models.CharField(blank=True, max_length=255)),
            ],
        ),
    ]
