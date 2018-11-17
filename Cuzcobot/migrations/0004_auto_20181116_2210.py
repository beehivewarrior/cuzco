# Generated by Django 2.1.3 on 2018-11-17 05:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Cuzcobot', '0003_auto_20181116_1917'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transactionDate', models.DateTimeField(auto_now_add=True)),
                ('shares', models.IntegerField()),
                ('pricePerShare', models.DecimalField(decimal_places=2, max_digits=16)),
                ('tradeStatus', models.CharField(choices=[('In-Transit', 'IT'), ('Executed', 'E'), ('Failed', 'F')], max_length=1)),
            ],
        ),
        migrations.AddField(
            model_name='pair',
            name='spreadHigh',
            field=models.DecimalField(decimal_places=4, default=0, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pair',
            name='spreadLow',
            field=models.DecimalField(decimal_places=4, default=0, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='price',
            name='current',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=16),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='security',
            name='sharesOwned',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pair',
            name='ticker1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Cuzcobot.Security'),
        ),
        migrations.AlterField(
            model_name='pair',
            name='ticker2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='secondSecurity', to='Cuzcobot.Security'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='ticker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Cuzcobot.Security'),
        ),
    ]
