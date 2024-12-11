from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

from GameMax.shop.views import CartView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('GameMax.home.urls')),
    path('accounts/', include('GameMax.app_users.urls')),
    path('shop/', include('GameMax.shop.urls')),
    path('wishlist/', include('GameMax.wishlist.urls')),
    path('orders/', include('GameMax.orders.urls')),
    path('reviews/', include('GameMax.reviews.urls')),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('api/cart/', CartView.as_view(), name='cart'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
