# Generated by Django 4.1.10 on 2023-09-14 10:29

import django.contrib.postgres.fields
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models

import api_app.defaults
import api_app.validators


class Migration(migrations.Migration):
    dependencies = [
        (
            "api_app",
            "0046_remove_pluginconfig_plugin_config_no_config_all_null_and_more",
        ),
        ("playbooks_manager", "0018_playbookconfig_scan_check_time_and_more"),
        ("pivots_manager", "0006_alter_pivotconfig_analyzer_config_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="PivotReport",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("FAILED", "Failed"),
                            ("PENDING", "Pending"),
                            ("RUNNING", "Running"),
                            ("SUCCESS", "Success"),
                            ("KILLED", "Killed"),
                        ],
                        max_length=50,
                    ),
                ),
                ("report", models.JSONField(default=dict)),
                (
                    "errors",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(max_length=512),
                        blank=True,
                        default=list,
                        size=None,
                    ),
                ),
                ("start_time", models.DateTimeField(default=django.utils.timezone.now)),
                ("end_time", models.DateTimeField(default=django.utils.timezone.now)),
                ("task_id", models.UUIDField()),
            ],
        ),
        migrations.RenameModel(
            old_name="Pivot",
            new_name="PivotMap",
        ),
        migrations.RemoveConstraint(
            model_name="pivotconfig",
            name="pivot_config_no_config_all_null",
        ),
        migrations.RemoveIndex(
            model_name="pivotconfig",
            name="pivots_mana_analyze_30afa2_idx",
        ),
        migrations.RemoveIndex(
            model_name="pivotconfig",
            name="pivots_mana_connect_255ab8_idx",
        ),
        migrations.RemoveIndex(
            model_name="pivotconfig",
            name="pivots_mana_visuali_eb376f_idx",
        ),
        migrations.RemoveIndex(
            model_name="pivotconfig",
            name="pivots_mana_playboo_a73263_idx",
        ),
        migrations.RemoveIndex(
            model_name="pivotmap",
            name="pivots_mana_startin_694120_idx",
        ),
        migrations.RemoveIndex(
            model_name="pivotmap",
            name="pivots_mana_pivot_c_c45692_idx",
        ),
        migrations.RemoveIndex(
            model_name="pivotmap",
            name="pivots_mana_ending__913ba6_idx",
        ),
        migrations.RenameField(
            model_name="pivotconfig",
            old_name="field",
            new_name="field_to_compare",
        ),
        migrations.AlterUniqueTogether(
            name="pivotconfig",
            unique_together=set(),
        ),
        migrations.AddField(
            model_name="pivotconfig",
            name="config",
            field=models.JSONField(
                default=api_app.defaults.config_default,
            ),
        ),
        migrations.AddField(
            model_name="pivotconfig",
            name="execute_on_python_module",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="pivots",
                to="api_app.pythonmodule",
            ),
        ),
        migrations.AddField(
            model_name="pivotconfig",
            name="python_module",
            field=models.ForeignKey(
                null=True,
                blank=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="%(class)ss",
                to="api_app.pythonmodule",
            ),
        ),
        migrations.AlterUniqueTogether(
            name="pivotconfig",
            unique_together={
                ("python_module", "execute_on_python_module", "playbook_to_execute"),
                ("name",),
            },
        ),
        migrations.AddField(
            model_name="pivotreport",
            name="config",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="reports",
                to="pivots_manager.pivotconfig",
            ),
        ),
        migrations.AddField(
            model_name="pivotreport",
            name="job",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="%(class)ss",
                to="api_app.job",
            ),
        ),
        migrations.AlterUniqueTogether(
            name="pivotreport",
            unique_together={("config", "job")},
        ),
    ]