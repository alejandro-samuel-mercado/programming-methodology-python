from django.shortcuts import render
from .models import Producto
from django.core.paginator import Paginator


def home(request):
    productos = Producto.objects.all()
    return render(request, "core/base.html", {'productos': productos})


def lista_productos(request):
    productos = Producto.objects.all()
    num_slides = range(3)  # Generar 3 diapositivas
    paginator = Paginator(productos, 28)  # Muestra 28 productos por página

# Obteniene el número de página de la solicitud
    page_number = request.GET.get('page')

    # Obtiene los productos para esa página
    page_obj = paginator.get_page(page_number)

    context = {
        'productos': productos,
        'num_slides': num_slides,
        'page_obj': page_obj
    }
    return render(request, 'core/lista_productos.html', context)
