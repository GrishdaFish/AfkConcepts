from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.conf import settings
import views
from django.conf.urls.static import static
urlpatterns = [
    # Examples:
    # url(r'^$', 'afkconcepts.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('home.urls', namespace='home', app_name='home')),#www.afkovertime.com will point nto afkovertime.com/home/
    url(r'^home/', include('home.urls', namespace='home', app_name='home')), #verbose, or redundant? #somewhat both. this is incase of afkovertime.com/home/ will point to this
    url(r'^portfolio/', views.portfolio, name='portfolio'),#should put these in home urls
    url(r'^services/', views.services, name='services'),#<-
    url(r'^contact/', views.contact, name='contact'),#<-
]
if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'media/(?P<path>.*)',

        'serve',
        {'document_root': settings.MEDIA_ROOT}),

    )