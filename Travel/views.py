from django.shortcuts import render, redirect
from .models import Package
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm
from .models import Order
from .forms import OrderForm

# Create your views here.
def package(request):
    packages = Package.objects.order_by('title')
    return render(request, 'Travel/package.html', {'packages':packages})

@login_required
def orders(request):
    client = request.user
    orders = Order.objects.filter(Customer=client)
    return render(request, 'Travel/orders.html', {'orders':orders})

def index(request):
    return render(request, 'Travel/index.html', {})

def how(request):
    return render(request,'Travel/how.html', {})

def contact(request):
    return render(request, 'Travel/contact.html', {})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/login')
    else:
        form = SignUpForm()
    return render(request, 'Travel/signup.html', {'form': form})

@login_required
def client(request):
    if request.method=="POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)            order.Price = get_price(order.Package, order.Number_of_travelers)
            order.save()
            return redirect('orders')
    form = OrderForm()
    return render(request, 'Travel/client.html', {'form':form})


def get_price(package, num_of_people):
    total_price = num_of_people * package.price
    return total_price



