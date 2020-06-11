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