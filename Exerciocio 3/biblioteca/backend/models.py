from django.db import models

class Livro(models.Model):
    titulo = models.CharField(max_length=100) 
    autor = models.CharField(max_length=100)
    dt_publicacao = models.DateField(auto_now_add=True)
    genero = models.CharField(max_length=100)

    def __str__(self):
        return self.titulo
    class Meta:
        verbose_name_plural = "Livros"
    
class Autor(models.Model):
    nome = models.CharField(max_length=100)
    dt_nascimento = models.DateField(auto_now_add=True)
    nacionalidade = models.CharField(max_length=100)
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name_plural = "Autores"
        
class Multa(models.Model):
    valor = models.FloatField(default=0.0)
    dt_pagamento = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"R${self.valor:.2f}"
    class Meta:
        verbose_name_plural = "Multas"

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    dt_registro = models.DateField(auto_now_add=True)
    multas = models.ManyToManyField(Multa) # Um usuário pode ter muitas multas
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name_plural = "Usuarios"

class Emprestimo(models.Model):
    livro = models.ForeignKey(Livro,on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)
    dt_emprestimo = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.dt_emprestimo
    class Meta:
        verbose_name_plural = "Emprestimos"

class Reserva(models.Model):
    livro = models.ForeignKey(Livro,on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)
    dt_reserva = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.dt_reserva
    class Meta:
        verbose_name_plural = "Reservas"


class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
    class Meta:
        verbose_name_plural = "Categorias"

class Editora(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)


    def __str__(self):
        return self.nome
    class Meta:
        verbose_name_plural = "Editoras"








