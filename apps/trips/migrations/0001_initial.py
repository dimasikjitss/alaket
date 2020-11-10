# Generated by Django 3.1.3 on 2020-11-10 07:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Город')),
            ],
            options={
                'verbose_name': 'Название города',
                'verbose_name_plural': 'Название городов',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Страна')),
            ],
            options={
                'verbose_name': 'Страна',
                'verbose_name_plural': 'Страны',
            },
        ),
        migrations.CreateModel(
            name='Packages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('date', models.DateField(auto_now=True)),
                ('weight', models.FloatField()),
                ('fee', models.DecimalField(decimal_places=10, max_digits=19)),
                ('comment', models.TextField()),
                ('recipient_name', models.CharField(max_length=100)),
                ('recipient_contact', models.CharField(max_length=100)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trips.categories')),
                ('city_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='packages_city_from', to='trips.city')),
                ('city_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='packages_city_to', to='trips.city')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Посылка',
                'verbose_name_plural': 'Посылки',
                'ordering': ('-date_created',),
            },
        ),
        migrations.CreateModel(
            name='TransportType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Вид Транспорта',
                'verbose_name_plural': 'Виды транспорта',
            },
        ),
        migrations.CreateModel(
            name='Trips',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departure_date', models.DateField(auto_now=True)),
                ('arrival_date', models.DateField(auto_now=True)),
                ('weight', models.FloatField()),
                ('fee', models.DecimalField(decimal_places=2, max_digits=19)),
                ('comment', models.TextField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('categoty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trips.categories')),
                ('city_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trip_city_from', to='trips.city')),
                ('city_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trip_city_to', to='trips.city')),
                ('transport_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trips.transporttype')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Поездка',
                'verbose_name_plural': 'Поездки',
            },
        ),
        migrations.CreateModel(
            name='Pictures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='pictures')),
                ('packages_id', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='packages', to='trips.packages')),
                ('trip_id', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='trips', to='trips.trips')),
            ],
            options={
                'verbose_name': 'Изображение',
                'verbose_name_plural': 'Изображения',
            },
        ),
        migrations.AddField(
            model_name='city',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trips.country', verbose_name='Страна'),
        ),
    ]