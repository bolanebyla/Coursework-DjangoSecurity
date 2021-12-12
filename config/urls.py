from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('attacks_demonstration/', include('attacks_demonstration.urls'))
]
