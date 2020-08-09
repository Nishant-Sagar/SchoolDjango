from django.forms import ModelForm
from .models import Admission

class AdmissionForm(ModelForm):
    class Meta:
        model = Admission
        fields = ['name','father_name','guardian_name','occupation','dob','phone','email','qualification','address','city','pincode','religion','sex','nationality']