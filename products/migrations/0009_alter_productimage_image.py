# Generated by Django 5.1.2 on 2025-04-10 15:36

import config.utils.image_validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_product_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.ImageField(upload_to='products/', validators=[config.utils.image_validators.validate_image_size, config.utils.image_validators.validate_image_dimesions]),
        ),
    ]
