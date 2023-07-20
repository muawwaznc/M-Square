# Generated by Django 4.0.6 on 2023-07-15 11:02

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('price', models.FloatField()),
                ('orderedAt', models.DateTimeField(default=django.utils.timezone.now)),
                ('isDeliver', models.BooleanField(default=False)),
                ('buyerID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.buyer')),
                ('productID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.product')),
                ('sellerID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.seller')),
            ],
        ),
    ]