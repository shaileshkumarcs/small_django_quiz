from django.conf.urls import url

from .views import (
        StudentCreateView,
        StudentDetailsView,
        StudentListView,
        StudentDetailUpdate,
    )

urlpatterns = [
    url(r'^$', StudentListView.as_view(), name="listview"),
    url(r'^createview$', StudentCreateView.as_view(), name="createstudent"),
    url(r'^profile/(?P<pk>\d+)/$', StudentDetailsView.as_view(), name="detail"),
    url(r'^profile-update/(?P<pk>\d+)/$', StudentDetailUpdate.as_view(), name="update"),
]