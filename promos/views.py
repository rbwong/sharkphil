from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse_lazy
from django.views.generic import DetailView

from promos.models import Promo


class PromoPage(DetailView):
    template_name = "promo.html"

    def get_object(self):
        return get_object_or_404(Promo, id=1)

    def get_context_data(self, **kwargs):
        context = super(PromoPage, self).get_context_data(**kwargs)
        return context
