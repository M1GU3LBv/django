from django.urls import path, include, re_path
from rest_framework import routers
from api import views

routers = routers.DefaultRouter()
routers.register(r'persona', views.PersonaViewSet)
routers.register(r'Rol', views.RolViewSet)
routers.register(r'TipoDocumento', views.TipoDocumentoViewSet)
routers.register(r'Reserva', views.ReservaViewSet)
routers.register(r'Privilegios', views.PrivilegiosViewSet)
routers.register(r'RolPrivilegios', views.RolPrivilegioViewSet)

urlpatterns = [
    path('', include(routers.urls)),
    path(r'signup', views.signup),
    path(r'login', views.login)

]

