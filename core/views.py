from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import (
    Pessoa,
    Marca,
    Veiculo,
    MovRotativo,
    Mensalista,
    MovMensalista,
)
from .form import (
    PessoaForm,
    MarcaForm,
    VeiculoForm,
    MovRotativoForm,
    MensalistaForm,
    MovMensalistaForm,
)


def home(request):
    return render(request, 'core/index.html')


@login_required
def lista_pessoa(request):
    data = {}
    form = PessoaForm()
    data['pessoa'] = Pessoa.objects.all()
    data['form'] = form
    return render(request, 'core/lista_pessoa.html', data)


@login_required
def pessoa_novo(request):
    form = PessoaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('lista_pessoa')


@login_required
def update_pessoa(request, pk):
    data = {}
    pessoa = Pessoa.objects.get(pk=pk)
    form = PessoaForm(request.POST or None, instance=pessoa)
    data['pessoa'] = pessoa
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('lista_pessoa')
    else:
        return render(request, 'core/update_pessoa.html', data)


@login_required
def del_pessoa(request, pk):
    data = {}
    obj = Pessoa.objects.get(pk=pk)
    data['obj'] = obj

    if request.method == 'POST':
        obj.delete()
        return redirect('lista_pessoa')
    else:
        return render(request, 'core/del_confirmacao.html', data)


@login_required
def lista_marca(request):
    data = {}
    form = MarcaForm()
    data['marca'] = Marca.objects.all()
    data['form'] = form
    return render(request, 'core/lista_marca.html', data)


@login_required
def marca_novo(request):
    form = MarcaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('lista_marca')


@login_required
def update_marca(request, pk):
    data = {}
    marca = Marca.objects.get(pk=pk)
    form = MarcaForm(request.POST or None, instance=marca)
    data['marca'] = marca
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('lista_marca')
    else:
        return render(request, 'core/update_marca.html', data)


@login_required
def del_marca(request, pk):
    data = {}
    obj = Marca.objects.get(pk=pk)
    data['obj'] = obj

    if request.method == 'POST':
        obj.delete()
        return redirect('lista_marca')
    else:
        return render(request, 'core/del_confirmacao.html', data)


@login_required
def lista_veiculo(request):
    data = {}
    form = VeiculoForm()
    data['veiculo'] = Veiculo.objects.all()
    data['form'] = form
    return render(request, 'core/lista_veiculo.html', data)


@login_required
def veiculo_novo(request):
    form = VeiculoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('lista_veiculo')


@login_required
def update_veiculo(request, pk):
    data = {}
    veiculo = Veiculo.objects.get(pk=pk)
    form = VeiculoForm(request.POST or None, instance=veiculo)
    data['veiculo'] = veiculo
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('lista_veiculo')
    else:
        return render(request, 'core/update_veiculo.html', data)


@login_required
def del_veiculo(request, pk):
    data = {}
    obj = Veiculo.objects.get(pk=pk)
    data['obj'] = obj

    if request.method == 'POST':
        obj.delete()
        return redirect('lista_veiculo')
    else:
        return render(request, 'core/del_confirmacao.html', data)


@login_required
def lista_movrotativo(request):
    data = {}
    form = MovRotativoForm()
    data['movrotativo'] = MovRotativo.objects.all()
    data['form'] = form
    return render(request, 'core/lista_movrotativo.html', data)


@login_required
def movrotativo_novo(request):
    form = MovRotativoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('lista_movrotativo')


@login_required
def update_movrotativo(request, pk):
    data = {}
    movrotativo = MovRotativo.objects.get(pk=pk)
    form = MovRotativoForm(request.POST or None, instance=movrotativo)
    data['movrotativo'] = movrotativo
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('lista_movrotativo')
    else:
        return render(request, 'core/update_movrotativo.html', data)


@login_required
def del_movrotativo(request, pk):
    data = {}
    obj = MovRotativo.objects.get(pk=pk)
    data['obj'] = obj

    if request.method == 'POST':
        obj.delete()
        return redirect('lista_movrotativo')
    else:
        return render(request, 'core/del_confirmacao.html', data)


@login_required
def lista_mensalista(request):
    data = {}
    form = MensalistaForm()
    data['mensalista'] = Mensalista.objects.all()
    data['form'] = form
    return render(request, 'core/lista_mensalista.html', data)


@login_required
def mensalista_novo(request):
    form = MensalistaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('lista_mensalista')


@login_required
def update_mensalista(request, pk):
    data = {}
    mensalista = Mensalista.objects.get(pk=pk)
    form = MensalistaForm(request.POST or None, instance=mensalista)
    data['mensalista'] = mensalista
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('lista_mensalista')
    else:
        return render(request, 'core/update_mensalista.html', data)


@login_required
def del_mensalista(request, pk):
    data = {}
    obj = Mensalista.objects.get(pk=pk)
    data['obj'] = obj

    if request.method == 'POST':
        obj.delete()
        return redirect('lista_mensalista')
    else:
        return render(request, 'core/del_confirmacao.html', data)


@login_required
def lista_movmensalista(request):
    data = {}
    form = MovMensalistaForm()
    data['movmensalista'] = MovMensalista.objects.all()
    data['form'] = form
    return render(request, 'core/lista_movmensalista.html', data)


@login_required
def movmensalista_novo(request):
    form = MovMensalistaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('lista_movmensalista')


@login_required
def update_movmensalista(request, pk):
    data = {}
    movmensalista = MovMensalista.objects.get(pk=pk)
    form = MovMensalistaForm(request.POST or None, instance=movmensalista)
    data['movmensalista'] = movmensalista
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('lista_movmensalista')
    else:
        return render(request, 'core/update_movmensalista.html', data)


@login_required
def del_movmensalista(request, pk):
    data = {}
    obj = MovMensalista.objects.get(pk=pk)
    data['obj'] = obj

    if request.method == 'POST':
        obj.delete()
        return redirect('lista_movmensalista')
    else:
        return render(request, 'core/del_confirmacao.html', data)
