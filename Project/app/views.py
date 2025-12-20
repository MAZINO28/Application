from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Product, Category
from django.urls import reverse_lazy

class HomePageView(TemplateView):
    template_name = 'app/home.html'


class AboutPageView(TemplateView):
    template_name = 'app/about.html'


class ProductListView(ListView):
    model = Product
    template_name = 'app/product_list.html'
    context_object_name = 'product'

class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'app/product_detail.html'

class ProductCreateView(CreateView):
    model = Product
    fields = ['name', 'description', 'price', 'image', 'category']
    template_name = 'app/product_create.html'
    
    def form_valid(self, form):
        form.instance.User_id = self.request.user
        form.instance.categorey_id = Category.objects.first()  # Set a default category
        return super().form_valid(form)

class ProductUpdateView(UpdateView):
    model = Product
    fields = ['name', 'description', 'price', 'image', 'category']
    template_name = 'app/product_update.html'

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'app/product_delete.html'
    success_url = reverse_lazy('product')