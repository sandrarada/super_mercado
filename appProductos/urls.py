from django.urls import path
from . import views
urlpatterns = [
    path('categorias/', views.verCategorias, name='categorias'),
    path('productos/<str:idCategoria>', views.verProductosCategoria, name='productos'),
    path('producto/<str:idProd>', views.verProducto, name='un_producto'),
]