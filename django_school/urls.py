
from django.urls import include, path
from classroom.views import classroom, students, teachers, stdetails


urlpatterns = [
    path('', include('classroom.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('studentlist/', include('student_detail.urls')),
    path('accounts/signup/', classroom.SignUpView.as_view(), name='signup'),
    path('accounts/signup/student/', students.StudentSignUpView.as_view(), name='student_signup'),
    path('accounts/signup/teacher/', teachers.TeacherSignUpView.as_view(), name='teacher_signup'),
    path('accounts/signup/stdetails/', stdetails.StdetailSignUpView.as_view(), name='stdetails_signup'),
]
