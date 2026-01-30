from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.core.files.storage import FileSystemStorage
from django.views import View
from .forms import (ServiceModelForm,
                    MasterModelForm,
                    GalleryModelForm,
                    ReviewModelForm,
                    TypeOfServiceModelForm,
                    SignUpModelForm
                    )
from .filters import (ServiceFilter,
                      MasterFilter,
                      GalleryFilter,
                      ReviewFilter,
                      TypeOfServiceFilter,
                      SignUpFilter
                        )
from django.views.generic.base import TemplateView
from django.views.generic import CreateView, DetailView, ListView
from main.models import Service, Master, Gallery, Review, TypeOfService, SignUp


class HomeTemplate(TemplateView):
    template_name = 'plan/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services'] = Service.objects.all()
        context['masters'] = Master.objects.all()
        context['galleries'] = Gallery.objects.all()
        context['reviews'] = Review.objects.all()
        return context
    

class AboutUsTemplate(TemplateView):
    template_name = 'plan/aboutus.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['masters'] = Master.objects.all()
        return context
    

class ServiceTemplate(TemplateView):
    template_name = 'plan/service.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['typesofservice'] = TypeOfService.objects.all()
        return context
    

class MastersTemplate(TemplateView):
    template_name = 'plan/masters.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['masters'] = Master.objects.all()
        context['galleries'] = Gallery.objects.all()
        return context
    

class MasterDetailTemplate(TemplateView):
    template_name = 'plan/aboutmaster.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        master_id = self.kwargs['id'] 
        context['master'] = Master.objects.get(id=master_id)
        context['galleries'] = Gallery.objects.all()
        context['reviews'] = Review.objects.all()
        return context
    

class SignUpCreate(CreateView):
    model = SignUp
    template_name = 'base.html'
    form_class = SignUpModelForm
    success_url = '/'