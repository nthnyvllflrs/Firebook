# Generated by Django 2.0.8 on 2019-10-02 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='status',
            field=models.CharField(choices=[('Ongoing', 'Ongoing'), ('Cleared', 'Cleared')], default='Ongoing', max_length=10),
        ),
    ]
