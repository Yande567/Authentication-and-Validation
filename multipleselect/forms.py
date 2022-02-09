from django import forms
from .models import *


class ApplicationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.job_title = kwargs.pop('job_title')
        super(ApplicationForm, self).__init__(*args, **kwargs)
        get_data = self.job_title
        dic = {'job_title__job_title': get_data}
        self.fields['qualifications'].queryset = Requirements.objects.filter(**dic)

    class Meta:
        model = Applicants
        fields = ['email', 'qualifications']

    email = forms.EmailField(label='', max_length=100, required=True, widget=forms.TextInput(
        attrs={'class': 'form-group form-control input-lg ', 'placeholder': 'Email'}), )
    qualifications = forms.ModelMultipleChoiceField(queryset=None, widget=forms.CheckboxSelectMultiple)
