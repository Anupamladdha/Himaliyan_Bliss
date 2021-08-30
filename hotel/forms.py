from django import forms
from django.core.exceptions import ValidationError

import datetime



class AvailabilityForm(forms.Form):
    check_in=forms.DateField(required=True,input_formats=["%Y-%m-%d"])
    check_out=forms.DateField(required=True,input_formats=["%Y-%m-%d"])
