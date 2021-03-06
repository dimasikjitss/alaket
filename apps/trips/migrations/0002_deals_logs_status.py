# Generated by Django 3.1.3 on 2020-11-10 07:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('trips', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('executor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deals_executor', to=settings.AUTH_USER_MODEL)),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deals_package', to='trips.packages')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deals_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Сделка',
                'verbose_name_plural': 'Сделки',
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Статус',
                'verbose_name_plural': 'Статус',
            },
        ),
        migrations.CreateModel(
            name='Logs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('deal_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trips.deals')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trips.status')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Журнал',
                'verbose_name_plural': 'Журналы',
            },
        ),
    ]
