from django.contrib import admin
from .models import Contract, EmploymentHistory, JoinedData, Person, Position, Posting, PreviousEmployer, Students, Supervisors, WorkTerm
 
admin.site.register(Contract)
class RequestDemoAdmin(admin.ModelAdmin):
  list_display = [field.name for field in
Contract._meta.get_fields()]

admin.site.register(EmploymentHistory)
class RequestDemoAdmin(admin.ModelAdmin):
  list_display = [field.name for field in
EmploymentHistory._meta.get_fields()]

admin.site.register(JoinedData)
class RequestDemoAdmin(admin.ModelAdmin):
  list_display = [field.name for field in
JoinedData._meta.get_fields()]


admin.site.register(Person)
class RequestDemoAdmin(admin.ModelAdmin):
  list_display = [field.name for field in
Person._meta.get_fields()]

admin.site.register(Position)
class RequestDemoAdmin(admin.ModelAdmin):
  list_display = [field.name for field in
Position._meta.get_fields()]


admin.site.register(Posting)
class RequestDemoAdmin(admin.ModelAdmin):
  list_display = [field.name for field in
Posting._meta.get_fields()]

admin.site.register(PreviousEmployer)
class RequestDemoAdmin(admin.ModelAdmin):
  list_display = [field.name for field in
PreviousEmployer._meta.get_fields()]

admin.site.register(Students)
class RequestDemoAdmin(admin.ModelAdmin):
  list_display = [field.name for field in
Students._meta.get_fields()]

admin.site.register(Supervisors)
class RequestDemoAdmin(admin.ModelAdmin):
  list_display = [field.name for field in
Supervisors._meta.get_fields()]

admin.site.register(WorkTerm)
class RequestDemoAdmin(admin.ModelAdmin):
  list_display = [field.name for field in
WorkTerm._meta.get_fields()]

