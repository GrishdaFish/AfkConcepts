from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.conf import settings

urlpatterns = [
    # Examples:
    # url(r'^$', 'afkconcepts.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('home.urls', namespace='home', app_name='home')),
    url(r'^home/', include('home.urls', namespace='home', app_name='home')), #verbose, or redundant?
]
if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'media/(?P<path>.*)',

        'serve',
        {'document_root': settings.MEDIA_ROOT}),

    )
