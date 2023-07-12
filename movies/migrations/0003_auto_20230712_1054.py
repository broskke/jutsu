# Generated by Django 3.2 on 2023-07-12 10:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20230712_1034'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='movies',
            name='age_permissions',
            field=models.PositiveIntegerField(default=12, verbose_name='Возрастной рейтинг'),
        ),
        migrations.CreateModel(
            name='PostImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='posts')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='movies.movies')),
            ],
        ),
    ]
