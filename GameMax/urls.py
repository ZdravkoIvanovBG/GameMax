from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('GameMax.home.urls')),
    path('accounts/', include('GameMax.app_users.urls'))
]
