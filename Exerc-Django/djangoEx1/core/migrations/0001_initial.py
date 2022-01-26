# Generated by Django 4.0.1 on 2022-01-26 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produtos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('preco', models.IntegerField(verbose_name='Preço')),
                ('estoque', models.IntegerField(verbose_name='Quantidade em estoque')),
            ],
        ),
    ]
