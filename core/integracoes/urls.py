from django.urls import path, include

urlpatterns = [
    path('github/', include('core.integracoes.github.urls'))
]