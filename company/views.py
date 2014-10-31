from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, DetailView

from company.models import Profile
from make.models import Make
from series.models import Series
from accessories.models import Accessory
from products.models import Product
from productimages.models import ProductImage
from promos.models import Promo


class IndexPage(DetailView):
    template_name = "index.html"

    def get_object(self):
        return get_object_or_404(Profile, id=1)

    def get_context_data(self, **kwargs):
        context = super(IndexPage, self).get_context_data(**kwargs)
        context['make_list'] = Make.objects.all().order_by('name')
        context['series_list'] = Series.objects.all().order_by('name')
        context['brand_logo'] = self.object.logo
        return context
