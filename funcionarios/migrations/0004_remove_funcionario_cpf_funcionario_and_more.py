# Generated by Django 4.2.7 on 2024-02-02 17:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('funcionarios', '0003_funcionario_loja_delete_proprietario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='funcionario',
            name='cpf_funcionario',
        ),
        migrations.RemoveField(
            model_name='funcionario',
            name='loja',
        ),
        migrations.RemoveField(
            model_name='funcionario',
            name='nome_funcionario',
        ),
        migrations.RemoveField(
            model_name='funcionario',
            name='telefone_funcionario',
        ),
    ]