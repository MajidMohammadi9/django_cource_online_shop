from django.shortcuts import get_list_or_404,redirect,render,HttpResponse
from django.views import generic
from django.urls import reverse
from django.utils.translation import gettext as _
from django.contrib import messages

from .models import Product,Comment
from .forms import CommentForm


def test_translation(request):
    result=_('Hello')
    messages.success(request,'This is a success message.')
    messages.warning(request,'This is a warning messages.')
    messages.error(request,'This is a error message.')
    return render(request,'products/testhello.html')

class ProductListView(generic.ListView):
    queryset=Product.objects.filter(active=True)
    template_name='products/product_list.html'
    context_object_name='products'

"""class ProductDetailView(generic.DetailView):
    model=Product
    template_name='products/product_detail.html'
    context_object_name='product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        return context 

# if you want to use this class,you have to set form action="{% url 'comment_create' product.id %}"
class CommentCreateView(generic.CreateView):
    model=Comment
    form_class=CommentForm
    
    def form_valid(self,form):
        obj=form.save(commit=False)
        obj.author=self.request.user
        product_id=int(self.kwargs['product_id'])
        product=get_object_or_404(Product,pk=product_id)
        obj.product=product
        return super().form_valid(form)"""

class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'

    # def active_comments(self):
    #     return self.object.comments.filter(active=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        #context['comments'] = self.object.comments.all()  # Assuming there is a related name `comments` on Product
        # context['active_comments']=self.object.comments.filter(active=True)
        # context['active_comments']=self.active_comments()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        comment_form = CommentForm(request.POST)
        
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.author = request.user
            new_comment.product = self.object
            new_comment.save()
            return redirect(reverse('product_detail', args=[self.object.pk]))

        # If form is invalid, re-render the page with the invalid form and existing context
        context = self.get_context_data()
        context['comment_form'] = comment_form
        return self.render_to_response(context)

