from django.urls import path, include
from django.contrib.auth import logout
from . import views

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="CAR HIRE API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://myapp/policies/terms/",
      contact=openapi.Contact(email="contact@carhire.local"),
      license=openapi.License(name="Test License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', views.index, name ='index'),
    path('addcar', views.add_car, name='addcar'),
    path('show_cars/', views.show_cars, name='show_cars'),
    path('<int:car_id>/delete', views.delete_car, name='delete_car'),
    path('edit/<int:carid>', views.update_car, name='update_car'),
    path('login',views.login_Page, name='login'),
    path('register', views.register_Page, name='register'),
    path('logout', views.logout_user, name='logout'),
    path('customer/index', views.customer_index_page, name='customer_index'),
    path('<int:carid>/book', views.book_car, name = 'book'),
    path('all/booked', views.booked_cars, name = 'booked_cars'),
    path('mycars/', views.my_cars, name='my_cars'),
    
    
    
    # REST FRAMEWOK APIs
    path('api/', views.apiOverview, name="api-overview"),
    path('car-list/', views.carList, name ="car-list"),
    path('car-detail/<str:pk>/', views.carDetails, name ="car-detail"),
    path('car-create/', views.carCreate, name ="car-create"),
    path('car-update/<str:pk>/', views.carUpdate, name ="car-update"),
    path('car-delete/<str:pk>/', views.carDelete, name ="car-delete"),
    


  
]