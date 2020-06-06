from django.db import models
from django.urls import reverse

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
class Donor(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15,unique=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    blood_group = models.CharField(max_length=4,choices=BLOOD_GROUP, default='o+')
    birth_date = models.DateField(null=True, blank=True)
    present_address = models.CharField(max_length=255)
    permanent_address = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)
    blood_donor_status = models.BooleanField(default=True)
    objects = models.QuerySet()
    
    class Meta:
        ordering=['name','blood_group']
    
    def get_absolute_url(self):
        return reverse('donor-detail',args=[str(self.id)])
    
    def __str__(self):
        return f"{self.name}"
    



