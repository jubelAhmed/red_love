# Generated by Django 3.0.3 on 2020-06-14 19:17

from django.db import migrations, models
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('donor', '0004_auto_20200612_2250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalmember',
            name='cropping',
            field=image_cropping.fields.ImageRatioField('image', '400x300', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=True, verbose_name='cropping'),
        ),
        migrations.AlterField(
            model_name='historicalmember',
            name='occupation',
            field=models.CharField(help_text='Student / Business / Farmer /..', max_length=250),
        ),
        migrations.AlterField(
            model_name='member',
            name='cropping',
            field=image_cropping.fields.ImageRatioField('image', '400x300', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=True, verbose_name='cropping'),
        ),
        migrations.AlterField(
            model_name='member',
            name='occupation',
            field=models.CharField(help_text='Student / Business / Farmer /..', max_length=250),
        ),
    ]
