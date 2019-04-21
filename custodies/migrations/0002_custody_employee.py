# Generated by Django 2.2 on 2019-04-19 07:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
        ('custodies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='custody',
            name='employee',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='employees.Employee'),
            preserve_default=False,
        ),
    ]