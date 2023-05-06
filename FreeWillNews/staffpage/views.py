from django.shortcuts import render

def uploadnew(request):
    context =  {}
    try:
        return render(request, "./uploadnew/uploadnew.html", context)
    except:
        print("the template does not exist")
