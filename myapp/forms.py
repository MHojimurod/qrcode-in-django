from django import forms
from .models import YourModel
class YOurMOdelForm(forms.ModelForm):
    class Meta:
        model = YourModel
        fields = "__all__"