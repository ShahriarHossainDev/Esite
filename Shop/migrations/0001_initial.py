# Generated by Django 4.1.3 on 2022-12-21 17:03

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
            name='userProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'female'), ('Other', 'Other')], max_length=10)),
                ('image', models.ImageField(upload_to='profilePic')),
                ('birthday', models.DateTimeField(auto_now_add=True)),
                ('phone_number', models.IntegerField()),
                ('address', models.TextField(default='Add Your Address', max_length=200)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
