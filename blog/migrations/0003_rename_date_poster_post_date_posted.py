# Generated by Django 4.2.8 on 2023-12-19 16:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_rename_pst_post'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='date_poster',
            new_name='date_posted',
        ),
    ]