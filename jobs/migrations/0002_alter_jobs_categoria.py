# Generated by Django 4.2.8 on 2023-12-05 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='categoria',
            field=models.CharField(choices=[('T', 'Todas'), ('D', 'Design'), ('EV', 'Edição de Vídeo')], default='T', max_length=2),
        ),
    ]
