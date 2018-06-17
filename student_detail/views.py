from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from .models import Student
from .forms import StudentAdmissionForm


# Create your views here.
class StudentCreateView(CreateView):
    model = Student
    form_class = StudentAdmissionForm
    template_name = "addstudent.html"
    success_url = "/studentlist/"

    def form_valid(self, form):
        print(self.request.user)
        students = form.save(commit=False)
        students.owner = self.request.user
        return super(StudentCreateView,self).form_valid(form)

    def get_context_data(self, *args,**kwargs):
        context = super(StudentCreateView, self).get_context_data(*args, **kwargs)
        return context


class StudentListView(ListView):
    model = Student
    #ordering = ('name',)
    context_object_name = 'lists'
    template_name = 'studentlist_list.html'

    def get_queryset(self):
        return Student.objects.all()

class StudentDetailsView(DetailView):
    template_name = 'studentlist_detail.html'

    # def get_object(self):
    #     primarykey = self.kwargs.get('pk')
    #     print(primarykey)
    #     return get_object_or_404(primarykey, pk=primarykey)

    def get_context_data(self,*args, **kwargs):
        context = super(StudentDetailsView, self).get_context_data(*args, **kwargs)
        context['now'] = timezone.now()
        return context

    def get_queryset(self):
        return Student.objects.all()

class StudentDetailUpdate(UpdateView):
    model = Student
    form_class = StudentAdmissionForm
    template_name = 'student_update.html'
    success_url = '/studentlist/'

    def get_context_data(self, *args, **kwargs):
        context = super(StudentDetailUpdate, self).get_context_data(*args, **kwargs)
        return context

    # def get_queryset(self):
    #     return Student.objects.filter(owner=self.request.user) #.filter(category__iexact='I')




