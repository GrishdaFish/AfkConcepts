from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.conf import settings
import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'afkconcepts.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('home.urls', namespace='home', app_name='home')),
    url(r'^home/', include('home.urls', namespace='home', app_name='home')), #verbose, or redundant?
    url(r'^portfolio/', views.portfolio, name='portfolio'),
    url(r'^services/', views.services, name='services'),
    url(r'^contact/', views.contact, name='contact'),
]
if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'media/(?P<path>.*)',

        'serve',
        {'document_root': settings.MEDIA_ROOT}),

    )
