from django.contrib.auth import login
from django.views.generic import CreateView
from django.shortcuts import get_object_or_404, redirect, render

from ..forms import StudentSignUpDetailForm
from ..models import User

class StdetailSignUpView(CreateView):
    model = User
    form_class = StudentSignUpDetailForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'student_details'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        # print(form)
        user = form.save()
        login(self.request, user)
        return redirect('students:quiz_list')