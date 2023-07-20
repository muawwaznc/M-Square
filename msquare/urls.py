"""msquare URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from msquare import views
from app import views as appViews



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePage),
    path('become-a-seller/', views.BecomeSeller),
    path('become-a-seller/signup/', appViews.GetSellerData),
    path('track-my-order/', views.TrackMyOrder),    
    path('best-seller/', views.BestSeller),
    path('login/', views.Login),
    path('login/user-check/', appViews.CheckLogin),
    path('signup/', views.Signup),
    path('signup/buyer/', appViews.getBuyerData),
    path('cart/', views.Cart),
    path('cart/buy/', appViews.buyCartProduct),
    path('cart/remove/', appViews.delFromCart),
    path('fashion/', views.Fashion),
    path('electronics/', views.Electronics),
    path('jewellery/', views.Jewellery),
    path('product-detail/<int:pID>/', views.ProductDetails, name='product-detail'),
    path('add-to-cart/', appViews.addToCart),

    path('seller-dashboard/', views.sellerDashboard),
    path('add-new-product/', views.addNewProduct),
    path('add-new-product/add/', appViews.getProductData),
    path('remove-product/', views.removeProduct),
    path('remove-product/update/', appViews.updateProduct),
    path('remove-product/remove/', appViews.removeProduct),
    path('manage-orders/', views.manageOrders),
    path('manage-orders/deliver/', appViews.deliverOrder),
    path('earnings/', views.earnings),
    path('check/', views.Check)    
]