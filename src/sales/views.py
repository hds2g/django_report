from django.shortcuts import render

# Create your views here.
def home_view(request):
    message = 'hello from sales'
    return render(request, 'sales/main.html', {'message':message})

