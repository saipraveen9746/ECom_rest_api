# Generated by Django 4.2.6 on 2023-11-07 06:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_cart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='Quantity',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='product',
        ),
        migrations.AddField(
            model_name='cart',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.CreateModel(
            name='CartProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.PositiveIntegerField(default=0)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.cart')),
            ],
        ),
    ]
