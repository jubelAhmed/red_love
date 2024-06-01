from django import forms
from . import models
from django.utils.translation import ugettext_lazy as _

from django.contrib.admin.widgets import AdminDateWidget,AdminSplitDateTime
from django.forms.fields import DateField

class DateInput(forms.DateInput):
    input_type = 'date'

class DonorRegForm(forms.ModelForm):
    birth_date = DateField(widget=DateInput(attrs={'class':'dateinput form-control'}))
    class Meta:
        model = models.Donor
        fields = ('name', 'phone', 'email', 'blood_group', 'birth_date', 'present_address', 'permanent_address')
        labels = {
            'name': _('আপনার নাম'),
            'phone': _('মোবাইল'),
            'email': _('ইমেইল'),
            'blood_group': _('রক্তের গ্রুপ'),
            'birth_date': _('জন্ম তারিখ'),
            'present_address': _('বর্তমান ঠিকানা'),
            'permanent_address': _('স্থায়ী ঠিকানা'),
            
        }
