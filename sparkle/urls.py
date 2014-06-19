from django.conf.urls import patterns, url

urlpatterns = patterns(
    'sparkle.views',
    url(r'^(?P<application_slug>[\w-]+)/appcast.xml$', 'appcast',
        name='sparkle_application_appcast'),
)
