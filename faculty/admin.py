from django.contrib import admin
from .models import HomePage, Department, Program, Teacher, ExchangeProgram

admin.site.register(HomePage)
admin.site.register(Department)
admin.site.register(Program)
admin.site.register(Teacher)


@admin.register(ExchangeProgram)
class ExchangeAdmin(admin.ModelAdmin):
    list_display = ('university', 'country', 'seats', 'deadline')