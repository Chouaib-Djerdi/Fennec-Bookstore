# Generated by Django 4.0.10 on 2023-04-22 07:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_comment_rating_alter_comment_unique_together_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='comment',
            unique_together=set(),
        ),
    ]
