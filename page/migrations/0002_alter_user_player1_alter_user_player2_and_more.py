# Generated by Django 4.0.6 on 2022-08-03 00:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='player1',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='player1', to='page.player'),
        ),
        migrations.AlterField(
            model_name='user',
            name='player2',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='player2', to='page.player'),
        ),
        migrations.AlterField(
            model_name='user',
            name='player3',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='player3', to='page.player'),
        ),
    ]
