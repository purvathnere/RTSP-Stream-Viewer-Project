from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

from streamer.views import (
    StreamSessionViewSet,
    stream_view,        # updated stream view jo template render karega
    home,
    start_stream,
)

router = DefaultRouter()
router.register(r'streams', StreamSessionViewSet)  # ModelViewSet routes

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/', include(router.urls)),  # DRF ViewSet API
    path('api/streams/start/', start_stream, name='start_stream'),  # API to start streaming

    path('', home, name='home'),  # simple home page

    # Stream player page jo stream_id lega aur template ko render karega
    path('streams/<str:stream_id>/', stream_view, name='stream_view'),
]

# Static/media files serve karna (e.g., .m3u8 files)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
