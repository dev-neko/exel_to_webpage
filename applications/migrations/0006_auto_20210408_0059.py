# Generated by Django 3.1.7 on 2021-04-07 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0005_remove_searchquerymodel_md_analysis_pages'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='searchquerymodel',
            name='md_ana_end_spec',
        ),
        migrations.RemoveField(
            model_name='searchquerymodel',
            name='md_analysis_pages_end',
        ),
        migrations.RemoveField(
            model_name='searchquerymodel',
            name='md_analysis_pages_radio',
        ),
        migrations.RemoveField(
            model_name='searchquerymodel',
            name='md_analysis_pages_str',
        ),
        migrations.RemoveField(
            model_name='searchquerymodel',
            name='md_auto_ext',
        ),
        migrations.RemoveField(
            model_name='searchquerymodel',
            name='md_e_time',
        ),
        migrations.RemoveField(
            model_name='searchquerymodel',
            name='md_e_wday',
        ),
        migrations.RemoveField(
            model_name='searchquerymodel',
            name='md_exclude_id',
        ),
        migrations.RemoveField(
            model_name='searchquerymodel',
            name='md_exclude_id_radio',
        ),
        migrations.RemoveField(
            model_name='searchquerymodel',
            name='md_exclude_titledesc',
        ),
        migrations.RemoveField(
            model_name='searchquerymodel',
            name='md_exclude_titledesc_radio',
        ),
        migrations.RemoveField(
            model_name='searchquerymodel',
            name='md_radio_ana_end_spec',
        ),
        migrations.RemoveField(
            model_name='searchquerymodel',
            name='md_radio_e_wday_e_time',
        ),
        migrations.RemoveField(
            model_name='searchquerymodel',
            name='md_radio_url',
        ),
        migrations.RemoveField(
            model_name='searchquerymodel',
            name='md_rate',
        ),
        migrations.RemoveField(
            model_name='searchquerymodel',
            name='md_rate_radio',
        ),
        migrations.RemoveField(
            model_name='searchquerymodel',
            name='md_seller_url',
        ),
        migrations.RemoveField(
            model_name='searchquerymodel',
            name='md_src_url',
        ),
        migrations.AddField(
            model_name='searchquerymodel',
            name='md_ex_desc',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='searchquerymodel',
            name='md_ex_title',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='searchquerymodel',
            name='md_or_desc',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='searchquerymodel',
            name='md_or_title',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='searchquerymodel',
            name='md_price_max',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='searchquerymodel',
            name='md_price_min',
            field=models.CharField(max_length=50, null=True),
        ),
    ]