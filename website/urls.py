from django.urls import path
from .views import(
    home,
    contato,
    planos,
    servicos,
    sobre
)

urlpatterns = [
    path('', home, name='home'),
    path('contato/', contato, name='contato'),
    path('planos/', planos, name='planos'),
    path('servicos/', servicos, name='servicos'),
    path('sobre/', sobre, name='sobre'),
]
