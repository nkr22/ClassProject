# Generated by Django 4.1.2 on 2022-11-07 00:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hire_date', models.DateField(blank=True, null=True)),
                ('pay_rate', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('last_pay_increase', models.DateField(blank=True, null=True)),
                ('pay_increase_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('increase_input_date', models.DateField(blank=True, null=True)),
                ('termination_date', models.DateField(blank=True, null=True)),
                ('qualtrics_survey_sent', models.CharField(blank=True, max_length=7, null=True)),
                ('eform_submission_date', models.DateField(blank=True, null=True)),
                ('authorization_to_work_received', models.BooleanField(blank=True, null=True)),
                ('authorization_to_work_sent', models.DateField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Contract',
                'db_table': 'contract',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EmploymentHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Employment History',
                'verbose_name_plural': 'Employment Histories',
                'db_table': 'employment_history',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='JoinedData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=45, null=True)),
                ('last_name', models.CharField(blank=True, max_length=45, null=True)),
                ('international', models.BooleanField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, max_length=6, null=True)),
                ('email_address', models.CharField(blank=True, max_length=100, null=True)),
                ('expected_hours', models.IntegerField(blank=True, null=True)),
                ('semester', models.CharField(blank=True, max_length=6, null=True)),
                ('year', models.CharField(blank=True, max_length=10, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('byu_id', models.CharField(blank=True, max_length=20, null=True)),
                ('position_type', models.CharField(blank=True, max_length=45, null=True)),
                ('position_class', models.CharField(blank=True, max_length=50, null=True)),
                ('class_code', models.CharField(blank=True, max_length=10, null=True)),
                ('empl_record', models.CharField(blank=True, choices=[(0, '0'), (1, '1'), (3, '3'), (2, '2')], max_length=1, null=True)),
                ('supervisor_first_name', models.CharField(blank=True, max_length=45, null=True)),
                ('supervisor_last_name', models.CharField(blank=True, max_length=45, null=True)),
                ('hire_date', models.DateField(blank=True, null=True)),
                ('pay_rate', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('last_pay_increase', models.DateField(blank=True, null=True)),
                ('pay_increase_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('increase_input_date', models.DateField(blank=True, null=True)),
                ('program_year', models.CharField(blank=True, max_length=22, null=True)),
                ('pays_grad_tuition', models.BooleanField(blank=True, null=True)),
                ('name_change_completed', models.BooleanField(blank=True, null=True)),
                ('notes', models.CharField(blank=True, max_length=200, null=True)),
                ('termination_date', models.DateField(blank=True, null=True)),
                ('qualtrics_survey_sent', models.CharField(blank=True, max_length=7, null=True)),
                ('eform_submission_date', models.DateField(blank=True, null=True)),
                ('authorization_to_work_received', models.BooleanField(blank=True, null=True)),
                ('authorization_to_work_sent', models.DateField(blank=True, null=True)),
                ('byu_last_name', models.CharField(blank=True, max_length=45, null=True)),
                ('byu_first_name', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'verbose_name': 'Data Point',
                'db_table': 'joined_data',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=45, null=True)),
                ('last_name', models.CharField(blank=True, max_length=45, null=True)),
                ('gender', models.CharField(blank=True, max_length=6, null=True)),
                ('email_address', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Person',
                'db_table': 'person',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position_type', models.CharField(blank=True, max_length=45, null=True)),
                ('class_code', models.CharField(blank=True, max_length=10, null=True)),
                ('position_class', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'verbose_name': 'Position',
                'db_table': 'position',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Posting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expected_hours', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Posting',
                'db_table': 'posting',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PreviousEmployer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employer_name', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'verbose_name': 'Previous Employer',
                'db_table': 'previous_employer',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='WorkTerm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.CharField(blank=True, max_length=6, null=True)),
                ('year', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'verbose_name': 'Semester/Year Term',
                'db_table': 'work_term',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('Student', models.OneToOneField(db_column='id', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='newapp.person')),
                ('byu_first_name', models.CharField(blank=True, max_length=45, null=True)),
                ('byu_last_name', models.CharField(blank=True, max_length=45, null=True)),
                ('international', models.BooleanField(blank=True, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('byu_id', models.CharField(blank=True, max_length=20, null=True)),
                ('empl_record', models.CharField(blank=True, choices=[(0, '0'), (1, '1'), (3, '3'), (2, '2')], max_length=1, null=True)),
                ('program_year', models.CharField(blank=True, max_length=22, null=True)),
                ('pays_grad_tuition', models.BooleanField(blank=True, null=True)),
                ('name_change_completed', models.BooleanField(blank=True, null=True)),
                ('notes', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'verbose_name': 'Student',
                'db_table': 'students',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Supervisors',
            fields=[
                ('Supervisor', models.OneToOneField(db_column='id', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='newapp.person')),
            ],
            options={
                'verbose_name': 'Supervisor',
                'db_table': 'supervisors',
                'managed': False,
            },
        ),
    ]