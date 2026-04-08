from django.shortcuts import render, redirect

# Mock list of products (you can replace with actual data)
products = [
    {'id': 1, 'name': 'Product 1', 'price': 10},
    {'id': 2, 'name': 'Product 2', 'price': 20},
    {'id': 3, 'name': 'Product 3', 'price': 30},
]

def home(request):
    return render(request, 'home.html', {'products': products})

def add_to_cart(request, product_id):
    # Get the product by ID
    product = next((p for p in products if p['id'] == product_id), None)
    
    if product:
        # Add to cart in session (cart is a list stored in the session)
        cart = request.session.get('cart', [])
        
        # Check if the product is already in the cart, if so increase the quantity
        for item in cart:
            if item['id'] == product_id:
                item['quantity'] += 1
                break
        else:
            # Product not in cart, add it
            cart.append({'id': product['id'], 'name': product['name'], 'price': product['price'], 'quantity': 1})

        # Save cart back to session
        request.session['cart'] = cart

    return redirect('cart')

def cart(request):
    cart = request.session.get('cart', [])
    
    # Calculate total price
    total_price = sum(item['price'] * item['quantity'] for item in cart)
    
    return render(request, 'cart.html', {'cart': cart, 'total_price': total_price})


def remove_from_cart(request, product_id):
    cart = request.session.get('cart', [])

    # Remove the product from the cart
    cart = [item for item in cart if item['id'] != product_id]

    # Save updated cart back to session
    request.session['cart'] = cart

    return redirect('cart')
