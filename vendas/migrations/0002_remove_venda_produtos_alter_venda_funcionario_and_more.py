# Generated by Django 4.2.7 on 2024-02-05 14:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0008_alter_produto_codigo_barras'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vendas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venda',
            name='produtos',
        ),
        migrations.AlterField(
            model_name='venda',
            name='funcionario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='ItemVenda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.PositiveIntegerField(default=1)),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estoque.produto')),
            ],
        ),
        migrations.AddField(
            model_name='venda',
            name='itens',
            field=models.ManyToManyField(to='vendas.itemvenda'),
        ),
    ]
