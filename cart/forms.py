from django import forms


class AddToCartProductForm(forms.Form):
    QUANTITY_CHOICES=[(i,str(i)) for i in range(1,31)]
    quantity=forms.TypedChoiceField(choices=QUANTITY_CHOICES,coerce=int)


    # If inplace=False and we click the Add to Cart button, the amount will be added to the previous amount and sent.
    # If inplace=True and we click the Add to Cart button, the current amount will be sent.(usage on 'cart_detail.html')
    inplace=forms.BooleanField(required=False,widget=forms.HiddenInput)

