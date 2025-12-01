from django.http import HttpResponse

# Create your views here.

def something(req):
    return HttpResponse("this is thw api page")