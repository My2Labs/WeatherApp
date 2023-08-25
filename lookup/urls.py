from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('airhtml', views.airhtml, name="airhtml"),
    path('airviews', views.airviews, name="airviews"),
    path('', views.enter, name="enter"),
    path('calculator', views.calculator, name="calculator"),
    path('quantity', views.quantity, name="quantity"),
    ] 

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)