# Generated by Django 5.1.3 on 2024-11-20 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donor', '0003_alter_blooddonate_id_alter_donor_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blooddonate',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='donor',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
