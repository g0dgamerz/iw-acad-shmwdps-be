# Generated by Django 3.1.6 on 2021-02-11 16:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0001_initial'),
        ('users', '0004_auto_20210211_1610'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='room',
        ),
        migrations.AddField(
            model_name='patient',
            name='bed',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='hospital.bed'),
        ),
        migrations.AddField(
            model_name='patient',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.customuser'),
            preserve_default=False,
        ),
    ]