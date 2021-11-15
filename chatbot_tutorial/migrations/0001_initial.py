# Generated by Django 2.2.8 on 2021-11-14 10:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BotPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(null=True)),
                ('title', models.CharField(max_length=100)),
                ('user_id', models.ForeignKey(db_column='user_id', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_id', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
