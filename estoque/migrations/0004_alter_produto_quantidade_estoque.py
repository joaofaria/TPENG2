# Generated by Django 4.2.7 on 2024-02-02 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0003_produto_imagem_produto_alter_produto_valor_custo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='quantidade_estoque',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]