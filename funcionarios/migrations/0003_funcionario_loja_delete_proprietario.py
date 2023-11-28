# Generated by Django 4.2.7 on 2023-11-28 01:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administracao', '0003_remove_loja_id_proprietario_loja_usuario_responsavel_and_more'),
        ('funcionarios', '0002_proprietario_funcionario_cpf_funcionario_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='funcionario',
            name='loja',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='funcionarios', to='administracao.loja'),
        ),
        migrations.DeleteModel(
            name='Proprietario',
        ),
    ]