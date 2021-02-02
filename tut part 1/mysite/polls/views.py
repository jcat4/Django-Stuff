from django.http import HttpResponse


def index(request):
    return HttpResponse("Yo, you're at the poll index")