from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.decorators import authentication_classes, permission_classes # type: ignore
from rest_framework.permissions import IsAuthenticated  # type: ignore
from rest_framework.authentication import TokenAuthentication, SessionAuthentication # type: ignore
from django.shortcuts import get_object_or_404 # type: ignore
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class AutorViewSet(viewsets.ModelViewSet):

    @api_view(['POST'])
    def login(request):
        user = get_object_or_404(Usuario, username=request.data['username'])
        if not user.check_password(request.data['password']):
            return Response({'message': 'Not Found!'}, status=status.HTTP_400_BAD_REQUEST)
        
        token, created = Token.objects.get_or_create(user=user)
        serializer = UsuarioSerializer(instance=user)
        return Response({'token': token.key, 'user':serializer.data})

    @api_view(['POST'])
    def signup(request):
        serializer = UsuarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = Usuario.objects.get(username=request.data['username'])
            user.set_password(request.data['password'])
            user.save()
            token = Token.objects.create(user=user)
            return Response({'token': token.key, 'user':serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @api_view(['GET'])
    @authentication_classes([TokenAuthentication, SessionAuthentication])
    @permission_classes([IsAuthenticated])
    
    def test_token(request):
        return Response("passou para {}".format(request.user.email))

class LivroViewSet(viewsets.ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer

class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer

class EmprestimoViewSet(viewsets.ModelViewSet):
    queryset = Emprestimo.objects.all()
    serializer_class = EmprestimoSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer