# Generated by Django 2.2.24 on 2022-06-20 21:52

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("models", "8022_userprofile_mfa_hash"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="mobilesurveymodel",
            name="cards",
        ),
        migrations.RemoveField(
            model_name="mobilesurveymodel",
            name="createdby",
        ),
        migrations.RemoveField(
            model_name="mobilesurveymodel",
            name="groups",
        ),
        migrations.RemoveField(
            model_name="mobilesurveymodel",
            name="lasteditedby",
        ),
        migrations.RemoveField(
            model_name="mobilesurveymodel",
            name="users",
        ),
        migrations.AlterUniqueTogether(
            name="mobilesurveyxcard",
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name="mobilesurveyxcard",
            name="card",
        ),
        migrations.RemoveField(
            model_name="mobilesurveyxcard",
            name="mobile_survey",
        ),
        migrations.AlterUniqueTogether(
            name="mobilesurveyxgroup",
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name="mobilesurveyxgroup",
            name="group",
        ),
        migrations.RemoveField(
            model_name="mobilesurveyxgroup",
            name="mobile_survey",
        ),
        migrations.AlterUniqueTogether(
            name="mobilesurveyxuser",
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name="mobilesurveyxuser",
            name="mobile_survey",
        ),
        migrations.RemoveField(
            model_name="mobilesurveyxuser",
            name="user",
        ),
        migrations.RemoveField(
            model_name="mobilesynclog",
            name="survey",
        ),
        migrations.RemoveField(
            model_name="tilerevisionlog",
            name="survey",
        ),
        migrations.RemoveField(
            model_name="tilerevisionlog",
            name="synclog",
        ),
        migrations.DeleteModel(
            name="MobileSurvey",
        ),
        migrations.RemoveField(
            model_name="resourcerevisionlog",
            name="survey",
        ),
        migrations.RemoveField(
            model_name="resourcerevisionlog",
            name="synclog",
        ),
        migrations.DeleteModel(
            name="MobileSurveyModel",
        ),
        migrations.DeleteModel(
            name="MobileSurveyXCard",
        ),
        migrations.DeleteModel(
            name="MobileSurveyXGroup",
        ),
        migrations.DeleteModel(
            name="MobileSurveyXUser",
        ),
        migrations.DeleteModel(
            name="MobileSyncLog",
        ),
        migrations.DeleteModel(
            name="TileRevisionLog",
        ),
    ]
