from django.contrib import admin

# Register your models here.
from .models import Interview


class InterviewAdmin(admin.ModelAdmin):
	fields = ['source','employee']
	list_display = ('int_date','source','employee')
	list_filter = ['int_date']
	search_fields = ['source','employee']
admin.site.register(Interview, InterviewAdmin)