# Generated by Django 5.0 on 2023-12-20 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documento', '0002_documento_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='documento',
            name='em_transito',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
