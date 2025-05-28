from rest_framework import serializers
from .models import *

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        models = Reserva
        fields = '__all__'

class EmprestimoSerializer(serializers.ModelSerializer):
    class Meta:
        models = Emprestimo
        fields = '__all__'

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        models = Categoria
        fields = '__all__'

class LivroSerializer(serializers.ModelSerializer):
    class Meta:
        models = Livro
        fields = '__all__'