# Generated by Django 4.2.8 on 2023-12-05 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_alter_jobs_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='status',
            field=models.CharField(choices=[('C', 'Em criação'), ('AA', 'Aguardando Aprovação'), ('F', 'Finalizado')], default='C', max_length=2),
        ),
    ]
