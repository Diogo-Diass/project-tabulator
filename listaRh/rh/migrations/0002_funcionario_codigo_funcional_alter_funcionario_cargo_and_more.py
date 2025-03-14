# Generated by Django 5.1.6 on 2025-03-04 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rh", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="funcionario",
            name="codigo_funcional",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="funcionario",
            name="cargo",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="funcionario",
            name="data_admissao",
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name="funcionario",
            name="data_saida",
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name="funcionario",
            name="nascimento",
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name="funcionario",
            name="nome",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="funcionario",
            name="tipo_cargo",
            field=models.CharField(max_length=100, null=True),
        ),
    ]
