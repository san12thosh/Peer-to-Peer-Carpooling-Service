# Generated by Django 4.2.14 on 2024-08-04 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peer_to_peer', '0006_alter_createride_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='mapRider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=40)),
                ('destination', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='mapUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=40)),
                ('destination', models.CharField(max_length=40)),
            ],
        ),
        migrations.AddField(
            model_name='createride',
            name='Gender',
            field=models.CharField(default='Not Specified', max_length=10),
        ),
        migrations.AddField(
            model_name='createuser',
            name='Gender',
            field=models.CharField(default='Not Specified', max_length=10),
        ),
        migrations.AlterField(
            model_name='createride',
            name='vehicle_type',
            field=models.CharField(max_length=10),
        ),
    ]
