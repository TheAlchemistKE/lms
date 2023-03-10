# Generated by Django 4.1.7 on 2023-02-17 10:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Exam",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100)),
                ("description", models.CharField(max_length=100)),
                ("type", models.CharField(max_length=100)),
                ("administer_date", models.DateField()),
                ("created_at", models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Question",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "exam",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="exams.exam"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="AnswerOptions",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("option_text", models.CharField(max_length=100)),
                ("created_at", models.DateField(auto_now_add=True)),
                (
                    "question",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="exams.question"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Answer",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("created_at", models.DateField(auto_now_add=True)),
                (
                    "question",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="exams.question"
                    ),
                ),
            ],
        ),
    ]
