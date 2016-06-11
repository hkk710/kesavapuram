from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from registration import urls as reg_urls
from registration import views
from cirplacements.views import anonymous_required
from registration.views import *
from registration.models import *
from django.contrib.auth.decorators import login_required
import registration.views as views
from django.contrib.auth import views as auth_views

urlpatterns= (
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
    url(r'^register/', include(reg_urls), name='register'),
    # url(r'^$', 'cirplacements.views.home', ),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^user/login/$',
        anonymous_required(auth_views.login),
        {'template_name': 'register/login.html'},
        name='login'),
    url(r'^password/reset/$',
        anonymous_required(auth_views.password_reset),
        {'template_name': 'register/passwd_reset.html',
        'email_template_name':'register/passwd_reset_email.html'},
        name='password_reset'),
    url(r'^password/reset/done/$',
        anonymous_required(auth_views.password_reset_done),
        {'template_name': 'register/passwd_reset_done.html'},
        name='password_reset_done'),
    url(r'^password/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        anonymous_required(auth_views.password_reset_confirm),
        {'template_name': 'register/passwd_reset_confirm.html'},
        name='password_reset_confirm'),
    url(r'^password/reset/complete/$', anonymous_required(auth_views.password_reset_complete),
        {'template_name': 'register/passwd_reset_complete.html'},
        name='password_reset_complete'),
    url(r'^password/reset/done/$',
        anonymous_required(auth_views.password_reset_done),
        {'template_name': 'register/passwd_reset_done.html'},
        name='password_reset_done'),
    url(r'^password/change/$',
        auth_views.password_change,
        {'template_name': 'register/passwd_change.html'},
        name='password_change'),
    url(r'^user/logout/$',
        auth_views.logout,
        {'template_name': 'register/logout.html'},
        name='logout'),
    url(r'^about/$', TemplateView.as_view(template_name='register/about.html'), name='about')
)
