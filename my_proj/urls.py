from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns

from django.conf import settings    # for serving uploaded files
from django.conf.urls.static import static  # for serving uploaded files

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^i18n/', include('django.conf.urls.i18n')),
]

urlpatterns += i18n_patterns(
    url(r'^accounts/', include('my_auth.urls')),
    url('^accounts/', include('django.contrib.auth.urls')),
    url(r'^', include('portfolio.urls')),
)

urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
