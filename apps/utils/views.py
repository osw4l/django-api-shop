from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from django.views.generic import ListView
from django.views.generic import TemplateView
from django.views.generic import UpdateView, DetailView
from apps.utils.shortcuts import get_object_or_none


class BaseListView(LoginRequiredMixin, ListView):
    pass


class BaseCreateView(LoginRequiredMixin, CreateView):
    template_name = 'apps/base/base_form.html'

    def get_context_data(self, **kwargs):
        context = super(BaseCreateView, self).get_context_data(**kwargs)
        context['action'] = 'Crear'
        return context


class BaseListViewDinamicHeader(LoginRequiredMixin, ListView):
    context_object_name = "list"
    query_fields = ()
    HEADER = None

    def __init__(self):
        super(BaseListViewDinamicHeader, self).__init__()
        self.HEADER += ('Acciones',)

    def get_queryset(self):
        return self.model.objects.all()

    def get_context_data(self, **kwargs):
        context = super(BaseListViewDinamicHeader, self).get_context_data(**kwargs)
        context['header_table'] = self.get_header_table()
        return context

    def get_header_table(self):
        return self.HEADER


class DirectDeleteMixin(object):
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class BaseUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'apps/base/base_form.html'

    def get_context_data(self, **kwargs):
        context = super(BaseUpdateView, self).get_context_data(**kwargs)
        context['action'] = 'Modificar'
        return context

    def get_object(self, queryset=None):
        obj = self.model.objects.get(id=self.kwargs['pk'])
        return obj


class BaseTemplateView(LoginRequiredMixin, TemplateView):
    pass


class BaseDetailView(LoginRequiredMixin, DetailView):
    pass
