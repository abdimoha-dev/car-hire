
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.urlpatterns import format_suffix_patterns
from carpass import views

schema_view = get_schema_view(
   openapi.Info(
      title="CAR HIRE API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://myapp/policies/terms/",
      contact=openapi.Contact(email="cahire@carpass.local"),
      license=openapi.License(name="Test License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
    path('', include('carpass.urls')),
    path('admin/', admin.site.urls),
    # path('carapi/', views.CarList.as_view()),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
