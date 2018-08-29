"""easy_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView

from apps.utils import errors
from .settings import local, base
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Shop API')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^chaining/', include('smart_selects.urls')),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^fcm/', include('apps.fcm.urls')),
    # api
    url(r'^api/', include('apps.api.urls', namespace='api')),
    # apps
    url(r'^app/', include('apps.app.urls', namespace='app')),

    url(r'^$', schema_view),
    url(r'^client/', TemplateView.as_view(template_name='index.html'))

] + static(base.MEDIA_URL, document_root=base.MEDIA_ROOT)

if local.DEBUG:
    import debug_toolbar

    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]

handler400 = errors.error400
handler403 = errors.error403
handler404 = errors.error404
handler500 = errors.error500
