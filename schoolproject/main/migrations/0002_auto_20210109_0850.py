# Generated by Django 3.1.5 on 2021-01-09 08:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lesson',
            options={'verbose_name': 'Урок', 'verbose_name_plural': 'Уроки'},
        ),
        migrations.AlterModelOptions(
            name='pupil',
            options={'verbose_name': 'Ученик', 'verbose_name_plural': 'Ученики'},
        ),
        migrations.AlterModelOptions(
            name='teacher',
            options={'verbose_name': 'Учитель', 'verbose_name_plural': 'Учителя'},
        ),
        migrations.AddField(
            model_name='pupil',
            name='teacherName',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='main.teacher'),
        ),
    ]
