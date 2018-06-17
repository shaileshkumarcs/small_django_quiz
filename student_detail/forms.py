from django import forms

from .models import Student

class StudentAdmissionForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'first_name',
            'last_name',
            'std_class',
            'roll_number',
            'email_id',
            'address',

        ]

    def __init__(self, user=None, *args, **kwargs):
        #print(user)
        super(StudentAdmissionForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].queryset = Student.objects.filter(owner=user)  # .exclude(item__isnull=False)