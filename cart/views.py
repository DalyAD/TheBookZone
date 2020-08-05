from django.shortcuts import render, redirect


def view_cart(request):
    """ A view to return the cart contents page """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add a quantity of hte specified book to the shopping cart """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    book_format = None
    if 'book_format' in request.POST:
        book_format = request.POST['book_format']
    cart = request.session.get('cart', {})

    if book_format:
        if item_id in list(cart.keys()):
            if book_format in cart[item_id]['books_by_format'].keys():
                cart[item_id]['books_by_format'][book_format] += quantity
            else:
                cart[item_id]['books_by_format'][book_format] = quantity
        else:
            cart[item_id] = {'books_by_format': {book_format: quantity}}
    else:
        if item_id in list(cart.keys()):
            cart[item_id] += quantity
        else:
            cart[item_id] = quantity

    request.session['cart'] = cart
    return redirect(redirect_url)
