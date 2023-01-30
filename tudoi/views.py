from django.shortcuts import render

def firstpage(request):
    return render(request,'firstpage.html')
def login(request):
    return render(request,'login.php')
def signup(request):
    return render(request,'signup.php')
def forgotpassword(request):
    return render(request,'forgotpassword.html')
def homepage(request):
    return render(request,'homepage.html')

def menshp(request):
    return render(request,'menshp.html')

def womenhp(request):
    return render(request,'womenhp.html')
def cart(request):
    return render(request,'cart.html')
def checkout(request):
    return render(request,'checkout.html')
def prodd(request):
    return render(request,'product-details.html')
def fp(request):
    return render(request,'firstpage.html')
def connect(request):
    return render(request,login.php)