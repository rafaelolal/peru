# Generated by Django 4.0.4 on 2022-06-01 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_page_category_alter_page_period_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='title',
            field=models.CharField(default='Default Title', max_length=256),
            preserve_default=False,
        ),
    ]
