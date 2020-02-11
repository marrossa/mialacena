from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.views import generic, View
from django.forms.models import model_to_dict

from .models import Product, ProductComment

class IndexJsonView(View):
    def get(self, request):
        products = Product.objects.order_by('-exp_date').values()
        return JsonResponse({'products':list(products)}, safe=False)

class DetailJsonView(View):
    def get(self, request, *args, **kwargs):
        product = Product.objects.filter(pk=self.kwargs['pk']).values().first()
        return JsonResponse({'product': product})

@method_decorator(csrf_exempt, name='dispatch')
class CreateProductJsonView(View):
    def post(self, request):
        product = Product(name=request.POST.get('name'),
            exp_date=request.POST.get('exp_date'),
            description=request.POST.get('description'),
            quantity=request.POST.get('quantity'))
        product.save()
        return JsonResponse({'product': model_to_dict(product)})

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
