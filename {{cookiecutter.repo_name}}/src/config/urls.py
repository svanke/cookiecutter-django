from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from .views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
    path('', index, name='index'),
]

if settings.DEBUG:
    # import debug_toolbar

    urlpatterns += [
                       # re_path(r'__debug__/', include(debug_toolbar.urls))
                   ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
