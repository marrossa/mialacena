from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Product


def index(request):
    products = Product.objects.order_by('-exp_date')
    context = { 'products' : products }
    return render(request, 'products/index.html', context)

def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'products/detail.html', {'product': product})

def comments(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'products/comments.html', {'product' : product})

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
