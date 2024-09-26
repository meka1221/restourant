# Generated by Django 4.2.16 on 2024-09-14 10:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usman', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Courier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courier_name', models.CharField(max_length=50)),
                ('phone_number', models.IntegerField(default=0)),
                ('status', models.CharField(choices=[('car', 'car'), ('bike', 'bike'), ('walk', 'walk')], max_length=16)),
            ],
        ),
        migrations.RenameField(
            model_name='category',
            old_name='cafe_name',
            new_name='category_name',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='age',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usman.userprofile')),
                ('parent_review', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='usman.review')),
                ('resto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usman.food')),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stars', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], verbose_name='Rating')),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usman.food')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usman.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.PositiveIntegerField()),
                ('delivery_time', models.DateTimeField(auto_now_add=True)),
                ('courier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usman.courier')),
                ('resto_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usman.food')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usman.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Д', 'Доставлено'), ('Вп', 'В пути'), ('ОП', 'Ожидает получения')], max_length=16)),
                ('courier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usman.courier')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usman.order')),
            ],
        ),
    ]
