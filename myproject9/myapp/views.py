from django.shortcuts import render, redirect

# Fake users for login (you can add more here)
USERS = {
    'admin': 'admin123',
    'sharmi': 'sharmi123',
    'menaka': 'menaka123'
}

AVAILABLE_ITEMS = ['T-Shirt', 'Shoes', 'Sunglasses', 'Hat', 'Backpack']

def login_view(request):
    error = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username in USERS and USERS[username] == password:
            request.session['logged_in'] = True
            response = redirect('items')
            response.set_cookie('username', username)
            return response
        else:
            error = 'Invalid username or password.'
    
    return render(request, 'login.html', {'error': error})


def items_view(request):
    if not request.session.get('logged_in'):
        return redirect('login')
    
    username = request.COOKIES.get('username')
    return render(request, 'items.html', {'username': username, 'items': AVAILABLE_ITEMS})


def cart_view(request):
    if not request.session.get('logged_in'):
        return redirect('login')

    username = request.COOKIES.get('username')
    cart = request.session.get('cart', [])
    return render(request, 'cart.html', {'username': username, 'cart': cart})


def add_to_cart(request, item):
    if not request.session.get('logged_in'):
        return redirect('login')

    cart = request.session.get('cart', [])
    if item not in cart:
        cart.append(item)
    request.session['cart'] = cart
    return redirect('cart')


def remove_from_cart(request, item):
    if not request.session.get('logged_in'):
        return redirect('login')

    cart = request.session.get('cart', [])
    if item in cart:
        cart.remove(item)
    request.session['cart'] = cart
    return redirect('cart')
