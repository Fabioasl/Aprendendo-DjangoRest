from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from backend import views

router = DefaultRouter()
router.register(r'usuario', views.UsuarioViewSet)
router.register(r'autor', views.AutorViewSet)
router.register(r'livro', views.LivroViewSet)
router.register(r'Emprestimo', views.EmprestimoViewSet)
router.register(r'Reserva', views.ReservaViewSet)
router.register(r'Categoria', views.CategoriaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]