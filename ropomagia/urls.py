from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('scryfall/', include('scryfall.urls')),
    path('admin/', admin.site.urls),
]
