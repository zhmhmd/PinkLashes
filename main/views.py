from django.shortcuts import get_object_or_404
from django.views.generic.base import TemplateView
from django.views.generic import CreateView

from .forms import SignUpModelForm
from .models import Service, Master, Gallery, Review, TypeOfService, SignUp


class HomeTemplate(TemplateView):
    template_name = "plan/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        type_id = self.request.GET.get("type")

        context["typesofservice"] = TypeOfService.objects.all()

        if type_id:
            context["active_type"] = int(type_id)

            context["masters"] = Master.objects.filter(type_id=type_id).order_by("-id")
            context["galleries"] = Gallery.objects.filter(type_id=type_id).order_by("-id")

            context["reviews"] = (
                Review.objects.all()
            )
        else:
            context["masters"] = Master.objects.all().order_by("-id")
            context["galleries"] = Gallery.objects.all().order_by("-id")

            context["reviews"] = (
                Review.objects
                .select_related("master")
                .order_by("-id")
            )

        return context

class AboutUsTemplate(TemplateView):
    template_name = "plan/aboutus.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        type_id = self.request.GET.get("type")

        context["typesofservice"] = TypeOfService.objects.all()

        if type_id:
            context["active_type"] = int(type_id)

            context["masters"] = Master.objects.filter(type_id=type_id).order_by("-id")

        else:
            context["masters"] = Master.objects.all().order_by("-id")
        return context


class ServiceTemplate(TemplateView):
    template_name = "plan/service.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        types = (
            TypeOfService.objects
            .prefetch_related("services__masters")
            .all()
        )

        context["typesofservice"] = types
        return context


class MastersTemplate(TemplateView):
    template_name = "plan/masters.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        type_id = self.request.GET.get("type")

        context["typesofservice"] = TypeOfService.objects.all()

        if type_id:
            context["active_type"] = int(type_id)

            context["masters"] = Master.objects.filter(type_id=type_id).order_by("-id")
            context["galleries"] = Gallery.objects.filter(type_id=type_id).order_by("-id")

        else:
            context["masters"] = Master.objects.all().order_by("-id")
            context["galleries"] = Gallery.objects.all().order_by("-id")


        return context


class MasterDetailTemplate(TemplateView):
    template_name = "plan/aboutmaster.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        master = get_object_or_404(Master, id=self.kwargs["id"])
        context["master"] = master
        context["galleries"] = Gallery.objects.all()
        context["reviews"] = Review.objects.filter(master=master).order_by("-id")
        context["services"] = master.services.all()

        type_id = self.request.GET.get("type")

        context["typesofservice"] = TypeOfService.objects.all()

        if type_id:
            context["active_type"] = int(type_id)

            context["galleries"] = Gallery.objects.filter(type_id=type_id).order_by("-id")

        else:
            context["galleries"] = Gallery.objects.all().order_by("-id")



        return context


class SignUpCreate(CreateView):
    model = SignUp
    template_name = "base.html"  
    form_class = SignUpModelForm
    success_url = "/"
