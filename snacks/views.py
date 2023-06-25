from django.views.generic import ListView, DetailView, TemplateView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import Snack


# class-based views (instead of function-based views)
class SnackListView(ListView):
    template_name = "snack_list.html"
    model = Snack
    context_object_name = "snacks"


class SnackDetailView(DetailView):
    template_name = "snack_detail.html"
    model = Snack


class SnackAboutView(TemplateView):
    template_name = 'about.html'


# CRUD views:
class SnackCreateView(CreateView):
    template_name = "snack_create.html"
    model = Snack
    fields = ["title", "purchaser", "description", "info_url"]


class SnackDeleteView(DeleteView):
    template_name = "snack_delete.html"
    model = Snack
    success_url = reverse_lazy("snack_list")


class SnackUpdateView(UpdateView):
    template_name = "snack_update.html"
    model = Snack
    fields = ["title", "purchaser", "description", "info_url"] # can alternatively use "__all__" to include all cols

