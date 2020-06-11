from django.contrib import admin
from django.utils.html import format_html
import datetime
from django.utils.dateparse import parse_date
from simple_history.admin import SimpleHistoryAdmin

from .models import Donor,BloodDonation,Member

# Header and title change
admin.site.site_header = 'Red Love Blood Society Admin' 
admin.site.site_title = 'Red Love Blood Society Portal' 
admin.site.index_title = 'Congratulation to join with RLBS'

# Register your models here.
 

class BloodDonationInline(admin.TabularInline):
    model = BloodDonation
    extra = 1   

# draft and publishd
def make_published(modeladmin, request, queryset):
    queryset.update(status='p')
    
make_published.short_description = "Mark selected donor as published"

def make_draft(modeladmin, request, queryset):
    queryset.update(status='d')
    
make_draft.short_description = "Mark selected donor as draft"


# physical condition good or bad


    
def make_physical_good(modeladmin, request, queryset):
    queryset.update(blood_donor_status = True)
    
make_physical_good.short_description = "Make selected donor physical condition good"

def make_physical_bad(modeladmin, request, queryset):
    queryset.update(blood_donor_status = False)
    
make_physical_bad.short_description = 'Make selected donor physical condition bad'
        

@admin.register(Donor)
class DonorAdmin(SimpleHistoryAdmin):
    list_display = ('name','phone','blood_group','physical_condition_next_donation','birth_date','last_donation_date','total_donate','get_status','blood_donor_status')
    list_display_links = ('name', 'blood_group','get_status')
    list_filter = ['blood_group']
    search_fields = ('name','phone','blood_group','status')
    # fields = ['name','phone',('blood_group','birth_date')]
    inlines = [BloodDonationInline]
    date_hierarchy = 'created_date'
    actions = [make_published,make_draft]
    list_per_page = 10
    
    # class Media:
    #         css = {
    #             "screen": ("css/override.css",)
    #         }
    #         js = ("custom/js/admin/donor.js",)
    

    fieldsets = (
        (None,
         
         {
            'classes': ('wide', 'extrapretty'),
            'fields':(('name','phone','blood_group'),('present_address','permanent_address'),'status')
        }),
        ('others',{
            'fields':('birth_date','blood_donor_status')
        }),
        
    )
    
    def physical_condition_next_donation(self,obj):
        if obj.is_physical_condition:
            return format_html(     
                '<img src="/static/admin/img/icon-yes.svg" alt="True">',
            )
        else:
             return format_html(     
                '<img src="/static/admin/img/icon-no.svg" alt="False">',
            )
         
    physical_condition_next_donation.short_description = 'Next Donate Time Reached'
    
    

admin.site.register(Member,SimpleHistoryAdmin)


  
    
