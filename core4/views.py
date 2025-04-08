import form
from django.shortcuts import render, redirect, HttpResponse
from .models import AboutUs, Contact
from .models import Blog
from .models import Price
from .form import ContactForm, UserForm, RegisterForm
from .models import Register

def about(request):
    about_us = AboutUs.objects.all()
    return render(request, 'about.html', {
        'about_us': about_us
    })


def blog(request):
    blog = Blog.objects.all()
    return render(request, 'blog.html', {
        'blog': blog
    })

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {
        'form': form
    })


def success(request):
    return HttpResponse('Success')


def index(request):
    about_us = AboutUs.objects.all()
    blog = Blog.objects.all()
    contact = Contact.objects.all()
    price = Price.objects.all()
    register = Register.objects.all()
    return render(request, 'index.html',{
        'about_us': about_us,
        'blog': blog,
        'contact': contact,
        'price': price,
        'register': register
    })


def price(request):
    price = Price.objects.all()
    return render(request, 'price.html', {
        'price': price
    })

def service(request):
    return render(request, 'service.html')

def single(request):
    return render(request, 'single.html')




def register(request, form=None):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'register.html', {'form': form,'is_success': True})
    else:
        return render(request, 'register.html', {'form': form, 'is_success': False})

    return render(request, 'register.html', {'form': form, 'is_success': False})


