# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Contract(models.Model):
    student = models.ForeignKey('Person', models.DO_NOTHING, related_name='studentid')
    supervisor = models.ForeignKey('Person', models.DO_NOTHING)
    position = models.ForeignKey('Position', models.DO_NOTHING)
    work_term = models.ForeignKey('WorkTerm', models.DO_NOTHING)
    hire_date = models.DateField(blank=True, null=True)
    pay_rate = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    last_pay_increase = models.DateField(blank=True, null=True)
    pay_increase_amount = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    increase_input_date = models.DateField(blank=True, null=True)
    termination_date = models.DateField(blank=True, null=True)
    qualtrics_survey_sent = models.CharField(max_length=7, blank=True, null=True)
    eform_submission_date = models.DateField(blank=True, null=True)
    authorization_to_work_received = models.IntegerField(blank=True, null=True)
    authorization_to_work_sent = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contract'
        verbose_name = 'Contract'
    def __str__(self):
        return('Contract for ' + self.student + '/'+self.supervisor+'/' +self.work_term)


class EmailDefault(models.Model):
    email_id = models.AutoField(primary_key=True)
    email_to_send = models.CharField(max_length=500, blank=True, null=True)
    email_label = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'email_default'
        verbose_name = 'Email Default'
    def __str__(self):
        return(self.email_label)
     

class EmploymentHistory(models.Model):
    student = models.ForeignKey('Person', models.DO_NOTHING)
    employer = models.ForeignKey('PreviousEmployer', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'employment_history'
        verbose_name = 'Employment Historie'
    def __str__(self):
        return('History for' + self.student + '/'+self.supervisor)


class JoinedData(models.Model):
    first_name = models.CharField(max_length=45, blank=True, null=True)
    last_name = models.CharField(max_length=45, blank=True, null=True)
    international = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=6, blank=True, null=True)
    email_address = models.CharField(max_length=100, blank=True, null=True)
    expected_hours = models.IntegerField(blank=True, null=True)
    semester = models.CharField(max_length=6, blank=True, null=True)
    year = models.CharField(max_length=10, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    byu_id = models.CharField(max_length=20, blank=True, null=True)
    position_type = models.CharField(max_length=45, blank=True, null=True)
    position_class = models.CharField(max_length=50, blank=True, null=True)
    class_code = models.CharField(max_length=10, blank=True, null=True)
    empl_record = models.CharField(max_length=1, blank=True, null=True)
    supervisor_first_name = models.CharField(max_length=45, blank=True, null=True)
    supervisor_last_name = models.CharField(max_length=45, blank=True, null=True)
    hire_date = models.DateField(blank=True, null=True)
    pay_rate = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    last_pay_increase = models.DateField(blank=True, null=True)
    pay_increase_amount = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    increase_input_date = models.DateField(blank=True, null=True)
    program_year = models.CharField(max_length=22, blank=True, null=True)
    pays_grad_tuition = models.IntegerField(blank=True, null=True)
    name_change_completed = models.IntegerField(blank=True, null=True)
    notes = models.CharField(max_length=200, blank=True, null=True)
    termination_date = models.DateField(blank=True, null=True)
    qualtrics_survey_sent = models.CharField(max_length=7, blank=True, null=True)
    eform_submission_date = models.DateField(blank=True, null=True)
    authorization_to_work_received = models.IntegerField(blank=True, null=True)
    authorization_to_work_sent = models.DateField(blank=True, null=True)
    byu_last_name = models.CharField(max_length=45, blank=True, null=True)
    byu_first_name = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'joined_data'
        verbose_name = 'Data Point'
    def __str__(self):
        return('All Data for ' + self.first_name + ' '+ self.last_name)
    


class Person(models.Model):
    first_name = models.CharField(max_length=45, blank=True, null=True)
    last_name = models.CharField(max_length=45, blank=True, null=True)
    gender = models.CharField(max_length=6, blank=True, null=True)
    email_address = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'person'
        verbose_name = 'Person'
    def __str__(self):
        return(self.first_name + ' '+ self.last_name)


class Position(models.Model):
    position_type = models.CharField(max_length=45, blank=True, null=True)
    class_code = models.CharField(max_length=10, blank=True, null=True)
    position_class = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'position'
        verbose_name = 'Position'
    
    def __str__(self):
        if self.class_code ==None :
            return str(self.position_type)
        else:
           return(str(self.position_type) + ' '+ str(self.class_code)) 
        


class Posting(models.Model):
    supervisor = models.ForeignKey(Person, models.DO_NOTHING)
    position = models.ForeignKey(Position, models.DO_NOTHING)
    work_term = models.ForeignKey('WorkTerm', models.DO_NOTHING)
    expected_hours = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'posting'
        verbose_name = 'Posting'
    
    def __str__(self):
        return('Posting for' + self.supervisor + '/'+self.position + '/'+self.work_term)


class PreviousEmployer(models.Model):
    employer_name = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'previous_employer'
        verbose_name = 'Previous Employer'
    def __str__(self):
        return(self.employer_name)
    


class Students(models.Model):
    id = models.OneToOneField(Person, models.DO_NOTHING, db_column='id', primary_key=True)
    byu_first_name = models.CharField(max_length=45, blank=True, null=True)
    byu_last_name = models.CharField(max_length=45, blank=True, null=True)
    international = models.IntegerField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    byu_id = models.CharField(max_length=20, blank=True, null=True)
    empl_record = models.CharField(max_length=1, blank=True, null=True)
    program_year = models.CharField(max_length=22, blank=True, null=True)
    pays_grad_tuition = models.IntegerField(blank=True, null=True)
    name_change_completed = models.IntegerField(blank=True, null=True)
    notes = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'students'
        verbose_name = 'Student'
    
    def __str__(self):
        return(self.byu_first_name + ' '+ self.byu_last_name)
    


class Supervisors(models.Model):
    id = models.OneToOneField(Person, models.DO_NOTHING, db_column='id', primary_key=True)

    class Meta:
        managed = False
        db_table = 'supervisors'
        verbose_name = 'Supervisor'
    
    def __str__(self):
        return(str(self.id) )


class WorkTerm(models.Model):
    semester = models.CharField(max_length=6, blank=True, null=True)
    year = models.CharField(max_length=10, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'work_term'
        verbose_name = 'Semester/Year Term'
    def __str__(self):
        return(self.semester + ' '+ self.year)