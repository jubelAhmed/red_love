from django import forms
from . import models
from django.utils.translation import ugettext_lazy as _

from django.contrib.admin.widgets import AdminDateWidget,AdminSplitDateTime
from donation import settings
from django.forms.fields import DateField



class DonorRegForm(forms.ModelForm):
    birth_date = DateField(
        input_formats=['%Y-%m-%d'],
        widget=forms.DateInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1',
            'id': 'id_birth_date',
            
        })
    )
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
