from django.contrib import admin

from .models import Bb

class BbAdmin(admin.ModelAdmin):
	list_display = ('title', 'content',)

admin.site.register(Bb, BbAdmin)
# Register your models here.
