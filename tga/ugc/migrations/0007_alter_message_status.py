# Generated by Django 4.0.4 on 2022-05-15 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ugc', '0006_alter_message_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='status',
            field=models.TextField(null=True, verbose_name='Status'),
        ),
    ]
