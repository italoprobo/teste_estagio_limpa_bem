from django.contrib import admin
from .models import Cliente, Funcionario, Atendimento, Servico
# Register your models here.
admin.site.register(Cliente)
admin.site.register(Funcionario)
admin.site.register(Atendimento)
admin.site.register(Servico)