from django.contrib import admin
from django.urls import path, include
import igv
import landing
import landing.urls
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(landing.urls)),
    #path('igv/', include(igv.urls)),
]+ static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])



