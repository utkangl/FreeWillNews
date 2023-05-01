from django.shortcuts import render

def home(request):
    context =  {}
    try:
        return render(request, "myApp/home.html", context)
    except:
        print("the template does not exist")
        
        
def faq(request):
    context =  {}
    try:
        return render(request, "myApp/faq.html", context)
    except:
        print("the template does not exist")
        
        
def contact(request):
    context =  {}
    try:
        return render(request, "myApp/contact.html", context)
    except:
        print("the template does not exist")
        
def login(request):
    context =  {}
    try:
        return render(request, "myApp/login.html", context)
    except:
        print("the template does not exist")