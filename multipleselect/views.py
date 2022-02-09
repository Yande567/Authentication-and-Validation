from django.urls import reverse_lazy
from .models import *
from .forms import ApplicationForm
from django.views.generic import CreateView


class ApplicationForm(CreateView):
    model = Requirements
    form_class = ApplicationForm
    template_name = 'requirements/job_specs.html'
    success_url = reverse_lazy('home')

    # Passes the request object to forms
    def get_form_kwargs(self):
        kwargs = super(ApplicationForm, self).get_form_kwargs()
        kwargs['job_title'] = self.kwargs.get('job_title')
        return kwargs
