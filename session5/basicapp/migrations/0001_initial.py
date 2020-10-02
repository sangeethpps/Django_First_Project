# Generated by Django 3.1.1 on 2020-09-13 06:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfileInfo',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('port_folio_site', models.URLField(blank=True)),
                ('profile_picture', models.ImageField(blank=True, upload_to='profle_pics')),
            ],
        ),
    ]
