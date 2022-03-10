# Generated by Django 4.0.3 on 2022-03-10 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oauth', '0003_alter_oauth_access_token_alter_oauth_refresh_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='access_token',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='last_hit',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='client',
            name='refresh_token',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='oauth',
            name='full_name',
            field=models.CharField(default='Ageng Anugrah Wardoyo Putra', max_length=255),
            preserve_default=False,
        ),
    ]