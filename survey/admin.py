from django.contrib import admin
from survey.models import Poll, Response


# Register your models here.
class ResponseAdmin(admin.ModelAdmin):
    list_display = ['answer', 'question']

admin.site.register(Poll)
admin.site.register(Response, ResponseAdmin)