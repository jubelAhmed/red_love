from django.db import models
from django.urls import reverse
from django.utils.html import format_html
import datetime
from django.utils.dateparse import parse_date

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
class Donor(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15,unique=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    blood_group = models.CharField(max_length=4,choices=BLOOD_GROUP, default='o+')
    birth_date = models.DateField(null=True, blank=True)
    present_address = models.CharField(max_length=255)
    permanent_address = models.CharField(max_length=255,null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES,default='d')
    blood_donor_status = models.BooleanField(default=True,help_text='Ready Now?',verbose_name="Is Physical Condition Good ?")
    objects = models.QuerySet()
    
    class Meta:
        ordering=['-created_date']
        verbose_name = 'Donor List'

    
    def get_absolute_url(self):
        return reverse('donor-detail',args=[str(self.id)])
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
        print(obj)
        d_date = ''
        for ob in obj:
            d_date = ob.donation_date
        return d_date

    def is_physical_condition(self): 
        last_date = self.last_donation_date()
        day_count = 0
        if last_date:
            delta = datetime.date.today() - parse_date(str(last_date))
            day_count = delta.days
            if day_count>40:
                return True
            else:
                return False
        else:
             return True
         
             
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
    


