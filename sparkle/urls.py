from django.conf.urls import patterns, url
from .views import appcast

urlpatterns = patterns(
    '',
    url(r'^(?P<slug>[\w-]+)/appcast.xml$', appcast,
        name='sparkle_application_appcast'),
)
