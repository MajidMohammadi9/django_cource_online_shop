from django.contrib import messages
from django.utils.translation import gettext as _

from products.models import Product

class Cart:
    def __init__(self,request):
        """
            Initialize the cart
        """
        self.request=request
        self.session=request.session

        self.cart=self.session.setdefault('cart',{})
        
    def add(self,product,quantity=1,replace_current_quantity=False):
        """
            Add the specified product to the cart if it exists.
        """
        product_id=str(product.id)
        
        if product_id not in self.cart:
            self.cart[product_id]={'quantity':0}
        if replace_current_quantity:
            self.cart[product_id]['quantity']=quantity
        else:
            self.cart[product_id]['quantity']+=quantity
        # self.cart[product_id]={'quantity':self.cart.get(product_id,{}).get('quantity',0) + quantity}
        
        messages.success(self.request,_('Product successfully added to cart.'))
        self.save()

    def save(self):
        """
		  Mark session as modified to save changes
		"""
        self.session.modified=True

    def remove(self,product):
        """
            Remove a product from cart
        """
        product_id=str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
        messages.success(self.request,_('Product successfully removed from cart.'))
        self.save()    

    def __iter__(self):
        product_ids=self.cart.keys()
        products=Product.objects.filter(id__in=product_ids)
        cart=self.cart.copy()
        for product in products:
            cart[str(product.id)]['product_obj']=product
        for item in cart.values():
            item['total_price']=item['quantity']*item['product_obj'].price
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())
    
    def clear(self):
        del self.session['cart']
        self.save()

    def get_total_price(self):
        product_ids=self.cart.keys()
        # products=Product.objects.filter(id__in=product_ids)
        # return sum(item['quantity']*product.price for item,product in zip(self.cart.values(),products))
        return sum(item['quantity']*item['product_obj'].price for item in self.cart.values())
        """
            when we use 'for item in self.cart.values()', it Calls '__iter__' internally
            and '__iter__' returns 'item' which contains 'product_obj'
        """