from django.urls import path, include

urlpatterns = [
    path('integracoes/', include('core.integracoes.urls')),
    path('admin/', include('core.admin.urls'))
]
