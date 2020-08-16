from django.shortcuts import render, redirect, reverse, HttpResponse


def view_cart(request):
    """ A view to return the cart contents page """
    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add a quantity of the specified book to the shopping cart """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    book_format = None
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


def adjust_cart(request, item_id):
    """ Adjust the quantity of the specified product to the specified amount """

    quantity = int(request.POST.get('quantity'))
    book_format = None
    book_format = request.POST['book_format']
    cart = request.session.get('cart', {})

    if book_format:
        if quantity > 0:
            cart[item_id]['books_by_format'][book_format] = quantity
        else:
            del cart[item_id]['books_by_format'][book_format]
            if cart[item_id]['books_by_format']:
                cart.pop(item_id)
    else:
        if quantity > 0:
            cart[item_id] = quantity
        else:
            cart.pop(item_id)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_from_cart(request, item_id):
    """ Remove the specified item from the shopping cart """
    try:
        book_format = None
        if 'book_format' in request.POST:
            book_format = request.POST['book_format']
        cart = request.session.get('cart', {})

        if book_format:
            del cart[item_id]['books_by_format'][book_format]
            if not cart[item_id]['books_by_format']:
                cart.pop(item_id)
        else:
            cart.pop(item_id)

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
