# Generated by Django 3.1.2 on 2020-10-12 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Event_image', models.ImageField(upload_to='event_images/')),
                ('Event_text', models.CharField(max_length=200)),
            ],
        ),
    ]