from django.urls import path, include
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from project import settings

urlpatterns = [
    path('', include('img_uploader.urls')),
]

if settings.DEBUG and settings.DEBUG_TOOLS:
    import debug_toolbar

    urlpatterns = [path('__debug__/', include(debug_toolbar.urls))] + urlpatterns

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
