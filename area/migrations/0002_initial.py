# Generated by Django 5.2.2 on 2025-06-13 17:13

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('area', '0001_initial'),
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='anime',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='event',
            name='anime',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='area.anime'),
        ),
        migrations.AddField(
            model_name='food',
            name='anime',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='area.anime'),
        ),
        migrations.AddField(
            model_name='food',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='foods', to='area.foodcategory', verbose_name='категория'),
        ),
        migrations.AddField(
            model_name='food',
            name='food_ingredient',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ingredients', to='area.foodingredient'),
        ),
        migrations.AddField(
            model_name='merch',
            name='anime',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='animes', to='area.anime'),
        ),
        migrations.AddField(
            model_name='merch',
            name='merch_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='area.merchcategory'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='orderelement',
            name='content_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype'),
        ),
        migrations.AddField(
            model_name='orderelement',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='area.order', verbose_name='Заказ'),
        ),
        migrations.AddField(
            model_name='payment',
            name='order',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='area.order'),
        ),
    ]
