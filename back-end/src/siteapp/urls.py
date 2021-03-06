from __future__ import absolute_import, print_function, unicode_literals

from cms.sitemaps import CMSSitemap
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.static import serve
from inex_page_home import views

admin.autodiscover()

urlpatterns = [
    url(r'^sitemap\.xml$', sitemap,
        {'sitemaps': {'cmspages': CMSSitemap}}),
]

urlpatterns += (
    url(r'^admin/', admin.site.urls), 
    url(r'^', include('cms.urls')),
    url(r'^api/search/all', views.search)
)

urlpatterns += (
    url(r'^solutions/', include('solutions.urls')),
    url(r'^products/', include('product.urls')),
    url(r'^offer/', include('offer.urls')),
    url(r'^contact/', include('contact.urls')),
    url(r'^search/', include('search.urls')),
    url(r'^about/', include('about.urls')),
)
      
if settings.DEBUG:
    urlpatterns = [
        url(r'^media/(?P<path>.*)$', serve,
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        ] + staticfiles_urlpatterns() + urlpatterns