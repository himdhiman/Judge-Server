from django.urls import path
from problem import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.upload_tc, name = "index"),
    path('get/', views.getData),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

