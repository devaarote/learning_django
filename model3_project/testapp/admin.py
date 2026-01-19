from django.contrib import admin
from testapp.models import employee

# class employeeAdmin(admin.ModelAdmin):
#     list_display=['id','eno','ename','esal']

# Register your models here.
# admin.site.register(employee,employeeAdmin)

admin.site.register(employee)