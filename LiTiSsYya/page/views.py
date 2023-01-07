from django.shortcuts import render

# Create your views here.


#About
def About(request):
    return render(request, 'page/about.html')
#Privacy
def Privacy(request):
    return render(request, 'page/privacy.html')
#Terms
def Terms(request):
    return render(request, 'page/terms.html')
#Docs

def Docs(request):
    return render(request, 'page/docs.html')

# Create your views here.

