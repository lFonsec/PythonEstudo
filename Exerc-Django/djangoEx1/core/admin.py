from django.contrib import admin

from .models import Produtos, Cliente


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque')


class ClenteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'email')


admin.site.register(Produtos, ProdutoAdmin)
admin.site.register(Cliente, ClenteAdmin)
