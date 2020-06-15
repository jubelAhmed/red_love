from django.contrib import admin
# Register your models here.
from django.utils.html import format_html
import datetime
from django.utils.dateparse import parse_date
from simple_history.admin import SimpleHistoryAdmin

from .models import BloodInformation,Message,OrgContact,EmailList,PhoneList


class BloodInformationAdmin(SimpleHistoryAdmin):
    # list_display = [field.name for field in Member._meta.fields if field.name != "id" and field.name != "image" and field.name != "cropping"  ]
    list_display = ('quetion','answer','created_date')
    list_display_links = ('quetion','created_date')
    list_filter = ['created_date']
    # resource_class = MemberResource
    search_fields = ('quetion','created_date')
    date_hierarchy = 'created_date'
    list_per_page = 10

admin.site.register(BloodInformation,BloodInformationAdmin)

class MessageAdmin(SimpleHistoryAdmin):
    # list_display = [field.name for field in Member._meta.fields if field.name != "id" and field.name != "image" and field.name != "cropping"  ]
    list_display = ('name','phone','message','email','created_date')
    list_display_links = ('name','created_date')
    list_filter = ['created_date']
    # resource_class = MemberResource
    search_fields = ('name','phone','created_date')
    date_hierarchy = 'created_date'
    list_per_page = 10

admin.site.register(Message,MessageAdmin)



@admin.register(OrgContact)
class DonorAdmin(SimpleHistoryAdmin):
    list_display = ('address','fb_group_link','phone_list_view','email_list_view')
    # fields = ['name','phone',('blood_group','birth_date')]

    
# admin.site.register(OrgContact)
admin.site.register(EmailList)
admin.site.register(PhoneList)