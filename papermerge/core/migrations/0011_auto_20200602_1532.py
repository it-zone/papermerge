# Generated by Django 3.0.6 on 2020-06-02 15:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_remove_kvstore_human_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kvstorenode',
            name='node',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='kvstore', to='core.BaseTreeNode'),
        ),
    ]
