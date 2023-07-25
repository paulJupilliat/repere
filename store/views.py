from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from store.models import Cart, Products, Order, Commande


# Create your views here.
def index(request):
    products = Products.objects.all()
    return render(request, 'store/index.html', context={'products': products})


def product_detail(request, slug):
    product = get_object_or_404(Products, slug=slug)
    return render(request, 'store/detail.html', context={'product': product})

def add_to_cart(request, slug):
    #les différents cas de figure : deja un panier, pas de panier, particle existe deja dans son panier
    user = request.user
    product = get_object_or_404(Products, slug=slug)
    #methode permettant de recuperer si existe, sinon créer
    cart, _ = Cart.objects.get_or_create(user=user)
    order, created = Order.objects.get_or_create(user=user, product=product)
    if created : 
        cart.orders.add(order)
        cart.save()
    else:
        order.quantity += 1
        order.save()
    return redirect(reverse("product", kwargs={'slug': slug}))

def cart(request):
    cart = get_object_or_404(Cart, user=request.user)
    return render(request, 'store/cart.html', context={'orders': cart.orders.all()})

def delete_cart(request):
    cart = request.user.cart
    if cart :
        cart.orders.all().delete()
        cart.delete()
    return redirect('index')


def commande(request):
    commande = get_object_or_404(Commande, user=request.user)
    for article in commande :
        prix += article.price * article.quantity
    return render(request, 'store/commande.html', context={'commande': commande, 'prix': prix})
