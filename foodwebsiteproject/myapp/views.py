from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Product, Features, Categories, Bannerdesc, Userregistration, Blog, Addreview, CartItem, Cart


# Create your views here.
def home(request):
    pr = Product.objects.all()
    fr = Features.objects.all()
    cr = Categories.objects.all()
    ds = Bannerdesc.objects.all()
    usr = Userregistration.objects.all()
    bl = Blog.objects.all()
    try:
        txt = request.GET.get("text")
        print(txt)
        sf = Addreview(ureview=txt)
        sf.save()

    except Exception as e:
        print(e)

    data = {'pr': pr, 'fr': fr, 'cr': cr, 'ds': ds, 'user': usr, 'bl': bl}

    return render(request, "index.html", data)


def add_to_cart(request, product_id):
    product = Product.objects.get(pk=product_id)

    # Get or create a cart associated with the user's session
    cart_id = request.session.get('cart_id')
    if not cart_id:
        cart = Cart.objects.create()
        request.session['cart_id'] = cart.id
    else:
        cart = Cart.objects.get(pk=cart_id)

    # Add the product to the cart
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    cart_item.quantity += 1
    cart_item.save()

    return redirect('view_cart')  # Redirect to your product list view


def view_cart(request):
    cart_id = request.session.get('cart_id')
    if not cart_id:
        return HttpResponse("Your cart is empty.")

    cart = Cart.objects.get(pk=cart_id)
    cart_items = CartItem.objects.filter(cart=cart)
    return render(request, 'view_cart.html', {'cart_items': cart_items, 'cart': cart})


def remove_from_cart(request, cart_item_id):
    cart_item = CartItem.objects.get(pk=cart_item_id)
    cart_item.delete()
    return redirect('view_cart')


def checkout(request):
    cart_id = request.session.get('cart_id')
    if not cart_id:
        return redirect('view_cart')

    cart = Cart.objects.get(pk=cart_id)
    total_cost = cart.total_cost

    if request.method == 'POST':
        # Simulate order completion (clear cart, mark items as purchased, etc.)
        cart.cartitem_set.all().delete()
        request.session['cart_id'] = None  # Clear cart from session
        return render(request, 'checkout_complete.html', {'total_cost': total_cost})

    return render(request, 'checkout.html', {'cart': cart, 'total_cost': total_cost})


def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})
