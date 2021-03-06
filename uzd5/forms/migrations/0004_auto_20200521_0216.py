# Generated by Django 3.0.4 on 2020-05-20 23:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0003_auto_20200521_0206'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='materials',
            name='form',
        ),
        migrations.AddField(
            model_name='materials',
            name='material_act',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='material_act', to='forms.MaterialAct'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='materials',
            name='amount_type',
            field=models.CharField(choices=[('PIECE', 'piece'), ('SET', 'set')], default='PIECE', max_length=5),
        ),
    ]
