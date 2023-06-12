from django.contrib import admin
from .models import Jobs
# Register your models here.
class JobModelAdmin(admin.ModelAdmin):
    list_display = ['jobid','title','skills','description']
    list_filter = ['title']
    class Meta:
        model=Jobs
admin.site.register(Jobs,JobModelAdmin)
