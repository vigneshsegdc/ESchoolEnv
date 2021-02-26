# Generated by Django 3.1.6 on 2021-02-26 10:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_settings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cast',
            name='cast_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='cast',
            name='religion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='user_settings.religion'),
        ),
    ]
