# Generated by Django 2.2.2 on 2019-06-11 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CartesMagic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('prix', models.DecimalField(decimal_places=2, max_digits=10000)),
            ],
        ),
    ]
