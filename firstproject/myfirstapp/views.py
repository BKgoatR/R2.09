from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'myfirstapp/index.html')

def bonjour(request):
    contexte = {
        "nom": request.GET.get("nom"),
        "prenom": request.GET.get("prenom"),
        "age": request.GET.get("age"),
    }
    return render(request, 'myfirstapp/bonjour.html', contexte)