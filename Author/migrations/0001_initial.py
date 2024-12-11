# Generated by Django 4.2.2 on 2024-12-05 14:00

import Author.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40, validators=[django.core.validators.MinLengthValidator(4), Author.models.letters_only_check])),
                ('last_name', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(2), Author.models.letters_only_check])),
                ('passcode', models.CharField(help_text='Your passcode must be a combination of 6 digits', validators=[Author.models.validate_passcode])),
                ('pets_number', models.PositiveSmallIntegerField()),
                ('info', models.TextField(blank=True, null=True)),
                ('image_url', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
