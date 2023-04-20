from django.urls import path, include

urlpatterns = [
    path('integracoes/', include('core.integracoes.urls'))
]
