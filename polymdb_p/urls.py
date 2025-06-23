
from django.contrib import admin
from django.urls import path, include 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('polymes/', include('polymes.urls')),
    #path('', include('polymdb_p.urls')),
]
