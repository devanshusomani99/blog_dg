from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Music Page</h1><br><h2>Hans Zimmer</h2>")
