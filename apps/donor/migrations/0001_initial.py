# Generated by Django 3.0.3 on 2020-06-05 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Donor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=15, unique=True)),
                ('email', models.EmailField(blank=True, max_length=255, null=True)),
                ('blood_group', models.CharField(choices=[('o+', 'O+'), ('o-', 'O-'), ('a+', 'A+'), ('a-', 'A-'), ('b+', 'B+'), ('b-', 'B-'), ('ab+', 'AB+'), ('ab-', 'AB-')], default='O+', max_length=10)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('present_address', models.CharField(max_length=255)),
                ('permanent_address', models.CharField(max_length=255)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=False)),
                ('blood_donor_status', models.BooleanField(default=True)),
            ],
        ),
    ]