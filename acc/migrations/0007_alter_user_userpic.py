# Generated by Django 3.2.7 on 2021-09-28 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acc', '0006_alter_user_userpic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='userpic',
            field=models.ImageField(blank=True, upload_to='usr/%y'),
        ),
    ]