from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Produto

def index(request):
    return render(request, 'stock/index.html')

@login_required
def produtos_view(request):
    produtos_list = Produto.objects.all()
    context = {'produtos_list': produtos_list}
    return render(request, 'stock/produtos.html', context)
   
@login_required
def teste(request):
    return render(request, 'stock/teste.html')