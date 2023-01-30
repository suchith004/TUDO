"""tudoi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from tudoi.views import homepage
from tudoi.views import menshp
from tudoi.views import login
from tudoi.views import signup
from tudoi.views import forgotpassword
from tudoi.views import womenhp
from tudoi.views import cart
from tudoi.views import checkout
from tudoi.views import prodd
from tudoi.views import firstpage
from tudoi.views import connect
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',firstpage),
    path('login',login,name="login"),
    path('signup',signup,name="signup"),
    path('forgotpassword',forgotpassword,name="forgotpassword"),
    path('homepage',homepage,name="homepage"),
    path('menshp',menshp,name="menshp"),
    path('womenhp',womenhp,name="womenhp"),
    path('cart',cart,name="cart"),
    path('checkout',checkout,name="chechout"),
    path('product-details',prodd,name="product-details"),
    path('connect',connect,name="connect",)
         
]



