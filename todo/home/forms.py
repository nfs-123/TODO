from django import forms
from home.models import Task
class TaskRe(forms.ModelForm):
    class Meta:
        model=Task
        fields=['title','desc']
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'desc':forms.Textarea(attrs={'class':'form-control'})
        }
