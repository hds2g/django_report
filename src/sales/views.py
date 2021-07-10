from django.shortcuts import render
from django.views.generic import ListView
from .models import Sale

# Create your views here.
def home_view(request):
    message = 'hello from sales'
    return render(request, 'sales/home.html', {'message':message})


class SaleListView(ListView):
    model = Sale
    template_name = 'sales/main.html'
    context_object_name = 'qs'