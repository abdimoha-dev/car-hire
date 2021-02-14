from django.shortcuts import render, get_object_or_404, redirect, HttpResponsePermanentRedirect
from django.template import loader
from django.http import HttpResponse, Http404, JsonResponse
from .models import Car
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users, admin_only
from django.contrib.auth.models import Group
from django.contrib.auth.models import User, Group
# from django import template

from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework import viewsets
from .serializers import CarSerializer
from rest_framework import status
from rest_framework.decorators import api_view

#create new user
@unauthenticated_user #if user is authenticated, dont show register page
def register_Page(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='customer')
            user.groups.add(group)
            messages.success(request, 'Account was created for '+username)
            return redirect('login')

    context = {'form': form}
    return render(request, 'accounts/register.html', context)


# user login
@unauthenticated_user
def login_Page(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password = request.POST.get('password')
        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            users_in_group = Group.objects.get(name="admin").user_set.all()
            if request.user in users_in_group:
                return redirect('show_cars')
            else:
                return redirect('customer_index')
                
        else:
            messages.info(request, 'Username OR password is incorrect')
            # return render(request,'accounts/login.html')
            

    return render(request, 'accounts/login.html')
#show customer list of available cars
@login_required(login_url='login')
def customer_index_page(request):
    cars = Car.objects.all().filter(booked=False)
    context = {'cars':cars}
    return render(request, 'index.html', context)

@login_required(login_url='login')
def my_cars(request):
    cars = Car.objects.filter(booked_by=request.user.id)
    context = {
        'cars': cars
    }
    return render(request, 'carpass/my_cars.html',context)

@login_required(login_url='login')
@allowed_users(['admin'])
def show_cars(request):
    cars = Car.objects.all()
    groups =  Group.objects.get(name="admin").user_set.all()
    
    context = {
        'cars': cars,
        'groups': groups
    }
    return render(request, 'carpass/all_cars.html', context)


@login_required(login_url='login')
def index(request):
    return render(request, 'carpass/home.html')

@login_required(login_url='login')
@allowed_users(['admin'])
def add_car(request):
    if request.method == 'POST':
        car_model = request.POST.get('car_model')
        car_numberplate = request.POST.get('car_numberplate')
        car_image = request.FILES['car_image']
        car_sits = request.POST.get('car_sits')
        price_per_day = request.POST.get('price_per_day')

        car_details = Car(car_model=car_model, car_numberplate=car_numberplate,
                          car_image=car_image, car_sits=car_sits, price_per_day=price_per_day)

        car_details.save()
        return render(request, 'carpass/add_car.html')

    else:
        return render(request, 'carpass/add_car.html')

@login_required(login_url='login')
@allowed_users(['admin'])
def show_cars(request):
    cars = Car.objects.filter(booked=False)
    groups =  Group.objects.get(name="admin").user_set.all()
    
    context = {
        'cars': cars,
        'groups': groups
    }
    return render(request, 'carpass/all_cars.html', context)

@login_required(login_url='login')
@allowed_users(['admin'])
def delete_car(request, car_id):
    try:
        car = Car.objects.get(pk=car_id)
        print(car)
        car.delete()
        return show_cars(request)

    except Car.DoesNotExist:
        raise Http404("Car Does Not Exist")
    # return show_cars(request)

@login_required(login_url='login')
@allowed_users(['admin'])
def update_car(request, carid):
    if request.method == 'GET':
        car = Car.objects.get(pk=carid)
        context = {'car': car}
        return render(request, 'carpass/edit_car.html', context)
    else:
        car_model = request.POST.get('car_model')
        car_numberplate = request.POST.get('car_numberplate')
        car_image = request.FILES['car_image']
        car_sits = request.POST.get('car_sits')
        price_per_day = request.POST.get('price_per_day')

        Car.objects.filter(id=carid).update(car_model=car_model, car_numberplate=car_numberplate,
                                            car_image=car_image, car_sits=car_sits, price_per_day=price_per_day)
        cars = Car.objects.all()
        context = {
            'cars': cars
        }
        return render(request, 'carpass/all_cars.html', context)



def logout_user(request):
    logout(request)
    return HttpResponsePermanentRedirect('login')

@login_required(login_url='login')
def customer_index_page(request):
    cars = Car.objects.all().filter(booked=False)
    context = {'cars':cars}
    return render(request, 'index.html', context)

@login_required(login_url='login')
def book_car(request, carid):
    booked = True
    booked_by = request.user.id
    car = Car.objects.filter(pk=carid).update(booked=booked, booked_by=booked_by)
    cars = Car.objects.all().filter(booked=False)
    
    context = {'cars':cars}
    return render(request, 'index.html', context)

@login_required(login_url='login')
@allowed_users(['admin'])
def booked_cars(request):
    cars = Car.objects.filter(booked=True)
    context = {
        'cars':cars
    }
    return render(request,'carpass/booked_cars.html',context )


class CarList(APIView):
    def get(self, request):
        cars1 = Car.objects.all()
        serializers = CarSerializer(cars1, many=True)
        
        return Response(serializers.data)
# APIs
    
@api_view(['GET'])    
def apiOverview(request):
    api_urls = {
        'list': '/car-list/',
        'detail view': '/car-detail/<str:pk>/',
        'create':'/car-create/',
        'update':'car-update/<str:pk>/',
        'delete':'/car-delete/<str:pk>/'
    }
    return Response(api_urls)

@api_view(['GET']) 
def carList(request):
    cars = Car.objects.all()
    serializer = CarSerializer(cars, many=True)
    return Response(serializer.data)

@api_view(['GET']) 
def carDetails(request, pk):
    cars = Car.objects.get(id=pk)
    serializer = CarSerializer(cars, many=False)
    return Response(serializer.data)

@api_view(['POST']) 
def carCreate(request):
    serializer = CarSerializer(data=request.data)
    data = {}
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST']) 
def carUpdate(request, pk):
    cars = Car.objects.get(id=pk)
    serializer = CarSerializer(instance=cars, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE']) 
def carDelete(request, pk):
    cars = Car.objects.get(id=pk)
    cars.delete()

    return Response('Item successfully deleted')