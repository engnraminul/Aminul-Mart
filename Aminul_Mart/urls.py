from django.contrib import admin
from django.urls import path, include

#show media files
from django.conf import settings
from django.contrib. staticfiles.urls import static, staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('Login.urls')),
    path('',include('Shop.urls')),

]

urlpatterns +=staticfiles_urlpatterns()
urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)