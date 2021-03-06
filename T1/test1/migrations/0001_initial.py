# Generated by Django 2.0.6 on 2018-06-25 02:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DocType', models.CharField(default='CATPart', max_length=20)),
                ('PartNumber', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProjectID', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='doc',
            name='DocProject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test1.Project'),
        ),
    ]
