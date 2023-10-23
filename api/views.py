from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import api_view

from .serializer import *
from .models import *

from rest_framework.response import Response
from rest_framework import status

# Create your views here.
from rest_framework.authtoken.models import Token


class PersonaViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer


class TipoDocumentoViewSet(viewsets.ModelViewSet):
    queryset = TipoDocumento.objects.all()
    serializer_class = TipoDocumentoSerializer


class RolViewSet(viewsets.ModelViewSet):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer


class PrivilegiosViewSet(viewsets.ModelViewSet):
    queryset = Privilegios.objects.all()
    serializer_class = PrivilegiosSerializer


class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer


class RolPrivilegioViewSet(viewsets.ModelViewSet):
    queryset = RolPrivilegios.objects.all()
    serializer_class = RolPrivilegioSerializer


@api_view(['POST'])
def signup(request):
    serializer = UsuarioSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user = Usuario.objects.get(username=request.data['username'])
        user = Usuario.objects.get(password=request.data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return Response({'token': token.key, 'user': serializer.data})
    return Response(serializer.errors, status=status.HTTP_200_OK)


@api_view(['POST'])
def login(request):
    user = get_object_or_404(Usuario, username=request.data['username'])
    if not user.check_password(request.data['password']):
        return Response("missing user", status=status.HTTP_404_NOT_FOUND)
    token, created = Token.objects.get_or_create(user=user)
    serializer = UsuarioSerializer(user)
    return Response({'token': token.key, 'user': serializer.data})
