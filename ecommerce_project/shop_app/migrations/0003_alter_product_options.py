# Generated by Django 4.2.9 on 2024-02-06 17:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0002_alter_category_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('name',), 'verbose_name': 'product', 'verbose_name_plural': 'products'},
        ),
    ]