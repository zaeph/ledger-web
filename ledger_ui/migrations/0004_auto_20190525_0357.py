# Generated by Django 2.1.7 on 2019-05-25 01:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ledger_ui', '0003_undo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='undo',
            old_name='last_entry',
            new_name='last_entry_pickle',
        ),
    ]
