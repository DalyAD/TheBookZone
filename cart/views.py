from django.shortcuts import render,\
    redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from books.models import Book


def view_cart(request):
    """ A view to return the cart contents page """
    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add a quantity of the specified book to the shopping cart """

    book = get_object_or_404(Book, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    book_format = None
    book_format = request.POST['book_format']
    cart = request.session.get('cart', {})

    if book_format:
        if item_id in list(cart.keys()):
            if book_format in cart[item_id]['books_by_format'].keys():
                cart[item_id]['books_by_format'][book_format] += quantity
                messages.success(request, f'Updated \
                    {book.title} quantity to \
                    {cart[item_id]["books_by_format"][book_format]}')
            else:
                cart[item_id]['books_by_format'][book_format] = quantity
                messages.success(request, f'Added {book.title} to your cart')
        else:
            cart[item_id] = {'books_by_format': {book_format: quantity}}
            messages.success(request, f'Added {book.title} to your cart')

    request.session['cart'] = cart
    return redirect(redirect_url)


def adjust_cart(request, item_id):
    """ Adjust the quantity of the specified
        product to the specified amount """

    book = get_object_or_404(Book, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    book_format = None
    book_format = request.POST['book_format']
    cart = request.session.get('cart', {})

    if book_format:
        if quantity > 0:
            cart[item_id]['books_by_format'][book_format] = quantity
            messages.success(request, f'Updated \
                {book.title} quantity to\
                {cart[item_id]["books_by_format"][book_format]}')
        else:
            del cart[item_id]['books_by_format'][book_format]
            if cart[item_id]['books_by_format']:
                cart.pop(item_id)
            messages.success(request, f'Removed {book.title} from your cart')

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_from_cart(request, item_id):
    """ Remove the specified item from the shopping cart """
    try:
        book = get_object_or_404(Book, pk=item_id)
        book_format = None
        if 'book_format' in request.POST:
            book_format = request.POST['book_format']
        cart = request.session.get('cart', {})

        if book_format:
            del cart[item_id]['books_by_format'][book_format]
            if not cart[item_id]['books_by_format']:
                cart.pop(item_id)
                messages.success(request, f'Removed \
                    {book.title} from your cart')

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
