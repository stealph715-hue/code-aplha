def cart_item_count(request):
    """Makes the cart count available in every template (for the navbar badge)."""
    if request.user.is_authenticated:
        cart = getattr(request.user, 'cart', None)
        if cart:
            return {'cart_count': cart.total_items()}
    return {'cart_count': 0}
