from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse_lazy
from django.views.generic import DetailView

from company.models import Profile
from series.models import Series
from accessories.models import Accessory


class SeriesPage(DetailView):
    template_name = "series.html"

    def get_object(self):
        return get_object_or_404(Series, id=self.args[0])

    def get_context_data(self, **kwargs):
        context = super(SeriesPage, self).get_context_data(**kwargs)
        context['accessory_list'] = Accessory.objects.filter(series=self.object).order_by('name')
        return context
