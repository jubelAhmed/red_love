from django.db import models
from django.conf import settings

from django.urls import reverse
from django.utils.html import format_html
import datetime
from django.utils.dateparse import parse_date
from simple_history.models import HistoricalRecords
from image_cropping import ImageRatioField


# Create your models here.



BLOOD_GROUP = (
    ('o+',"O+"),
    ('o-',"O-"),
    ('a+',"A+"),
    ('a-',"A-"),
    ('b+',"B+"),
    ('b-',"B-"),
    ('ab+',"AB+"),
    ('ab-',"AB-"), 
        
)

STATUS_CHOICES = [
    ('d', 'Draft'),
    ('p', 'Published'),
]

class ContactInfo(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15,unique=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    blood_group = models.CharField(max_length=4,choices=BLOOD_GROUP, default='o+')
    birth_date = models.DateField()
    present_address = models.CharField(max_length=255)
    permanent_address = models.CharField(max_length=255,null=True, blank=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES,default='d')
    class Meta:
        abstract = True
class Donor(ContactInfo):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    blood_donor_status = models.BooleanField(default=True,help_text='Your health is good?',verbose_name="Health Good")
    history = HistoricalRecords()
    changed_by = models.ForeignKey(settings.AUTH_USER_MODEL,models.SET_NULL,null=True,blank=True)
    objects = models.QuerySet()
    
    class Meta(ContactInfo.Meta):
        ordering=['-created_date']
        verbose_name = 'Donor List'
    
    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value
    
    # def get_absolute_url(self):
    #     return reverse('donor-detail',args=[str(self.id)])
    def get_status(self):
        color_code = '#ffffff'
        status = ''
        if self.status == 'd':
            status = 'Draft'
            color_code = 'red'
        elif self.status == 'p':
            status = 'Published'
            color_code = 'blue' 
        return format_html(     
            '<span style="color: {};">{}</span>',
            color_code,
            status,
        )
    
    get_status.short_description = "Status"

    
    def total_donate(self):
        return self.blood_donation_details.all().count()
    
    def last_donation_date(self):
        obj = self.blood_donation_details.order_by('-created_date').filter()[:1]
        d_date = ''
        for ob in obj:
            d_date = ob.donation_date
        return d_date
    @property
    def is_physical_condition(self): 
        last_date = self.last_donation_date()
        day_count = 0
        if last_date:
            delta = datetime.date.today() - parse_date(str(last_date))
            day_count = delta.days
            if day_count>=120:
                return True
            else:
                return False
        else:
             return self.blood_donor_status
         
             
    def __str__(self):
        return f"{self.name}"
    
class BloodDonation(models.Model):
    donor = models.ForeignKey(Donor, on_delete=models.CASCADE,related_name='blood_donation_details')
    donation_date = models.DateField()
    patient_type = models.CharField(max_length=255,null=True,blank=True,help_text='Operation')
    hospital_name = models.CharField(max_length=255,null=True,blank=True,help_text='Osmani Medical College')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering=['created_date','updated_date']

    def __str__(self):
        return f"{self.donor.name + ' '+ str(self.donation_date)}"
    

RELEGION_CHOICES = [
    ('i', 'Islam'),
    ('h', 'Hindu'),
    ('k', 'Khristan'),
    ('o', 'Others'),
]

CURRENT_POSITION_CHOICES = [
    ('running', 'Running'),
    ('retired', 'Retired')
]

COMITTEE_POSITION_CHOICES = [
    ('member', 'সদস্য'),
    ('permanent_member', 'স্থায়ী কমিটি সদস্য'),
    ('chairmen', 'সভাপতি'),
    ('vice_chairmen', 'সহ-সভাপতি'),
    ('senior_vice_chairmen', 'সিনিয়র সহ-সভাপতি'),
    ('general_secretary', 'সাধারণ সম্পাদক'),
    ('organizational_secretary', 'সাংগঠনিক সম্পাদক'),
    ('finance_secretary', 'অর্থ সম্পাদক'),
    ('EducationAndSocialWelfareSecretary', 'শিক্ষা ও সমাজ কল্যাণ সম্পাদক'),
    ('religion_secretary', 'ধর্ম সম্পাদক'),
    ('InformationAndPlanningSecretary', 'তথ্য ও পরিকল্পনা সম্পাদক'),
    ('finance_secretary', 'অর্থ সম্পাদক'),
    ('office_secretary', 'অফিস সম্পাদক'),
    ('BloodCoordinator', 'ব্লাড সমন্বয়ক'),
    ('executive_member', 'নির্বাহী সদস্য'),
    ('HealthSecretary', 'স্বাস্থ্য সম্পাদক'),
    ('Co-GeneralSecretary', 'সহ-সাধারন সম্পাদক'),
    ('Co-OrganizingSecretary', 'সহ-সাংগঠনিক সম্পাদক'),
    ('MemberSecretary', 'সদস্য সচিব'),
    ('international_secretary', 'আন্তর্জাতিক সম্পাদক'),
    
]

class Member(models.Model):
    donor = models.OneToOneField(Donor, on_delete=models.CASCADE,related_name='org_member',verbose_name="Related Donor Info")
    nid_or_birthday_no = models.CharField(max_length=100,help_text='Add your NID number or Birthday Number',null=True,blank=True)
    father_name = models.CharField(max_length=250)
    mother_name = models.CharField(max_length=250)
    educational_status = models.CharField(max_length=250,help_text='S.S.C or H.S.C or B.S.C')
    occupation = models.CharField(max_length=250,help_text='Student / Business / Farmer /..')
    relegion = models.CharField(max_length=1, choices=RELEGION_CHOICES,default='i')
    running_position_status = models.CharField(max_length=10, choices=CURRENT_POSITION_CHOICES,default='running')
    facebook_link = models.CharField(max_length=1000,null=True,blank=True)
    organisation_position = models.CharField(max_length=100, choices=COMITTEE_POSITION_CHOICES,default='member')
    image = models.ImageField(upload_to='images/member/')
    # size is "width x height"
    cropping = ImageRatioField('image', '400x300',size_warning=True)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True) 
    changed_by = models.ForeignKey(settings.AUTH_USER_MODEL,models.SET_NULL,null=True,blank=True)
    history = HistoricalRecords()
    
    class Meta:
        ordering = ['created_date']
    
    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value
        
    def donor_name(self):
        return self.donor.name
    donor_name.short_description = 'Name'

    def donor_group(self):
        return self.donor.blood_group
    donor_group.short_description = 'Blood Group'
    def donor_phone(self):
        return self.donor.phone
    donor_phone.short_description = 'Phone'

    def donor_status(self):
        return self.donor.status
    donor_status.short_description = 'Donate Status'
    
    # def image_tag(self):
    #     return format_html('<img src="{}" />'.format(self.image.url))

    # image_tag.short_description = 'Image Privew'
    # image_tag.allow_tags = True

    def __str__(self):
        return f"{ self.donor.name +' - ' +self.donor.phone}"
    


class OrgMemorie(models.Model):
    title = models.CharField(max_length=250,null=True,blank=True)
    place = models.CharField(max_length=250,null=True,blank=True)
    image = models.ImageField(upload_to='images/memories/')
    # size is "width x height"
    cropping = ImageRatioField('image', '1200x800',free_crop=True)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True) 
    changed_by = models.ForeignKey(settings.AUTH_USER_MODEL,models.SET_NULL,null=True,blank=True)
    history = HistoricalRecords()
    
    class Meta:
        ordering = ['-created_date']
    
    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value
        
    def __str__(self):
        return f"{self.image} {self.created_date}"