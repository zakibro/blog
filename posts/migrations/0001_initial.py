# Generated by Django 2.2 on 2019-04-11 20:08

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
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=False, verbose_name='aktywny')),
                ('pub_date', models.DateTimeField(null=True, verbose_name='data publikacji')),
                ('title', models.CharField(max_length=25, verbose_name='tytuł')),
                ('slug', models.SlugField()),
                ('lead', models.TextField(verbose_name='wprowadzanie')),
                ('body', models.TextField(verbose_name='treść')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='autor')),
            ],
            options={
                'verbose_name': 'wpis',
                'verbose_name_plural': 'wpisy',
            },
        ),
    ]
