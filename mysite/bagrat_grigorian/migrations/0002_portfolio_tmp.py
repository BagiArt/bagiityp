# Generated by Django 3.2.7 on 2022-09-21 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bagrat_grigorian', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='portfolio_tmp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_img', models.ImageField(upload_to='images/portfolio_tmp')),
                ('title', models.TextField()),
                ('date', models.DateField()),
                ('client', models.TextField()),
                ('category', models.TextField()),
                ('progect_url', models.URLField()),
                ('description', models.TextField()),
                ('cover', models.ImageField(upload_to='images/portfolio_tmp')),
            ],
        ),
    ]
