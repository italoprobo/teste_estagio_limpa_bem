from django.shortcuts import get_object_or_404, redirect, render
from .models import Cliente, Servico, Funcionario, Atendimento
from django import forms
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

def home(request):
    return render(request, 'main/home.html', {})

def listar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'main/listar_clientes.html', {'clientes': clientes})

def listar_servicos(request):
    servicos = Servico.objects.all()
    return render(request, 'main/listar_servicos.html', {'servicos': servicos})

def listar_funcionarios(request):
    funcionarios = Funcionario.objects.all()
    return render(request, 'main/listar_funcionarios.html', {'funcionarios': funcionarios})

def listar_atendimentos(request):
    atendimentos = Atendimento.objects.all()
    return render(request, 'main/listar_atendimentos.html', {'atendimentos': atendimentos})

class NovoClienteForm(forms.ModelForm):
    class Meta:    
        model = Cliente
        fields = '__all__'

class NovoServicoForm(forms.ModelForm):
    class Meta:    
        model = Servico
        fields = '__all__'

class NovoFuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = '__all__'

class NovoAtendimentoForm(forms.ModelForm):
    class Meta:
        model = Atendimento
        fields = ['servico', 'atendente', 'helper', 'valor', 'desconto', 'forma_pagamento', 'data_cadastro', 'data_execucao', 'situacao', 'cliente']
        widgets = {
            'data_cadastro': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'data_execucao': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
    servico = forms.ModelChoiceField(queryset=Servico.objects.all(), empty_label=None)
    atendente = forms.ModelChoiceField(queryset=Funcionario.objects.filter(tipo='atendente'))
    helper = forms.ModelChoiceField(queryset=Funcionario.objects.filter(tipo='helper'))
    cliente = forms.ModelChoiceField(queryset=Cliente.objects.all())
    
    def save(self, commit=True):
        atendimento = super(NovoAtendimentoForm, self).save(commit=False)
        if commit:
            atendimento.save()
        return atendimento

def adicionar_clientes(request):
    if request.method == 'POST':
        form = NovoClienteForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            telefone = form.cleaned_data['telefone']
            endereco = form.cleaned_data['endereco']
            cliente = Cliente(nome=nome, telefone=telefone, endereco=endereco)
            cliente.save()
            return redirect('listar_clientes')
    else:
        form = NovoClienteForm()
    return render(request, 'main/adicionar_clientes.html', {'form': form})

def adicionar_servicos(request):
    if request.method == 'POST':
        form = NovoServicoForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            valor = form.cleaned_data['valor']
            servico = Servico(nome=nome, valor=valor)
            servico.save()
            return redirect('listar_servicos')
    else:
        form = NovoServicoForm()
    return render(request, 'main/adicionar_servicos.html', {'form': form})

def adicionar_funcionarios(request):
    if request.method == 'POST':
        form = NovoFuncionarioForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            tipo = form.cleaned_data['tipo']
            funcionario = Funcionario(nome=nome, tipo=tipo)
            funcionario.save()
            return redirect('listar_funcionarios')
    else:
        form = NovoFuncionarioForm()
    return render(request, 'main/adicionar_funcionarios.html', {'form': form})

def editar_funcionario(request, pk):
    funcionario = get_object_or_404(Funcionario, pk=pk)

    if request.method == 'POST':
        form = NovoFuncionarioForm(request.POST, instance=funcionario)
        if form.is_valid():
            form.save()
            return redirect('listar_funcionarios')
    else:
        form = NovoFuncionarioForm(instance=funcionario)

    context = {
        'form': form,
    }
    return render(request, 'main/editar_funcionario.html', context)

def editar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)

    if request.method == 'POST':
        form = NovoClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('listar_clientes')
    else:
        form = NovoClienteForm(instance=cliente)

    context = {
        'form': form,
    }
    return render(request, 'main/editar_cliente.html', context)

def editar_servico(request, pk):
    servico = get_object_or_404(Servico, pk=pk)

    if request.method == 'POST':
        form = NovoServicoForm(request.POST, instance=servico)
        if form.is_valid():
            form.save()
            return redirect('listar_servicos')
    else:
        form = NovoServicoForm(instance=servico)

    context = {
        'form': form,
    }
    return render(request, 'main/editar_servico.html', context)

def editar_atendimento(request, pk):
    atendimento = get_object_or_404(Atendimento, pk=pk)

    if request.method == 'POST':
        form = NovoAtendimentoForm(request.POST, instance=atendimento)
        if form.is_valid():
            form.save()
            return redirect('listar_atendimentos')
    else:
        form = NovoAtendimentoForm(instance=atendimento)

    context = {
        'form': form,
    }
    return render(request, 'main/editar_atendimento.html', context)

def certeza_excluir_atendimento(request, atendimento_id):
    atendimento = Atendimento.objects.get(id=atendimento_id)
    return render(request, 'excluir_atendimento.html', {'atendimento': atendimento})

def excluir_atendimento(request, atendimento_id):
    atendimento = Atendimento.objects.get(id=atendimento_id)
    atendimento.delete()
    return redirect('listar_atendimentos')

def adicionar_atendimentos(request):
    if request.method == 'POST':
        form = NovoAtendimentoForm(request.POST)
        if form.is_valid():
            atendimento = form.save(commit=False)
            atendimento.save()
            return redirect('listar_atendimentos')
    else:
        form = NovoAtendimentoForm()
    servicos = Servico.objects.all()
    atendentes = Funcionario.objects.filter(tipo='atendente')
    helpers = Funcionario.objects.filter(tipo='helper')
    clientes = Cliente.objects.all()
    context = {
        'form': form,
        'servicos': servicos,
        'atendentes': atendentes,
        'helpers': helpers,
        'clientes': clientes
    }
    return render(request, 'main/adicionar_atendimentos.html', context)