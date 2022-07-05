# Generated by Django 4.0.4 on 2022-06-21 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppBlog', '0003_alter_posts_cuerpo_avatar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Imagen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('imagen', models.ImageField(upload_to='pictures')),
            ],
            options={
                'verbose_name': 'Imagen',
                'verbose_name_plural': 'Imagenes',
            },
        ),
        migrations.AlterModelOptions(
            name='avatar',
            options={'verbose_name': 'Avatar', 'verbose_name_plural': 'Avatar'},
        ),
    ]