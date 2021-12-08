from django.http import HttpResponse

def index(request):
    return HttpResponse("результат сложения на WEB")
