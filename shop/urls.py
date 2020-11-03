from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="shophome"),
    path('about/', views.about, name="aboutus"),
    path('contact/', views.contact, name="contactus"),
    path('tracker/', views.tracker, name="trackingstatus"),
    path('checkout/', views.checkout, name="checkout"),
    path('products/<int:myid>', views.productView, name="productView"),
    path('search/', views.search, name="search"),
    path('handlerequest/', views.handlerequest, name="handlerequest"),
]
