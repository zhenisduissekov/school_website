# Generated by Django 3.1.5 on 2021-01-11 07:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210111_0704'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pupil',
            old_name='teacherName',
            new_name='teacher',
        ),
        migrations.AlterField(
            model_name='teacher',
            name='className',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.lesson'),
        ),
    ]
