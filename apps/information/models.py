from django.db import models
from simple_history.models import HistoricalRecords
from django.conf import settings

# Create your models here.


class BloodInformation(models.Model):
    quetion = models.CharField(max_length=255)
    answer = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True,help_text='Want to published ?',)
    history = HistoricalRecords()
    changed_by = models.ForeignKey(settings.AUTH_USER_MODEL,models.SET_NULL,null=True,blank=True)
    objects = models.QuerySet()
    
    class Meta:
        ordering=['created_date']
        verbose_name = 'Blood Related Quetions & Answer'
    
    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value
        
        
    def __str__(self):
        return self.quetion + '-' +self.answer
        
class Message(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    message = models.TextField()
    email = models.EmailField(null=True,blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    history = HistoricalRecords()
    changed_by = models.ForeignKey(settings.AUTH_USER_MODEL,models.SET_NULL,null=True,blank=True)
    objects = models.QuerySet()
    
    class Meta:
        ordering=['-created_date']
        verbose_name = 'Message'
    
    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value
        
    def __str__(self):
        return self.name + '-'+self.phone + '-'+self.message
    



class PhoneList(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.name} - {self.phone}"
    

class EmailList(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.name} - {self.email}"
    
class OrgContact(models.Model):
    phonelist = models.ManyToManyField(
        PhoneList
    )
    emaillist = models.ManyToManyField(
        EmailList
    )
    address = models.CharField(max_length=255)
    fb_group_link = models.URLField(max_length=1000)
    # channel_link = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def phone_list_view(self):
        phones = self.phonelist.all()[0:3]
        phones_str = ''
        for p in phones:
            phones_str = phones_str + str(p.phone) +' , '
        return phones_str
    def email_list_view(self):
        emails = self.emaillist.all()[0:3]
        email_str = ''
        for e in emails:
            email_str = email_str + str(e.email) +' , '
        return email_str
    
    def __str__(self):
        return f"{self.fb_group_link} - {self.address}"

