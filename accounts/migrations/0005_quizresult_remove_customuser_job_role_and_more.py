# Generated by Django 4.1 on 2023-10-21 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_delete_quizresult_customuser_job_role_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuizResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_role', models.CharField(default='Data Annotation Specialist', max_length=100)),
                ('years_of_experience', models.PositiveIntegerField(default=0)),
                ('percentage', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
            ],
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='job_role',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='percentage',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='years_of_experience',
        ),
    ]
