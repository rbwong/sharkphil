from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse_lazy
from django.views.generic import DetailView

from company.models import Profile
from products.models import Product
from productimages.models import ProductImage


class ProductPage(DetailView):
    template_name = "product.html"

    def get_object(self):
        return get_object_or_404(Product, id=self.args[0])

    def get_context_data(self, **kwargs):
        context = super(ProductPage, self).get_context_data(**kwargs)
        context['productimage_list'] =ProductImage.objects.filter(product=self.object).order_by('name')
        return context
