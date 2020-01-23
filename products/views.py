from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Product, ProductComment

class IndexView(generic.ListView):
    template_name = 'products/index.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.order_by('-exp_date')

class DetailView(generic.DetailView):
    model = Product
    template_name = 'products/detail.html'

class CommentsView(generic.DetailView):
    model = Product
    template_name = 'products/comments.html'

def comment(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    try:
        comment = product.productcomment_set.create(comment_text=request.POST['comment_text'])
    except (KeyError, ProductComment.DoesNotExist):
        # Redisplay the product detail with the comments
        return render(request, 'products/details.html', {
            'product' : product,
            'error_message' : 'Comment cannot be created',
        })
    return HttpResponseRedirect(reverse('products:comments', args=(product.id,)))
