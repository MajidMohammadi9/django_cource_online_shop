from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.translation import gettext as _

from .forms import OrderForm
from cart.cart import Cart
from .models import OrderItem

@login_required
def order_create_view(request):
    order_form=OrderForm()  # to spicify errors if there are errors, so as a context will be sent to temlate.
    cart=Cart(request)

    if len(cart)==0:
        messages.warning(request, _('You can not proceed to checkout page, because your cart is empty!'))

    if request.method=='POST':
        order_form=OrderForm(request.POST,)

        if order_form.is_valid():
            order_obj=order_form.save(commit=False)
            order_obj.user=request.user
            order_obj.save()

            for item in cart:
                product=item['product.obj']
                OrderItem.objects.create(
                    order=order_obj,
                    product=product,
                    quantity=item['quantity'],
                    price=product.price,
                )
            cart.clear()

            request.user.first_name=order_obj.first_name
            request.user.lastname=order_obj.last_name
            request.user.save()

            messages.success(request, _('Your order has successfully placed.'))

    return render(request,'orders/order_create.html',context={'form':order_form,})
