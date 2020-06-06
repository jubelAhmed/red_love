from django.contrib import admin

from .models import Donor

# Header and title change
admin.site.site_header = 'Red Love Blood Society' 
admin.site.site_title = 'Red Love Blood Society' 
admin.site.index_title = 'Red Love Blood Society'

# Register your models here.
 
@admin.register(Donor)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name','phone','blood_group','status','birth_date')
    list_display_links = ('name', 'blood_group')
    search_fields = ('name','phone','blood_group','status')
   
