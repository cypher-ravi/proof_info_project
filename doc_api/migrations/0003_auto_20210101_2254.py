# Generated by Django 3.1.4 on 2021-01-01 22:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doc_api', '0002_auto_20210101_2233'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='processfordoc',
            name='step',
        ),
        migrations.RemoveField(
            model_name='proof',
            name='authority_required',
        ),
        migrations.RemoveField(
            model_name='proof',
            name='documents_required',
        ),
        migrations.RemoveField(
            model_name='proof',
            name='process',
        ),
        migrations.AddField(
            model_name='authoritysignrequiredforproof',
            name='proof',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='doc_api.proof'),
        ),
        migrations.AddField(
            model_name='documentrequiredforproof',
            name='proof',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='doc_api.proof'),
        ),
        migrations.AddField(
            model_name='processfordoc',
            name='proof',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='doc_api.proof'),
        ),
        migrations.AddField(
            model_name='stepofprocess',
            name='process',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='doc_api.processfordoc'),
        ),
    ]
