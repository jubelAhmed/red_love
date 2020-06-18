# Generated by Django 3.0.3 on 2020-06-15 19:02

from django.db import migrations, models
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('donor', '0006_historicalorgmemorie_orgmemorie'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalmember',
            name='position_name',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='historicalmember',
            name='running_position_status',
            field=models.CharField(choices=[('running', 'Running'), ('retired', 'Retired')], default='running', max_length=10),
        ),
        migrations.AddField(
            model_name='member',
            name='position_name',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='running_position_status',
            field=models.CharField(choices=[('running', 'Running'), ('retired', 'Retired')], default='running', max_length=10),
        ),
        migrations.AlterField(
            model_name='historicalorgmemorie',
            name='cropping',
            field=image_cropping.fields.ImageRatioField('image', '1200x800', adapt_rotation=False, allow_fullsize=False, free_crop=True, help_text=None, hide_image_field=False, size_warning=False, verbose_name='cropping'),
        ),
        migrations.AlterField(
            model_name='orgmemorie',
            name='cropping',
            field=image_cropping.fields.ImageRatioField('image', '1200x800', adapt_rotation=False, allow_fullsize=False, free_crop=True, help_text=None, hide_image_field=False, size_warning=False, verbose_name='cropping'),
        ),
    ]