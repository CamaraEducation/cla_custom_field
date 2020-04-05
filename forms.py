from .models import ExtraInfo
from django.forms import ModelForm

class ExtraInfoForm(ModelForm):

    class Meta(object):
        model = ExtraInfo
        fields = ('school_name', )