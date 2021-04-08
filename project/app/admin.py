from django.contrib import admin
from . models import *

# Register your models here.
class ImageAdmin(admin.ModelAdmin):
	list_display=('BROWSE',)

admin.site.register(Image,ImageAdmin)

class StudentAdmin(admin.ModelAdmin):
	list_display=('SNO',)


admin.site.register(Student,StudentAdmin)


