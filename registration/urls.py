from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from registration import views
from registration.views import *
from registration.models import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='register/register.html')),
    url(r'^user/$', UserRegistrationView.as_view(), name='register_user'),
    url(r'^user/success/$',TemplateView.as_view(template_name='register/user/success.html'),name='user_registration_success'),
    url(r'^portal/student/$',TemplateView.as_view(template_name='register/manage_students.html'),name="manage_students"),
    url(r'^portal/staff/$',TemplateView.as_view(template_name='register/manage_staff.html'),name="manage_staff"),
    url(r'^preferences', TemplateView.as_view(template_name='preferences.html'),name="preferences"),
    url(r'^sign-in', TemplateView.as_view(template_name='sign-in.html'),name="sign-in"),
    url(r'^index', TemplateView.as_view(template_name='index.html'),name="index"),
    url(r'^student/$', StudentRegistrationView.as_view(), name='register_student'),
    url(r'^cirstaff/success/', TemplateView.as_view(template_name='register/cirstaff/success.html'), name='success'),
    url(r'^bulk/$', StudentBulkUploadView.as_view(), name='register_student_bulk'),
    url(r'^bulk/handle/$', views.handle_student_upload, name='upload_students'),
    url(r'^list/$', StudentListView.as_view(), name='list'),
    url(r'^profile/edit/(?P<aums_id>[\w|\W]+)/$', StudentListUpdateView.as_view(), name='student_profile_update'),
    url(r'^students/filter/$', TemplateView.as_view(template_name='register/cirstaff/filter_external.html'),name="filter_external"),
    url(r'^students/filter/external/$', StudentFilterExternalView.as_view(),name="filter_external_list"),
    url(r'^student/tests/technical/$', StudentTechnicalTestEntryView.as_view(), name='technical_test'),
    url(r'^gallery/$', GalleryListView.as_view(), name='gallery'),
    url(r'^sapimg/$', SapimgListView.as_view(), name='sapimg'),
    url(r'^dailyrituals/$', DailyritualsListView.as_view(), name='dailyrituals'),
    url(r'^offerings/$', OfferingsListView.as_view(), name='offerings'),
    url(r'^poojadetails/$', PoojadetailsListView.as_view(), name='poojadetails'),
    url(r'^contactus/$', ContactusListView.as_view(), name='contactus'),
    url(r'^orgin/$', OrginListView.as_view(), name='orgin'),
    url(r'^upadevas/$', UpadevasListView.as_view(), name='upadevas'),
    url(r'^organisationalsetup/$', OrganisationalsetupListView.as_view(), name='organisationalsetup'),
    url(r'^activities/$', ActivitiesListView.as_view(), name='activities'),
    url(r'^festivals/$', FestivalsListView.as_view(), name='festivals'),
    url(r'^facilities/$', FacilitiesListView.as_view(), name='facilities'),
    url(r'^officebearers/$', OfficebearersListView.as_view(), name='officebearers'),
    url(r'^vazhipad_booking/$', Vazhipad_bookingListView.as_view(), name='vazhipad_booking'),
    url(r'^prathishtta_krishna/$', Prathishtta_krishnaListView.as_view(), name='prathishtta_krishna'),
    url(r'^prathishtta_ganapathi/$', Prathishtta_ganapathiListView.as_view(), name='prathishtta_ganapathi'),
    url(r'^prathishtta_devi/$', Prathishtta_deviListView.as_view(), name='prathishtta_devi'),
    url(r'^prathishtta_nagar/$', Prathishtta_nagarListView.as_view(), name='prathishtta_nagar'),
]