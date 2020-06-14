from django.contrib import admin
from django.utils.html import format_html
import datetime
from django.utils.dateparse import parse_date
from simple_history.admin import SimpleHistoryAdmin
from image_cropping import ImageCroppingMixin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export.forms import ConfirmImportForm,ImportForm
from import_export.admin import ImportMixin

from django.contrib.contenttypes.admin import GenericTabularInline



from .models import Donor,BloodDonation,Member

# Header and title change
admin.site.site_header = 'Red Love Blood Society Admin' 
admin.site.site_title = 'Red Love Blood Society Portal' 
admin.site.index_title = 'Congratulation to join with RLBS'

# Register your models here.
 

class BloodDonationInline(admin.TabularInline):
    model = BloodDonation
    extra = 1 

class DonorInline(admin.TabularInline):
    model = Donor
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
class DonorAdmin(SimpleHistoryAdmin,ImportExportModelAdmin):
    list_display = ('name','phone','blood_group','physical_condition_next_donation','birth_date','last_donation_date','total_donate','get_status','blood_donor_status')
    list_display_links = ('name', 'blood_group','get_status')
    list_filter = ['created_date','blood_group']
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
    
    
    
    # member 
    
from django import forms

class CustomImportForm(ImportForm):
    donor = forms.ModelChoiceField(
        queryset=Donor.objects.all(),
        required=True)

class CustomConfirmImportForm(ConfirmImportForm):
    donor = forms.ModelChoiceField(
        queryset=Donor.objects.all(),
        required=True)

class MemberResource(resources.ModelResource):
    class Meta:
        model = Member
        # fields = ('id','donor__id','donor__name','donor__phone','donor__email','donor__blood_group','donor__birth_date','donor__present_address','donor__permanent_address','nid_or_birthday_no','father_name','mother_name','educational_status','occupation','facebook_link','image',)   
        widgets = {
                'donor__birth_date': {'format': '%Y-%m-%d'},
                } 

class MemberAdmin(ImageCroppingMixin, SimpleHistoryAdmin,ImportExportModelAdmin):
    # list_display = [field.name for field in Member._meta.fields if field.name != "id" and field.name != "image" and field.name != "cropping"  ]
    list_display = ('donor','donor_group','donor_phone','nid_or_birthday_no','father_name','mother_name','educational_status','occupation','facebook_link','image')
    list_display_links = ('donor','nid_or_birthday_no')
    list_filter = ['created_date']
    # resource_class = MemberResource
    search_fields = ('donor__name','donor__blood_group','nid_or_birthday_no','donor__phone','father_name','mother_name','educational_status')
    date_hierarchy = 'created_date'
    list_per_page = 10
    prepopulated_fields = { 'image': ['cropping']} 

    

    fieldsets = (
        (None,
         
         {
            'classes': ('wide', 'extrapretty'),
            'fields':('donor',('father_name','mother_name'),('occupation','relegion'),'facebook_link')
        }),
        ('others',{
            'fields':('image','cropping')
        }),
    )
    # readonly_fields = ['image_tag']
    
    def get_import_form(self):
        return CustomImportForm

    def get_confirm_import_form(self):
        return CustomConfirmImportForm

    def get_form_kwargs(self, form, *args, **kwargs):
        # pass on `author` to the kwargs for the custom confirm form
        if isinstance(form, CustomImportForm):
            if form.is_valid():
                donor = form.cleaned_data['donor']
                kwargs.update({'donor': donor.id})
        return kwargs


    
admin.site.register(Member,MemberAdmin)








# Proxy Model  start

# def create_modeladmin(modeladmin, model, name = None):
#     class  Meta:
#         proxy = True
#         app_label = model._meta.app_label

#     attrs = {'__module__': '', 'Meta': Meta}

#     newmodel = type(name, (model,), attrs)

#     admin.site.register(newmodel, modeladmin)
#     return modeladmin

# class MemberInline(admin.TabularInline):
#     model = Member
#     extra = 1   
  

# class DonorMemberAdmin(SimpleHistoryAdmin,ImportExportModelAdmin):
   
#     # fields = ['name','phone',('blood_group','birth_date')]
#     inlines = [MemberInline]
    
        
# class MyPostAdmin(admin.ModelAdmin):
#     def get_queryset(self, request):
#         return self.model.objects.all()
    
    
# class MyPostAdmin(DonorMemberAdmin):
#     def get_queryset(self, request):
#         return self.model.objects.filter()

# create_modeladmin(MyPostAdmin, name='Redlove_Member', model=Donor)
    
# admin.site.register(DonorMemberAdmin, MyPostAdmin)

# Proxy Model  ENd



  
    
