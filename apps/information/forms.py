from django import forms
from .models import Message
from django.utils.translation import ugettext_lazy as _


class MessageReqForm(forms.ModelForm):
    # org_details = forms.ModelChoiceField(orgDetail.objects.all())
    class Meta:
        model = Message
        fields = ('name', 'phone', 'email', 'message')
        labels = {
            'name': _('আপনার নাম'),
            'phone': _('মোবাইল'),
            'email': _('ইমেইল (যদি থাকে) '),
            'message': _('বিস্থারিত'),
           
        }