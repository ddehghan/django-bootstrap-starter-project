from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'myproject.views.home', name='home'),
                       url(r'', include('social_auth.urls')),
                       (r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),

                       url(r'^$', 'website.views.home', name='home'),
                       url(r'^index$', 'website.views.index', name='index'),
                       url(r'^private$', 'website.views.private', name='private'),

                       url("^mission", TemplateView.as_view(template_name='mission.html'), name="mission"),
                       url("^programs", TemplateView.as_view(template_name='programs.html'), name="programs"),
                       url("^drawings", TemplateView.as_view(template_name='drawings.html'), name="drawings"),

                       # Admin site
                       # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
                       url(r'^admin/', include(admin.site.urls)),
)
