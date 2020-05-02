# Generated by Django 3.0.5 on 2020-04-22 13:08

from django.conf import settings
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('slots_total', models.IntegerField()),
                ('content', models.TextField(blank=True)),
                ('weekly_event', models.BooleanField(default=True)),
                ('attendees', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]